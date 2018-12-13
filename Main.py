from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog
import sys
import json
import os
from calculating import IPv4Calc
from chksum import chksum
from StringCheck import StringCheck
from calculate_IHL import getFields
import string
import datetime


class CreateWindow(QWidget):
    try:
        os.remove("test.json")
    except:
        pass
    IPv4Header = []
    LogicData = IPv4Calc().IPv4Header
    datalist = IPv4Calc().datalist
    counter = 0
    alphabet = string.ascii_letters
    IPv4CalcInst = IPv4Calc()
    chksumInst = chksum()
    strchkInst = StringCheck()
    IHLget = calculate_IHL()


    def __init__(self):
        super().__init__()
        self.initUI()
        self.getChoice()
        self.showDialog(string=self.counter)
        self.get_IHL()
        self.finalResult()

    def initUI(self):
        pass

    def getChoice(self):
        items = ("bindec","decbin")
        self.item, okPressed = QInputDialog.getItem(self, "Get item", "Mode:", items, 0 , False)
        if not okPressed:
            exit()
        if okPressed and self.item:
            self.IPv4CalcInst.calctype = self.item

    def showDialog(self, string):
        if CreateWindow.counter < len(self.datalist):
            self.text, self.ok = QInputDialog.getText(self, 'Input Dialog', 'Enter ' + self.datalist[int(string)] + ':')
            if not self.ok:
                exit()
            if self.strchkInst.inputCheck(text=self.text, type=self.datalist[int(string)], item = self.item) == True:
                CreateWindow.counter += 1
            else:
                QMessageBox.about(self, "Error", "Invalid Input!")
            self.okButtonClick()
        else:
            with open('test.json', 'a+') as outfile:
                json.dump(self.IPv4Header, outfile)
                outfile.close()
            self.IPv4CalcInst.CallPrompt()

    def okButtonClick(self):
        if self.ok:
            if self.strchkInst.check == 0:
                self.IPv4Header.append(self.text)
                try:
                    with open('test.json', 'r') as infile:
                        if os.stat('test.json').st_size != 0:
                            data = json.load(infile)
                            self.IPv4Header = data
                        infile.close()
                except:
                    pass
            self.showDialog(CreateWindow.counter)

    def get_IHL(self):
        self.get_IHL().getFields(self.IPv4Header)


    def getTime(self):
        timenow = datetime.datetime.now()
        splittime = str(timenow).replace(":", "_").replace("-", "").replace(".", "").replace(" ", "_")
        self.filetime = splittime.replace(' ', '')[:-6]
        return self.filetime

    def finalResult(self):
        QMessageBox.about(self, "Saving...", "Saving data to file in Script folder")

        self.chksumInst.outChecksum(mode = self.item, inputdata = self.IPv4Header, outputdata = self.LogicData.values())
        self.inputchecksum = self.chksumInst.inputchecksum
        self.outputchecksum = self.chksumInst.outputchecksum

        filename = 'results'+self.getTime()+'.txt'
        with open(filename, 'w') as output:
            output.write("Your input:"+str(self.IPv4Header))
            for x in range(len(self.datalist)):
                output.write("\n"+list(self.LogicData.keys())[x]+":"+list(self.LogicData.values())[x])
            output.write("\nChecksum of the input:"+str(self.inputchecksum))
            output.write("\nChecksum of the output:"+str(self.outputchecksum))
            output.close()

        os.remove('test.json')
        exit()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreateWindow()
    sys.exit(app.exec_())