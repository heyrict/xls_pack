import sys, os
#os.system("pyuic5 xls_pack.ui -o ui_resource.py")
from ui_resource import Ui_Dialog
from xls_pack import *

import PyQt5
import pandas as pd
from PyQt5 import QtGui, QtCore, QtWidgets


class maindialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(maindialog,self).__init__(parent)
        
        self.output="-"*50+"\n\n"+"A program designed to find duplicated data and merge data in\n"
        self.output += "several excel files.\n\n"+"More details in Github: http://github.com/heyrict/xls_pack\n"
        self.output += "\n"+"-"*50 + "\n\n\n"
        self.major = Ui_Dialog()
        self.major.setupUi(self)
        self.major.plainTextEdit.setPlainText(self.output)
        self.scolbar = self.major.plainTextEdit.verticalScrollBar()

        self.major.lineEdit_k.setText("学号 姓名")
        self.major.lineEdit_tk.setText("int str")
        self.major.lineEdit_uk.setText("")
        self.major.lineEdit_out.setText("output.xls")
        self.major.checkBox_match.setChecked(True)
        
        if not os.path.exists("input\\"):
            os.mkdir("input\\")
            open("input\\PLACE INPUT FILES HERE","w").close()
        if not os.path.exists("meta_data\\"):
            os.mkdir("meta_data\\")
        if not os.path.exists("meta_data\\meta.xlsx"):
            open("meta_data\\meta.xlsx","w").close()
        elif os.path.getsize("meta_data\\meta.xlsx") == 0:
                print("WARNING: METADATA IS EMPTY!")

        self.fetchfiles()
        
        self.major.buttonmerge.clicked.connect(self.clicked)
        self.major.buttondup.clicked.connect(self.clicked)

    def dupcheck(self):
        k = find_duplicated(self.l,key=self.key,keyformat=self.keyformat,
                            subkey=self.subkey)
        if type(k)==pd.DataFrame:
            if len(k)!=0:
                self.printtoobj("There are some duplicated data below:")
                self.printtoobj(k,hint="",end="\n\n")
            else:
                self.printtoobj("No duplicated data found.")
        else:
            self.printtoobj("WARNING: CANNOT MATCH EXCEL FILES WITH METADATA")
        self.printtoobj("",hint="")

    def clicked(self):
        if len(self.l)==0 :
            self.fetchfiles()
            if len(self.l)==0:
                self.printtoobj("ERROR: NO EXCEL FILES FOUND IN \"input\\\"")
                return
        if not os.path.exists("meta_data\\meta.xlsx"):
            self.printtoobj("WARNING: FILE\"meta_data\\meta.xlsx\" NOT FOUND")
        if os.path.getsize("meta_data\\meta.xlsx") == 0:
            self.printtoobj("WARNING: META DATA IS EMPTY")

        self.key = self.major.lineEdit_k.text().split()
        self.keyformat = self.major.lineEdit_tk.text().split()
        self.subkey = self.major.lineEdit_uk.text().split()
        self.out = self.major.lineEdit_out.text()
        self.match = self.major.checkBox_match.isChecked()

        sender = self.sender()
        if sender.objectName() == "buttonmerge":
            self.printtoobj("Now merging files with keys of %s"%(", ".join(self.key)))
            self.printtoobj("please wait ...")
            total_process(self.l,key=self.key,keyformat=self.keyformat,
                          subkey=self.subkey,output=self.out,match=self.match)
            self.printtoobj("Success!")
            self.printtoobj("",hint="")
        elif sender.objectName() == "buttondup":
            self.dupcheck()

    def printtoobj(self,*text,sep=" ",end="\n",hint=">>>"):
        self.output += hint
        for t in text:
            self.output += str(t) + sep
        self.output += end
        self.major.plainTextEdit.setPlainText(self.output)
        self.scolbar.setValue(self.scolbar.maximumHeight())

    def fetchfiles(self,folder="\\input"):
        self.printtoobj("Now fetching excel files in the directory \"%s\""%folder)
        self.l = pd.Series(os.listdir(os.getcwd()+folder))
        if len(self.l)==0 :
            self.printtoobj("ERROR: NO EXCEL FILES FOUND IN \"input\\\"")
            return

        self.l = self.l[self.l.apply(lambda x: True if (str(x)[-4:]=='.xls' or str(x)[-4:]=='xlsx')
                      else False)]
        self.printtoobj("The files to be merged are below:")
        inputlist = list(self.l)
        for i in range(len(inputlist)):
            self.printtoobj(i+1," ",inputlist[i],hint="")
        self.printtoobj("",hint="")


if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    dlg = maindialog()
    dlg.show()
    app.exec_()