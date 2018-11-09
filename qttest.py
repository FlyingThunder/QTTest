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
        if CreateWindow.counter < len(self.datalist):
            self.text, self.ok = QInputDialog.getText(self, 'Input Dialog', 'Enter ' + self.datalist[int(string)] + ':')
            if not self.ok:
                exit()
            if self.inputCheck(text=self.text, type=self.datalist[int(string)]) == True:
                CreateWindow.counter += 1
            else:
                QMessageBox.about(self, "Error", "Invalid Input!")
            self.okButtonClick()
        else:
            with open('test.json', 'a+') as outfile:
                json.dump(self.IPv4Header, outfile)
                outfile.close()
            self.IPv4CalcInst.CallPrompt()


    def ipChecker(self, ip):
        iplist = ip.split(".")
        for part in iplist:
            if part != ".":
                if self.item == "decbin":
                    if int(part) > 255:
                        return False
                elif self.item == "bindec":
                    if int(part) > 11111111:
                        return False

    def inputCheck(self, text, type):
        if type in ["Source","Destination"]:
            if text.count(".") == 3:
                if self.ipChecker(text) == False:
                    self.check = 1
            else:
                self.check = 1
        if text is "":
            self.check = 1

        for listitem in text:
            if self.item == "decbin":
                if listitem not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
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

    def calcChecksum(self): #IPv4Header = InputList, LogicData = OutputDict
        self.templistin = []
        self.templistout = []

        if self.item == "bindec":
            for item in self.IPv4Header:            #jedes header feld des inputs:
                if "." in item:                     #wenn IP addresse:
                    x = []
                    x.append(item.split("."))
                    for ipitem in x[0]:
                        self.templistin.append(int(str(ipitem), 2)) #jedes oktet als dezimalwert in die liste einfügen
                else:
                    self.templistin.append(int(str(item), 2)) #jedes andere feld als dezimalwert in liste einfügen

            for item in self.LogicData.values():    #jedes header feld des outputs:
                if "." in item:                     #wenn IP addresse:
                    y = []
                    y.append(item.split("."))
                    for ipitem in y[0]:
                        self.templistout.append(int(ipitem))    #jedes oktet als listenitem in temporäre liste einfügen:
                else:
                    self.templistout.append(int(item))               #jedes andere feld in liste einfügen

            self.inputchecksum = sum(self.templistin) #liste summieren
            self.outputchecksum = sum(self.templistout) #liste summieren

    def finalResult(self):
        QMessageBox.about(self, "Saving...", "Saving data to file in Script folder")

        self.calcChecksum()

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