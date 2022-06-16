# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(345, 185)
        self.actionA_adir_nuevo_alumno = QAction(MainWindow)
        self.actionA_adir_nuevo_alumno.setObjectName(u"actionA_adir_nuevo_alumno")
        self.actionBorrar_alumno = QAction(MainWindow)
        self.actionBorrar_alumno.setObjectName(u"actionBorrar_alumno")
        self.actionModificar_alumno = QAction(MainWindow)
        self.actionModificar_alumno.setObjectName(u"actionModificar_alumno")
        self.actionMostrar_alumno = QAction(MainWindow)
        self.actionMostrar_alumno.setObjectName(u"actionMostrar_alumno")
        self.actionGenerar_Informe_Alumno = QAction(MainWindow)
        self.actionGenerar_Informe_Alumno.setObjectName(u"actionGenerar_Informe_Alumno")
        self.actionGenerar_Informe_Clase = QAction(MainWindow)
        self.actionGenerar_Informe_Clase.setObjectName(u"actionGenerar_Informe_Clase")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.botonEliminarAlumno = QPushButton(self.centralwidget)
        self.botonEliminarAlumno.setObjectName(u"botonEliminarAlumno")

        self.gridLayout.addWidget(self.botonEliminarAlumno, 1, 1, 1, 1)

        self.botonCrearAlumno = QPushButton(self.centralwidget)
        self.botonCrearAlumno.setObjectName(u"botonCrearAlumno")

        self.gridLayout.addWidget(self.botonCrearAlumno, 0, 0, 1, 1)

        self.botonModificarAlumno = QPushButton(self.centralwidget)
        self.botonModificarAlumno.setObjectName(u"botonModificarAlumno")

        self.gridLayout.addWidget(self.botonModificarAlumno, 0, 1, 1, 1)

        self.botonLeerAlumno = QPushButton(self.centralwidget)
        self.botonLeerAlumno.setObjectName(u"botonLeerAlumno")

        self.gridLayout.addWidget(self.botonLeerAlumno, 1, 0, 1, 1)

        self.botonGenerarInformeAlumno = QPushButton(self.centralwidget)
        self.botonGenerarInformeAlumno.setObjectName(u"botonGenerarInformeAlumno")
        self.botonGenerarInformeClase = QPushButton(self.centralwidget)
        self.botonGenerarInformeAlumno.setObjectName(u"botonGenerarInformeClase")

        self.gridLayout.addWidget(self.botonGenerarInformeAlumno, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.botonGenerarInformeClase, 1, 2, 1, 1)



        self.verticalLayout.addLayout(self.gridLayout)

        self.botonCerrar = QPushButton(self.centralwidget)
        self.botonCerrar.setObjectName(u"botonCerrar")

        self.verticalLayout.addWidget(self.botonCerrar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 345, 18))
        self.menuAcciones = QMenu(self.menubar)
        self.menuAcciones.setObjectName(u"menuAcciones")
        self.menuInformes = QMenu(self.menubar)
        self.menuInformes.setObjectName(u"menuInformes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAcciones.menuAction())
        self.menubar.addAction(self.menuInformes.menuAction())
        self.menuAcciones.addAction(self.actionA_adir_nuevo_alumno)
        self.menuAcciones.addAction(self.actionBorrar_alumno)
        self.menuAcciones.addAction(self.actionModificar_alumno)
        self.menuAcciones.addAction(self.actionMostrar_alumno)
        self.menuInformes.addAction(self.actionGenerar_Informe_Alumno)
        self.menuInformes.addAction(self.actionGenerar_Informe_Clase)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionA_adir_nuevo_alumno.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir nuevo alumno", None))
        self.actionBorrar_alumno.setText(QCoreApplication.translate("MainWindow", u"Borrar alumno", None))
        self.actionModificar_alumno.setText(QCoreApplication.translate("MainWindow", u"Modificar alumno", None))
        self.actionMostrar_alumno.setText(QCoreApplication.translate("MainWindow", u"Mostrar alumno", None))
        self.actionGenerar_Informe_Alumno.setText(QCoreApplication.translate("MainWindow", u"Generar Informe Alumno", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenido al Custodio de Alumnos de Desarrollo de Interfaces (C.A.D.I)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Acciones disponibles", None))
        self.botonEliminarAlumno.setText(QCoreApplication.translate("MainWindow", u"Eliminar Alumno", None))
        self.botonCrearAlumno.setText(QCoreApplication.translate("MainWindow", u"Crear Alumno", None))
        self.botonModificarAlumno.setText(QCoreApplication.translate("MainWindow", u"Modificar Alumno", None))
        self.botonLeerAlumno.setText(QCoreApplication.translate("MainWindow", u"Leer Alumno", None))
        self.botonGenerarInformeAlumno.setText(QCoreApplication.translate("MainWindow", u"Generar Informe de Alumno", None))
        self.botonGenerarInformeClase.setText(QCoreApplication.translate("MainWindow", u"Generar Informe de Clase", None))
        self.botonCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.menuAcciones.setTitle(QCoreApplication.translate("MainWindow", u"Alumnos", None))
        self.menuInformes.setTitle(QCoreApplication.translate("MainWindow", u"Informes", None))
    # retranslateUi

