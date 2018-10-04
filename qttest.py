from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog
import sys
import json
import os
import IPv4calc
import string


class CreateWindow(QWidget):
    IPv4Header = []
    LogicData = IPv4calc.IPv4Calc().IPv4Header
    IPv4calcTest = IPv4calc
    datalist = IPv4calc.IPv4Calc().datalist
    counter = 0
    alphabet = string.ascii_letters
    check = 0

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        print(CreateWindow.counter)
        try:
            os.remove('test.json')
        except:
            pass
        self.getChoice()
        self.showDialog(string=self.counter)
        IPv4calc.IPv4Calc().__init__()
        if self.counter == 12:
            self.finalResult()


    def showDialog(self, string):
        self.check = 0
        self.text, self.ok = QInputDialog.getText(self, 'Input Dialog', 'Enter ' + self.datalist[int(string)] + ':')

        if self.inputCheck(text=self.text) == True:
            if CreateWindow.counter < 12:
                CreateWindow.counter += 1
        else:
            QMessageBox.about(self, "Error", "Only integers and dots allowed!")

        self.okButtonClick()
        if not self.ok:
            exit()

    def getChoice(self):
        items = ("bindec","decbin")
        item, okPressed = QInputDialog.getItem(self, "Get item", "Mode:", items, 0 , False)
        if not okPressed:
            exit()
        if okPressed and item:
            self.IPv4calcTest.IPv4Calc.calctype = item

    def inputCheck(self, text):
        for letter in self.alphabet:
            for listitem in text:
                if letter in listitem:
                    self.check = 1
        if self.check == 1:
            return False
        else:
            return True


    def okButtonClick(self):
        if self.ok:
            if self.check == 0:
                with open('test.json', 'a+') as infile:
                    if os.stat('test.json').st_size != 0:
                        data = json.load(infile)
                        self.IPv4Header = data
                    infile.close()
                if self.text is not "":
                    self.IPv4Header.append(self.text)
                print(self.IPv4Header)
            self.showDialog(CreateWindow.counter)


        if self.x:
            with open('test.json', 'a+') as outfile:
                json.dump(self.IPv4Header, outfile)
                outfile.close()

            with open('test2.json', 'w') as outfile:
                json.dump(self.IPv4Header, outfile)
                outfile.close()

    def finalResult(self):
        print("Data by type:",self.LogicData)
        print("Plain data:", "-".join(self.LogicData.values()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreateWindow()
    sys.exit(app.exec_())