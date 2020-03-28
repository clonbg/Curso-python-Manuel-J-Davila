# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_boton = QtWidgets.QPushButton(self.centralwidget)
        self.button_boton.setGeometry(QtCore.QRect(200, 70, 86, 27))
        self.button_boton.setObjectName("button_boton")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(70, 70, 64, 19))
        self.label_titulo.setText("Título")
        self.label_titulo.setObjectName("label_titulo")
        self.Text_area = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Text_area.setGeometry(QtCore.QRect(60, 170, 241, 181))
        self.Text_area.setObjectName("Text_area")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 24))
        self.menubar.setObjectName("menubar")
        self.menuPesta_a1 = QtWidgets.QMenu(self.menubar)
        self.menuPesta_a1.setObjectName("menuPesta_a1")
        self.menuPesta_a2 = QtWidgets.QMenu(self.menubar)
        self.menuPesta_a2.setObjectName("menuPesta_a2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPesta_a1.menuAction())
        self.menubar.addAction(self.menuPesta_a2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_boton.setText(_translate("MainWindow", "Botón"))
        self.menuPesta_a1.setTitle(_translate("MainWindow", "Pestaña1"))
        self.menuPesta_a2.setTitle(_translate("MainWindow", "Pestaña2"))

        # Mi código

    # Función que se llama al presionar
        def FuncionPresionar():
            if self.label_titulo.text() == 'Título':
                self.label_titulo.setText("Un clavito clavo Pablito")
                self.label_titulo.setGeometry(QtCore.QRect(5, 70, 200, 19))
            else:
                self.label_titulo.setGeometry(QtCore.QRect(70, 70, 64, 19))
                self.label_titulo.setText("Título")
        # Ver el texto del label en la caja de texto
            mostrar = self.label_titulo.text()
            self.Text_area.setPlainText(mostrar)

    # Acción al presionar el botón
        self.button_boton.clicked.connect(FuncionPresionar)


# Fin de mi código

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
