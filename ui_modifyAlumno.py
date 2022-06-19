# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyAlumno.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import pyqtgraph as pg


class Ui_ModifyAlumno(object):
    def setupUi(self, ModifyAlumno):
        if not ModifyAlumno.objectName():
            ModifyAlumno.setObjectName(u"ModifyAlumno")
        ModifyAlumno.resize(258, 125)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ModifyAlumno.sizePolicy().hasHeightForWidth())
        ModifyAlumno.setSizePolicy(sizePolicy)
        ModifyAlumno.setBaseSize(QSize(258, 125))
        ModifyAlumno.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(ModifyAlumno)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(ModifyAlumno)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.nombreAlumno = QLineEdit(ModifyAlumno)
        self.nombreAlumno.setObjectName(u"nombreAlumno")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nombreAlumno)

        self.label_2 = QLabel(ModifyAlumno)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.notaEv1 = QDoubleSpinBox(ModifyAlumno)
        self.notaEv1.setObjectName(u"notaEv1")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.notaEv1)

        self.label_3 = QLabel(ModifyAlumno)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.notaEv2 = QDoubleSpinBox(ModifyAlumno)
        self.notaEv2.setObjectName(u"notaEv2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.notaEv2)

        self.label_4 = QLabel(ModifyAlumno)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.notaEv3 = QDoubleSpinBox(ModifyAlumno)
        self.notaEv3.setObjectName(u"notaEv3")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.notaEv3)

        self.label_5 = QLabel(ModifyAlumno)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.selectorAlumno = QComboBox(ModifyAlumno)
        self.selectorAlumno.setObjectName(u"selectorAlumno")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.selectorAlumno)


        self.verticalLayout.addLayout(self.formLayout)
        
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setBackground('w') 
        self.verticalLayout.addWidget(self.graphWidget)
        
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botonConfirmar = QPushButton(ModifyAlumno)
        self.botonConfirmar.setObjectName(u"botonConfirmar")

        self.horizontalLayout.addWidget(self.botonConfirmar)

        self.botonCancelar = QPushButton(ModifyAlumno)
        self.botonCancelar.setObjectName(u"botonCancelar")

        self.horizontalLayout.addWidget(self.botonCancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ModifyAlumno)

        QMetaObject.connectSlotsByName(ModifyAlumno)
    # setupUi

    def retranslateUi(self, ModifyAlumno):
        ModifyAlumno.setWindowTitle(QCoreApplication.translate("ModifyAlumno", u"C.A.D.I- Modificar Alumno", None))
        self.label.setText(QCoreApplication.translate("ModifyAlumno", u"Nombre Alumno", None))
        self.label_2.setText(QCoreApplication.translate("ModifyAlumno", u"Nota 1\u00aa Evaluacion", None))
        self.label_3.setText(QCoreApplication.translate("ModifyAlumno", u"Nota 2\u00aa Evaluacion", None))
        self.label_4.setText(QCoreApplication.translate("ModifyAlumno", u"Nota 3\u00aa Evaluacion", None))
        self.label_5.setText(QCoreApplication.translate("ModifyAlumno", u"ID Alumno", None))
        self.botonConfirmar.setText(QCoreApplication.translate("ModifyAlumno", u"Confirmar", None))
        self.botonCancelar.setText(QCoreApplication.translate("ModifyAlumno", u"Cancelar", None))
    # retranslateUi

