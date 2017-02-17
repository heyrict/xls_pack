# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xls_pack.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(803, 324)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 751, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.lineEdit_k = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_k.setObjectName("lineEdit_k")
        self.verticalLayout.addWidget(self.lineEdit_k)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_tk = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_tk.setObjectName("lineEdit_tk")
        self.verticalLayout.addWidget(self.lineEdit_tk)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_uk = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_uk.setObjectName("lineEdit_uk")
        self.verticalLayout.addWidget(self.lineEdit_uk)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_out = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_out.setObjectName("lineEdit_out")
        self.verticalLayout.addWidget(self.lineEdit_out)
        self.checkBox_match = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_match.setObjectName("checkBox_match")
        self.verticalLayout.addWidget(self.checkBox_match)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttondup = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttondup.setObjectName("buttondup")
        self.horizontalLayout_2.addWidget(self.buttondup)
        self.buttonmerge = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonmerge.setObjectName("buttonmerge")
        self.horizontalLayout_2.addWidget(self.buttonmerge)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "xls_pack"))
        self.label_1.setText(_translate("Dialog", "Shared keys(seperate by a space)"))
        self.label.setText(_translate("Dialog", "types of the shared keys"))
        self.label_2.setText(_translate("Dialog", "Shared useless keys(seperate by a space)"))
        self.label_3.setText(_translate("Dialog", "output filename"))
        self.checkBox_match.setText(_translate("Dialog", "match keys with metadata"))
        self.buttondup.setText(_translate("Dialog", "排重"))
        self.buttonmerge.setText(_translate("Dialog", "整合"))

