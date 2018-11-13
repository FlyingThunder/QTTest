from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog
import sys
import json
import os
from calculating import IPv4Calc
from chksum import chksum
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
    chksumInst = chksum()


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
            if self.item == "decbin":
                if int(part) > 255:
                    return False
            elif self.item == "bindec":
                if int(part) > 11111111:
                    return False

    def textCheck(self, textlist):
        textlist2 = []
        for item in textlist:
            textlist2.append(bin(int(item)).lstrip("0b"))
        if self.item == "decbin":
            print(self.text)
            print(textlist)
            if int(self.text) not in textlist:
                self.check = 1
        elif self.item == "bindec":
            if (self.text) not in textlist2:
                self.check = 1

    def inputCheck(self, text, type):
        if type in ["Source","Destination"]:
            if text.count(".") == 3:
                if self.ipChecker(text) == False:
                    self.check = 1
            else:
                self.check = 1

        elif type == "Version":
            self.textCheck([4,6])

        elif type == "IHL":
            self.textCheck(list(range(1,5))) #fix?

        elif type == "TOS":
            self.textCheck(list(range(1,9)))

        elif type == "Length":
            self.textCheck(list(range(1,17)))

        elif type == "Identification":
            self.textCheck(list(range(1,17)))

        elif type == "Flag":
            self.textCheck(list(range(1,4)))

        elif type == "Offset":
            self.textCheck(list(range(1,14)))

        elif type == "TTL":
            self.textCheck(list(range(1,9)))

        elif type == "Protocol":
            self.textCheck(list(range(1,9)))

        if text is "":
            self.check = 1

        for listitem in text:       #cant use textCheck because of full stop character
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