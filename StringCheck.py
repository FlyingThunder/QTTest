class StringCheck:
    check = 0


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
            try:
                if int(self.text) not in textlist:
                    self.check = 1
            except:
                pass
        elif self.item == "bindec":
            if self.text not in textlist2:
                self.check = 1


    def inputCheck(self, text, type, item):
        self.check = 0
        self.text = text
        self.item = item

        if text is "":
            self.check = 1

        for listitem in text:       #cant use textCheck because of full stop character
            if self.item == "decbin":
                if type not in ["Source","Destination"]:
                    if listitem not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        self.check = 1
            elif self.item == "bindec":
                if listitem not in ["0","1","."]:
                    self.check = 1

        if type in ["Source","Destination"]:
            if "," in text:
                self.check = 1
            if text.count(".") == 3:
                if self.ipChecker(text) == False:
                    self.check = 1
            else:
                self.check = 1

        elif type == "Version":
            self.textCheck([4,6])

        elif type == "TOS":
            self.textCheck(list(range(1,256)))

        elif type == "Length":
            self.textCheck(list(range(1,65536)))

        elif type == "Identification":
            self.textCheck(list(range(1,65536)))

        elif type == "Flag":
            self.textCheck(list(range(1,8)))

        elif type == "Offset":
            self.textCheck(list(range(1,8192)))

        elif type == "TTL":
            self.textCheck(list(range(1,256)))

        elif type == "Protocol":
            self.textCheck(list(range(1,256)))

        if self.check == 1:
            return False
        else:
            return True
