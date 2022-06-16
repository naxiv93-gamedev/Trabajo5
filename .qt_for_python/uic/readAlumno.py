# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'readAlumno.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ShowAlumno(object):
    def setupUi(self, ShowAlumno):
        if not ShowAlumno.objectName():
            ShowAlumno.setObjectName(u"ShowAlumno")
        ShowAlumno.resize(258, 126)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShowAlumno.sizePolicy().hasHeightForWidth())
        ShowAlumno.setSizePolicy(sizePolicy)
        ShowAlumno.setBaseSize(QSize(258, 125))
        ShowAlumno.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(ShowAlumno)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(ShowAlumno)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.selectorAlumno = QComboBox(ShowAlumno)
        self.selectorAlumno.setObjectName(u"selectorAlumno")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.selectorAlumno)

        self.label_2 = QLabel(ShowAlumno)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.labelNombre = QLabel(ShowAlumno)
        self.labelNombre.setObjectName(u"labelNombre")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelNombre)

        self.label_4 = QLabel(ShowAlumno)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.labelEv1 = QLabel(ShowAlumno)
        self.labelEv1.setObjectName(u"labelEv1")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelEv1)

        self.label_6 = QLabel(ShowAlumno)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.labelEv2 = QLabel(ShowAlumno)
        self.labelEv2.setObjectName(u"labelEv2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.labelEv2)

        self.label_8 = QLabel(ShowAlumno)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.labelEv3 = QLabel(ShowAlumno)
        self.labelEv3.setObjectName(u"labelEv3")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.labelEv3)

        self.label_10 = QLabel(ShowAlumno)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.labelMedia = QLabel(ShowAlumno)
        self.labelMedia.setObjectName(u"labelMedia")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.labelMedia)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botonConfirmar = QPushButton(ShowAlumno)
        self.botonConfirmar.setObjectName(u"botonConfirmar")

        self.horizontalLayout.addWidget(self.botonConfirmar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ShowAlumno)

        QMetaObject.connectSlotsByName(ShowAlumno)
    # setupUi

    def retranslateUi(self, ShowAlumno):
        ShowAlumno.setWindowTitle(QCoreApplication.translate("ShowAlumno", u"C.A.D.I- Mostrar Alumno", None))
        self.label.setText(QCoreApplication.translate("ShowAlumno", u"Seleccione Alumno", None))
        self.label_2.setText(QCoreApplication.translate("ShowAlumno", u"Nombre Alumno", None))
        self.labelNombre.setText("")
        self.label_4.setText(QCoreApplication.translate("ShowAlumno", u"Nota 1\u00aa Evaluacion", None))
        self.labelEv1.setText("")
        self.label_6.setText(QCoreApplication.translate("ShowAlumno", u"Nota 2\u00aa Evaluacion", None))
        self.labelEv2.setText("")
        self.label_8.setText(QCoreApplication.translate("ShowAlumno", u"Nota 3\u00aa Evaluacion", None))
        self.labelEv3.setText("")
        self.label_10.setText(QCoreApplication.translate("ShowAlumno", u"Nota media", None))
        self.labelMedia.setText("")
        self.botonConfirmar.setText(QCoreApplication.translate("ShowAlumno", u"Confirmar", None))
    # retranslateUi

