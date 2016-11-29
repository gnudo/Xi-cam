from PySide import QtGui
from PySide import QtCore


class difftoolbar(QtGui.QToolBar):
    sigCake = QtCore.Signal()
    sigRemesh = QtCore.Signal()
    def __init__(self):
        super(difftoolbar, self).__init__()

        self.actionCenterFind = QtGui.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("xicam/gui/icons_27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenterFind.setIcon(icon1)
        self.actionCenterFind.setObjectName("actionCenterFind")
        self.actionCenterFind.setToolTip('Auto-calibrate AgB')
        self.actionPolyMask = QtGui.QAction(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("xicam/gui/icons_05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPolyMask.setIcon(icon2)
        self.actionPolyMask.setToolTip('Polygon mask')
        self.actionPolyMask.setText("")
        self.actionPolyMask.setObjectName("actionPolyMask")
        self.actionOpen = QtGui.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setToolTip('Open')
        self.actionSaveExperiment = QtGui.QAction(self)
        self.actionSaveExperiment.setObjectName("actionSaveExperiment")
        self.actionSaveExperiment.setToolTip('Save experiment')
        self.actionLoadExperiment = QtGui.QAction(self)
        self.actionLoadExperiment.setObjectName("actionLoadExperiment")
        self.actionLoadExperiment.setToolTip('Load experiment')
        self.actionClose = QtGui.QAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.setToolTip('Close Xi-cam')
        self.actionMasking = QtGui.QAction(self)
        self.actionMasking.setToolTip('Masking')
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("xicam/gui/icons_03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMasking.setIcon(icon3)
        self.actionMasking.setObjectName("actionMasking")
        self.actionLog_Intensity = QtGui.QAction(self)
        self.actionLog_Intensity.setCheckable(True)
        self.actionLog_Intensity.setToolTip('Log intensity')
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("xicam/gui/icons_02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog_Intensity.setIcon(icon4)
        self.actionLog_Intensity.setObjectName("actionLog_Intensity")
        self.actionLog_Intensity.setChecked(True)
        self.actionCake = QtGui.QAction(self)
        self.actionCake.setToolTip('Cake')
        self.actionCake.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("xicam/gui/icons_04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCake.setIcon(icon5)
        self.actionCake.setObjectName("actionCake")
        self.actionRemove_Cosmics = QtGui.QAction(self)
        self.actionRemove_Cosmics.setToolTip('Remove cosmics')
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("xicam/gui/icons_06.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionRemove_Cosmics.setIcon(icon6)
        self.actionRemove_Cosmics.setText("")
        self.actionRemove_Cosmics.setObjectName("actionRemove_Cosmics")
        self.actionMaskLoad = QtGui.QAction(self)
        self.actionMaskLoad.setToolTip('Load mask')
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("xicam/gui/icons_08.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionMaskLoad.setIcon(icon7)
        self.actionMaskLoad.setText("")
        self.actionMaskLoad.setObjectName("actionMaskLoad")
        self.actionRadial_Symmetry = QtGui.QAction(self)
        self.actionRadial_Symmetry.setToolTip('Radial symmetry mask-filling')
        self.actionRadial_Symmetry.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("xicam/gui/icons_18.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRadial_Symmetry.setIcon(icon15)
        self.actionRadial_Symmetry.setObjectName("actionRadial_Symmetry")
        self.actionMirror_Symmetry = QtGui.QAction(self)
        self.actionMirror_Symmetry.setToolTip('Mirror symmetry mask-filling')
        self.actionMirror_Symmetry.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("xicam/gui/icons_17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMirror_Symmetry.setIcon(icon16)
        self.actionMirror_Symmetry.setObjectName("actionMirror_Symmetry")
        self.actionShow_Mask = QtGui.QAction(self)
        self.actionShow_Mask.setToolTip('Show mask')
        self.actionShow_Mask.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("xicam/gui/icons_20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17.addPixmap(QtGui.QPixmap("xicam/gui/icons_19.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionShow_Mask.setIcon(icon17)
        self.actionShow_Mask.setObjectName("actionShow_Mask")
        self.actionPolygon_Cut = QtGui.QAction(self)
        self.actionPolygon_Cut.setToolTip('Polygon region-of-interest')
        self.actionPolygon_Cut.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("xicam/gui/icons_21.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPolygon_Cut.setIcon(icon18)
        self.actionPolygon_Cut.setObjectName("actionPolygon_Cut")
        self.actionVertical_Cut = QtGui.QAction(self)
        self.actionVertical_Cut.setToolTip('Vertical region-of-interest')
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("xicam/gui/icons_22.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVertical_Cut.setIcon(icon19)
        self.actionVertical_Cut.setObjectName("actionVertical_Cut")
        self.actionHorizontal_Cut = QtGui.QAction(self)
        self.actionHorizontal_Cut.setToolTip('Horizontal region-of-interest')
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("xicam/gui/icons_23.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHorizontal_Cut.setIcon(icon20)
        self.actionHorizontal_Cut.setObjectName("actionHorizontal_Cut")
        self.actionLine_Cut = QtGui.QAction(self)
        self.actionLine_Cut.setToolTip('Line region-of-interest')
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("xicam/gui/icons_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLine_Cut.setIcon(icon21)
        self.actionLine_Cut.setObjectName("actionLine_Cut")
        self.actionRemeshing = QtGui.QAction(self)
        self.actionRemeshing.setToolTip('GIXS Ewald-sphere correction')
        self.actionRemeshing.setCheckable(True)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("xicam/gui/icons_25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemeshing.setIcon(icon23)
        self.actionRemeshing.setObjectName("actionRemeshing")
        self.actionRefine_Center = QtGui.QAction(self)
        self.actionRefine_Center.setToolTip('Refine calibration')
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("xicam/gui/icons_28.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefine_Center.setIcon(icon24)
        self.actionRefine_Center.setObjectName("actionRefine_Center")
        self.actionCalibrate_AgB = QtGui.QAction(self)
        self.actionCalibrate_AgB.setToolTip('Auto-calibrate AgB')
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("xicam/gui/icons_29.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCalibrate_AgB.setIcon(icon25)
        self.actionCalibrate_AgB.setObjectName("actionCalibrate_AgB")
        self.actionArc = QtGui.QAction(self)
        self.actionArc.setToolTip('Arc region-of-interest')
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("xicam/gui/icons_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionArc.setIcon(icon26)
        self.actionArc.setObjectName("actionArc")

        self.actionProcess = QtGui.QAction(self)
        self.actionProcess.setToolTip('Process')
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("xicam/gui/icons_34.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon27.addPixmap(QtGui.QPixmap("xicam/gui/icons_33.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionProcess.setIcon(icon27)
        self.actionProcess.setObjectName("actionProcess")
        self.actionProcess.setCheckable(True)
        self.actionProcess.setVisible(False)

        self.actionVideo = QtGui.QAction(self)
        self.actionVideo.setToolTip('Export Video')
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("xicam/gui/icons_31.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVideo.setIcon(icon28)
        self.actionVideo.setObjectName("actionVideo")
        self.actionVideo.setVisible(False)

        # self.actionSpaceGroup = QtGui.QAction(self)
        # icon29 = QtGui.QIcon()
        # icon29.addPixmap(QtGui.QPixmap("xicam/gui/icons_35.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.actionSpaceGroup.setIcon(icon29)
        # self.actionSpaceGroup.setObjectName("actionSpaceGroup")
        # self.actionSpaceGroup.setCheckable(True)
        # self.actionSpaceGroup.setVisible(False)

        self.actionCapture = QtGui.QAction(self)
        self.actionCapture.setToolTip('Capture region-of-interest')
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("xicam/gui/icons_36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCapture.setIcon(icon30)
        self.actionCapture.setObjectName("actionCapture")

        # self.actionROI = QtGui.QAction(self)
        #icon25 = QtGui.QIcon()
        #icon25.addPixmap(QtGui.QPixmap("xicam/gui/icons_29.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.actionROI.setIcon(icon25)
        #self.actionROI.setObjectName("actionROI")

        menu = QtGui.QMenu()
        # menu.addAction(self.actionShow_Mask)
        menu.addAction(self.actionPolyMask)
        menu.addAction(self.actionRemove_Cosmics)
        menu.addAction(self.actionMaskLoad)
        toolbuttonMasking = QtGui.QToolButton()
        toolbuttonMasking.setDefaultAction(self.actionMasking)
        toolbuttonMasking.setMenu(menu)
        toolbuttonMasking.setPopupMode(QtGui.QToolButton.InstantPopup)
        toolbuttonMaskingAction = QtGui.QWidgetAction(self)
        toolbuttonMaskingAction.setDefaultWidget(toolbuttonMasking)

        self.setIconSize(QtCore.QSize(32, 32))

        self.addAction(self.actionProcess)
        self.addAction(self.actionVideo)
        self.addAction(self.actionCalibrate_AgB)
        # self.addAction(self.actionCenterFind)        # Hide old buttons
        #self.addAction(self.actionRefine_Center)
        self.addAction(self.actionShow_Mask)
        self.addAction(toolbuttonMaskingAction)
        self.addAction(self.actionCake)
        self.addAction(self.actionRemeshing)
        self.addAction(self.actionArc)
        self.addAction(self.actionLine_Cut)
        self.addAction(self.actionVertical_Cut)
        self.addAction(self.actionHorizontal_Cut)
        self.addAction(self.actionLog_Intensity)
        self.addAction(self.actionRadial_Symmetry)
        self.addAction(self.actionMirror_Symmetry)
        # self.addAction(self.actionSpaceGroup)
        self.addAction(self.actionCapture)


    def connecttriggers(self, calibrate, centerfind, refine, showmask, cake, remesh, linecut, vertcut, horzcut, logint,
                        radialsym, mirrorsym, roi, arc, polymask, process=None, video=None,
                        capture=None,removecosmics=None):
        self.actionCalibrate_AgB.triggered.connect(calibrate)
        self.actionCenterFind.triggered.connect(centerfind)
        self.actionRefine_Center.triggered.connect(refine)
        self.actionShow_Mask.triggered.connect(showmask)
        self.actionCake.triggered.connect(self.caketoggle)  #####################3
        self.actionRemeshing.triggered.connect(self.remeshtoggle)  ##############
        self.actionLine_Cut.triggered.connect(linecut)
        self.actionVertical_Cut.triggered.connect(vertcut)
        self.actionHorizontal_Cut.triggered.connect(horzcut)
        self.actionPolyMask.triggered.connect(polymask)
        self.actionLog_Intensity.triggered.connect(logint)
        self.actionRadial_Symmetry.triggered.connect(radialsym)
        self.actionMirror_Symmetry.triggered.connect(mirrorsym)
        #self.actionROI.triggered.connect(roi)
        self.actionArc.triggered.connect(arc)

        self.sigCake.connect(cake)
        self.sigRemesh.connect(remesh)

        if process is not None:
            self.actionProcess.setVisible(True)
            self.actionProcess.triggered.connect(process)

        if video is not None:
            self.actionVideo.setVisible(True)
            self.actionVideo.triggered.connect(video)

        # if spacegroup is not None:
        #     self.actionSpaceGroup.setVisible(True)
        #     self.actionSpaceGroup.triggered.connect(spacegroup)

        if capture is not None:
            self.actionCapture.setVisible(True)
            self.actionCapture.triggered.connect(capture)

        if removecosmics is not None:
            self.actionRemove_Cosmics.setVisible(True)
            self.actionRemove_Cosmics.triggered.connect(removecosmics)

    def caketoggle(self):
        if self.actionCake.isChecked():
            self.actionRemeshing.setChecked(False)
        self.sigCake.emit()

    def remeshtoggle(self):
        if self.actionRemeshing.isChecked():
            self.actionCake.setChecked(False)
        self.sigRemesh.emit()




