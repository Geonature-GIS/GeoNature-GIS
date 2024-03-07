# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from qgis.core import *
from qgis.gui import *
import sys, os


from .additional_data_filter_widget import *



ui_path = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(ui_path, "ui")
form_refgeo, _ = uic.loadUiType(os.path.join(ui_path, "referentiel_geographique_dock.ui"))




class RefGeoWidget(QDockWidget, form_refgeo):
    fermeFenetreFonction = pyqtSignal(list)
    

    def __init__(self, interface):
        QWidget.__init__(self)
        self.setupUi(self)

    def initGui(self, dialog):
        maFenetre = dialog


        self.pbAddData = maFenetre.findChild(QPushButton, "pb_additionalFilter")
        self.pbAddData.clicked.connect(self.openAddDataFilter)

        self.addAction(self.pbAddData)



    def openAddDataFilter(self):
        # QMessageBox.information(self.interface.mainWindow(), u"Plugin Test1", u"Action 1 lancée")
        connexion = AddDataFilterWidget(self.interface)
        connexion.show()
        result = connexion.exec_()
        if result:
            pass

    def closeEvent(self, event):
        self.fermeFenetreFonction.emit(["refgeo"])
        event.accept()