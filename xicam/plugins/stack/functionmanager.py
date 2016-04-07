from PySide.QtUiTools import QUiLoader
from PySide import QtGui
from PySide import QtCore

import customwidgets


features = []
layout = None


def clearFeatures():
    global features
    value = QtGui.QMessageBox.question(None, 'Delete all functions?',
                                       'Are you sure you want to clear ALL functions?',
                                       (QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel))

    if value is QtGui.QMessageBox.Yes:
        for feature in features:
            feature.deleteLater()
            del feature
        features = []

def addFunction(function,subfunction):
    global features
    features.append(customwidgets.func(function,subfunction))
    update()


def addSubstrate():
    global features
    if not sum([type(feature) is customwidgets.substrate for feature in features]):
        features.insert(0, customwidgets.substrate())
    update()


def addLayer():
    global features
    features.append(customwidgets.layer())
    print features
    update()


def addParticle():
    global features
    features.append(customwidgets.particle())
    update()


def removeFeature(index):
    global features
    del features[index]
    update()


def layercount():
    return sum([type(feature) is customwidgets.layer for feature in features])


def particlecount():
    return sum([type(feature) is customwidgets.particle for feature in features])


def update():
    global layout
    assert isinstance(layout, QtGui.QVBoxLayout)

    for i in range(layout.count()):
        layout.itemAt(i).parent = None

    # layout.addItem(QtGui.QSpacerItem(0,0,vData=QtGui.QSizePolicy.Expanding))

    for item in features[::-1]:
        layout.addWidget(item)


def loadform(path):
    guiloader = QUiLoader()
    f = QtCore.QFile(path)
    f.open(QtCore.QFile.ReadOnly)
    form = guiloader.load(f)
    f.close()
    return form


def load():
    global features, layout
    layout.setAlignment(QtCore.Qt.AlignBottom)
    # addSubstrate()
    # addLayer()
    # addLayer()
    # addParticle()
