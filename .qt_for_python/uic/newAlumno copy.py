# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newAlumno copy.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(258, 125)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(258, 125))
        Form.setMaximumSize(QSize(258, 125))
        Form.setBaseSize(QSize(258, 125))
        Form.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.doubleSpinBox = QDoubleSpinBox(Form)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.doubleSpinBox_3 = QDoubleSpinBox(Form)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.doubleSpinBox_2 = QDoubleSpinBox(Form)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre Alumno", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nota 1\u00aa Evaluacion", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nota 2\u00aa Evaluacion", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nota 3\u00aa Evaluacion", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Confirmar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

