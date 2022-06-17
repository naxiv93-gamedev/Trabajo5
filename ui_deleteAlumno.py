# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteAlumno.ui'
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

class Ui_DeleteAlumno(object):
    def setupUi(self, DeleteAlumno):
        if not DeleteAlumno.objectName():
            DeleteAlumno.setObjectName(u"DeleteAlumno")
        DeleteAlumno.resize(228, 146)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteAlumno.sizePolicy().hasHeightForWidth())
        DeleteAlumno.setSizePolicy(sizePolicy)
        DeleteAlumno.setBaseSize(QSize(258, 125))
        DeleteAlumno.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(DeleteAlumno)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DeleteAlumno)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.selectorAlumno = QComboBox(DeleteAlumno)
        self.selectorAlumno.setObjectName(u"selectorAlumno")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.selectorAlumno)

        self.label_2 = QLabel(DeleteAlumno)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.labelNombre = QLabel(DeleteAlumno)
        self.labelNombre.setObjectName(u"labelNombre")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelNombre)

        self.label_4 = QLabel(DeleteAlumno)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.labelEv1 = QLabel(DeleteAlumno)
        self.labelEv1.setObjectName(u"labelEv1")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelEv1)

        self.label_6 = QLabel(DeleteAlumno)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.labelEv2 = QLabel(DeleteAlumno)
        self.labelEv2.setObjectName(u"labelEv2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.labelEv2)

        self.label_8 = QLabel(DeleteAlumno)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.labelEv3 = QLabel(DeleteAlumno)
        self.labelEv3.setObjectName(u"labelEv3")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.labelEv3)

        self.label_10 = QLabel(DeleteAlumno)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.labelMedia = QLabel(DeleteAlumno)
        self.labelMedia.setObjectName(u"labelMedia")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.labelMedia)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.botonConfirmar = QPushButton(DeleteAlumno)
        self.botonConfirmar.setObjectName(u"botonConfirmar")

        self.horizontalLayout.addWidget(self.botonConfirmar)
        
        self.botonCancelar = QPushButton(DeleteAlumno)
        self.botonCancelar.setObjectName(u"botonCancelar")

        self.horizontalLayout.addWidget(self.botonCancelar)

        


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DeleteAlumno)

        QMetaObject.connectSlotsByName(DeleteAlumno)
    # setupUi

    def retranslateUi(self, DeleteAlumno):
        DeleteAlumno.setWindowTitle(QCoreApplication.translate("DeleteAlumno", u"C.A.D.I- Eliminar Alumno", None))
        self.label.setText(QCoreApplication.translate("DeleteAlumno", u"Seleccione Alumno", None))
        self.label_2.setText(QCoreApplication.translate("DeleteAlumno", u"Nombre Alumno", None))
        self.labelNombre.setText("")
        self.label_4.setText(QCoreApplication.translate("DeleteAlumno", u"Nota 1\u00aa Evaluacion", None))
        self.labelEv1.setText("")
        self.label_6.setText(QCoreApplication.translate("DeleteAlumno", u"Nota 2\u00aa Evaluacion", None))
        self.labelEv2.setText("")
        self.label_8.setText(QCoreApplication.translate("DeleteAlumno", u"Nota 3\u00aa Evaluacion", None))
        self.labelEv3.setText("")
        self.label_10.setText(QCoreApplication.translate("DeleteAlumno", u"Nota media", None))
        self.labelMedia.setText("")
        self.botonCancelar.setText(QCoreApplication.translate("DeleteAlumno", u"Cancelar", None))
        self.botonConfirmar.setText(QCoreApplication.translate("DeleteAlumno", u"Confirmar", None))
    # retranslateUi

