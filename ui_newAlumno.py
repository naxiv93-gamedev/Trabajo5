# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newAlumno.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_NewAlumno(object):
    def setupUi(self, NewAlumno):
        if not NewAlumno.objectName():
            NewAlumno.setObjectName(u"NewAlumno")
        NewAlumno.resize(258, 125)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewAlumno.sizePolicy().hasHeightForWidth())
        NewAlumno.setSizePolicy(sizePolicy)
        NewAlumno.setBaseSize(QSize(258, 125))
        NewAlumno.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(NewAlumno)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(NewAlumno)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombreAlumno = QLineEdit(NewAlumno)
        self.nombreAlumno.setObjectName(u"nombreAlumno")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombreAlumno)

        self.label_2 = QLabel(NewAlumno)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.notaEv1 = QDoubleSpinBox(NewAlumno)
        self.notaEv1.setObjectName(u"notaEv1")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.notaEv1)

        self.label_3 = QLabel(NewAlumno)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.notaEv2 = QDoubleSpinBox(NewAlumno)
        self.notaEv2.setObjectName(u"notaEv2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.notaEv2)

        self.label_4 = QLabel(NewAlumno)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.notaEv3 = QDoubleSpinBox(NewAlumno)
        self.notaEv3.setObjectName(u"notaEv3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.notaEv3)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botonConfirmar = QPushButton(NewAlumno)
        self.botonConfirmar.setObjectName(u"botonConfirmar")

        self.horizontalLayout.addWidget(self.botonConfirmar)

        self.botonCancelar = QPushButton(NewAlumno)
        self.botonCancelar.setObjectName(u"botonCancelar")

        self.horizontalLayout.addWidget(self.botonCancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(NewAlumno)

        QMetaObject.connectSlotsByName(NewAlumno)
    # setupUi

    def retranslateUi(self, NewAlumno):
        NewAlumno.setWindowTitle(QCoreApplication.translate("NewAlumno", u"C.A.D.I- Nuevo Alumno", None))
        self.label.setText(QCoreApplication.translate("NewAlumno", u"Nombre Alumno", None))
        self.label_2.setText(QCoreApplication.translate("NewAlumno", u"Nota 1\u00aa Evaluacion", None))
        self.label_3.setText(QCoreApplication.translate("NewAlumno", u"Nota 2\u00aa Evaluacion", None))
        self.label_4.setText(QCoreApplication.translate("NewAlumno", u"Nota 3\u00aa Evaluacion", None))
        self.botonConfirmar.setText(QCoreApplication.translate("NewAlumno", u"Confirmar", None))
        self.botonCancelar.setText(QCoreApplication.translate("NewAlumno", u"Cancelar", None))
    # retranslateUi

