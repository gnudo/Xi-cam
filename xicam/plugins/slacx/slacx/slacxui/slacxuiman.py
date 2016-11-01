import os
from datetime import datetime as dt
import time
from functools import partial

from PySide import QtGui, QtCore, QtUiTools
import numpy as np

from . import uitools
from .opuiman import OpUiManager
from ..slacxcore.operations.slacxop import Operation
from ..slacxcore import slacxtools
from . import data_viewer

class UiManager(object):
    """
    Stores a reference to a QMainWindow,
    performs operations on it
    """

    # TODO: when the QImageView widget gets resized,
    # it will call QWidget.resizeEvent().
    # Try to use this to resize the images in the QImageView.

    def __init__(self):
        """Make a UI from ui_file, save a reference to it"""
        # Pick a UI definition, load it up
        ui_file = QtCore.QFile(slacxtools.rootdir+"/slacxui/basic.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        # load() produces a QMainWindow(QWidget).
        self.ui = QtUiTools.QUiLoader().load(ui_file)
        ui_file.close()
        # Set up the self.ui widget to delete itself when closed
        self.ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.opman = None    
        self.wfman = None
        #self.op_uimans = [] 

    def apply_workflow(self,logmethod=None):
        """
        run the workflow
        """
        self.msg_board_log('Starting workflow executor...')
        # Check for a batch executor...
        if 'EXECUTION.BATCH' in [item.data[0].categories for item in self.wfman.root_items]:
            self.msg_board_log('Beginning BATCH execution')
            self.wfman.run_wf_batch()
        else:
            self.msg_board_log('Beginning serial execution')
            self.wfman.run_wf_serial()

    def edit_op(self,item_indx=None):
        """
        interact with user to edit operations in the workflow
        """
        if not item_indx:
            item_indx = self.ui.workflow_tree.currentIndex()
        if item_indx:
            x = self.opman.get_item(item_indx).data[0]
            if issubclass(type(x),Operation):
                uiman = self.start_op_ui_manager(x,self.wfman,self.wfman)
                uiman.ui.op_selector.setCurrentIndex(item_indx)
                # TODO: add ways to 'save' edited ops, or do it automatically
                uiman.ui.show()
            uiman.ui.finish_button.clicked.disconnect()
            uiman.ui.finish_button.clicked.connect( partial(uiman.update_op,selected_indxs[0]) )
            uiman.ui.show()

    def rm_op(self):
        """
        remove the selected operation in the workflow list from the workflow
        """
        # TODO: implement multiple selection 
        # TODO: take out the garbage
        selected_indxs = self.ui.workflow_tree.selectedIndexes()
        #for indx in selected_indxs:
        self.wfman.remove_op(selected_indxs[0])

    def add_op(self,item_indx=None):
        """
        interact with user to build an operation into the workflow
        """
        if not item_indx:
            item_indx = self.ui.op_tree.currentIndex()
        if item_indx.isValid(): 
            if self.opman.get_item(item_indx).n_data() > 0:
                x = self.opman.get_item(item_indx).data[0]
                if isinstance(x,str):
                    pass
                elif issubclass(x,Operation):
                    uiman = self.start_op_ui_manager(x(),self.wfman,self.opman)
                    uiman.ui.op_selector.setCurrentIndex(item_indx)
                    uiman.ui.show()
        else:
                    uiman = self.start_op_ui_manager(None,self.wfman,self.opman)
                    uiman.ui.show()
            

    def start_op_ui_manager(self,current_op,wfm,opm):
        """
        Create a QFrame window from ui/op_builder.ui, then return it
        """
        uiman = OpUiManager(wfm,opm)
        if current_op:
            uiman.set_op(current_op)
        uiman.ui.setParent(self.ui,QtCore.Qt.Window)
        return uiman

    def display_item(self,indx):
        """
        Display selected item from the workflow tree in image_viewer 
        """
        if indx: 
            if self.wfman.get_item(indx).n_data() > 0:
                to_display = self.wfman.get_item(indx).data[0]
                uri = self.wfman.build_uri(indx)
                data_viewer.display_item(to_display,uri,self.ui.image_viewer,None)

    def final_setup(self):
        # Let the message board be read-only
        self.ui.message_board.setReadOnly(True)
        # Let the message board ignore line wrapping
        self.ui.message_board.setLineWrapMode(self.ui.message_board.NoWrap)
        # Tell the status bar that we are ready.
        self.show_status('Ready')
        # Tell the message board that we are ready.
        self.ui.message_board.insertPlainText('--- MESSAGE BOARD ---\n') 
        self.msg_board_log('slacx is ready') 
        # Clear any default tabs out of image_viewer
        #self.ui.center_frame.setMinimumWidth(200)
        self.ui.op_tree.resizeColumnToContents(0)
        self.ui.workflow_tree.resizeColumnToContents(0)
        self.ui.workflow_tree.resizeColumnToContents(1)
        self.ui.splitter.setStretchFactor(1,24)    

    def connect_actions(self):
        """Set up the works for buttons and menu items"""
        #self.ui.workflow_tree.activated.connect(self.display_item)
        self.ui.workflow_tree.clicked.connect(self.display_item)
        # Connect self.ui.image_viewer tabCloseRequested to local close_tab slot
        #self.ui.image_viewer.tabCloseRequested.connect(self.close_tab)
        # Connect self.ui.add_op_button:
        self.ui.add_op_button.setText("&Add")
        self.ui.add_op_button.clicked.connect(self.add_op)
        # Connect self.ui.rm_op_button:
        self.ui.rm_op_button.setText("&Delete")
        self.ui.rm_op_button.clicked.connect(self.rm_op)
        # Connect self.ui.edit_op_button:
        self.ui.edit_op_button.setText("&Edit")
        self.ui.edit_op_button.clicked.connect(self.edit_op)
        # Connect self.ui.apply_workflow_button:
        self.ui.apply_workflow_button.setText("&Run")
        self.ui.apply_workflow_button.clicked.connect(self.apply_workflow)
        # Connect self.ui.workflow_tree (QTreeView) to self.wfman (WfManager(TreeModel))
        self.ui.workflow_tree.setModel(self.wfman)
        # Connect self.ui.op_tree (QTreeView) to self.opman (OpManager(TreeModel))
        self.ui.op_tree.setModel(self.opman)
        self.ui.op_tree.hideColumn(1)
        self.ui.op_tree.doubleClicked.connect(self.add_op)

    def make_title(self):
        """Display the slacx logo in the image viewer"""
        # Load the slacx graphic  
        slacx_img_file = os.path.join(slacxtools.rootdir, "slacxui/slacx_icon_white.png")
        # Make a QtGui.QPixmap from this file
        slacx_pixmap = QtGui.QPixmap(slacx_img_file)
        # Make a QtGui.QGraphicsPixmapItem from this QPixmap
        slacx_pixmap_item = QtGui.QGraphicsPixmapItem(slacx_pixmap)
        # Add this QtGui.QGraphicsPixmapItem to a QtGui.QGraphicsScene 
        slacx_scene = QtGui.QGraphicsScene()
        slacx_scene.addItem(slacx_pixmap_item)
        qwhite = QtGui.QColor(255,255,255,255)
        textitem = slacx_scene.addText("v{}".format(slacxtools.version))
        textitem.setPos(100,35)
        textitem.setDefaultTextColor(qwhite)
        # Add the QGraphicsScene to self.ui.image_viewer layout 
        logo_view = QtGui.QGraphicsView()
        logo_view.setScene(slacx_scene)
        #logo_view.setStyleSheet( "QTextEdit { color: white  }" + self.ui.styleSheet() )
        #logo_view.setStyleSheet( "QGraphicsTextItem { color: white  }" + self.ui.styleSheet() )
        #logo_view.setStyleSheet( "QGraphicsView { color: white  }" + self.ui.styleSheet() )
        #textitem.setStyleSheet( "QGraphicsTextItem { color: white  }" + self.ui.styleSheet() )
        self.ui.image_viewer.addWidget(logo_view,0,0,1,1)
        #self.ui.title_box.setScene(slacx_scene)
        # Set the main window title and icon
        self.ui.setWindowTitle("slacx v{}".format(slacxtools.version))
        self.ui.setWindowIcon(slacx_pixmap)
 

    # Various simple utilities
    @staticmethod 
    def dtstr():
        """Return date and time as a string"""
        #return dt.strftime(dt.now(),'%Y %m %d, %H:%M:%S')
        return dt.strftime(dt.now(),'%m %d, %H:%M:%S')

    def msg_board_log(self,msg):
        """Print timestamped message with space to msg board"""
        self.ui.message_board.insertPlainText(
        '- ' + self.dtstr() + ': ' + msg + '\n') 
        self.ui.message_board.verticalScrollBar().setValue(99)
      
    def show_status(self,msg):
        self.ui.statusbar.showMessage(msg)

    def export_image(self):
        """export the image in the currently selected tab"""
        pass

    def edit_image(self):
        """open an image editor for the current tab"""
        pass

    # A QtCore.Slot for closing tabs from image_viewer
    #@QtCore.Slot(int)
    #def close_tab(self,indx):
    #    self.ui.image_viewer.removeTab(indx)

