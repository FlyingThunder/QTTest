from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog
import sys
import json
import os
from IPv4calc import IPv4Calc
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
    check = 0
    IPv4CalcInst = IPv4Calc()


    def __init__(self):
        super().__init__()
        self.initUI()
        self.getChoice()
        self.showDialog(string=self.counter)
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
        self.check = 0
        if CreateWindow.counter < 12:
            self.text, self.ok = QInputDialog.getText(self, 'Input Dialog', 'Enter ' + self.datalist[int(string)] + ':')
            if not self.ok:
                exit()
            if self.inputCheck(text=self.text) == True:
                CreateWindow.counter += 1
            else:
                QMessageBox.about(self, "Error", "Invalid Input!")
            self.okButtonClick()
        else:
            with open('test.json', 'a+') as outfile:
                json.dump(self.IPv4Header, outfile)
                outfile.close()
            self.IPv4CalcInst.CallPrompt()




    def inputCheck(self, text):
        if text is "":
            self.check = 1

        for listitem in text:
            if self.item == "decbin":
                if listitem not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:  #Quick&Dirty des Todes
                    self.check = 1
            elif self.item == "bindec":
                if listitem not in ["0","1","."]:
                    self.check = 1

        if self.check == 1:
            return False
        else:
            return True


    def okButtonClick(self):
        if self.ok:
            if self.check == 0:
                self.IPv4Header.append(self.text)
                print(self.IPv4Header)
                try:
                    with open('test.json', 'r') as infile:
                        if os.stat('test.json').st_size != 0:
                            data = json.load(infile)
                            self.IPv4Header = data
                        infile.close()
                except:
                    pass
            self.showDialog(CreateWindow.counter)

    def getTime(self):
        timenow = datetime.datetime.now()
        splittime = str(timenow).replace(":", "_").replace("-", "").replace(".", "").replace(" ", "_")
        self.filetime = splittime.replace(' ', '')[:-6]
        return self.filetime

    def finalResult(self):
        print("Data by type:",self.LogicData)
        print("Plain data:", "-".join(self.LogicData.values()))
        print("Saving results to file")
        filename = 'results'+self.getTime()+'.txt'
        with open(filename, 'w') as output:
            output.write("Your input:"+str(self.IPv4Header))
            for x in range(12):
                output.write("\n"+list(self.LogicData.keys())[x]+":"+list(self.LogicData.values())[x])
        os.remove('test.json')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreateWindow()
    sys.exit(app.exec_())