class chksum:
    # self.IPv4Header
    # self.LogicData.values()
    # self.item = mode
    def calcChecksum(self, mode, inputdata, outputdata):
        for item in inputdata:            #jedes header feld des inputs:
            if "." in item:                     #wenn IP addresse:
                x = []
                x.append(item.split("."))
                for ipitem in x[0]:
                    if mode == "bindec":
                        self.templistin.append(int(str(ipitem), 2)) #jedes oktet als dezimalwert in die liste einfügen
                    elif mode == "decbin":
                        self.templistin.append(int(ipitem))
            else:
                if mode == "bindec":
                    self.templistin.append(int(str(item), 2)) #jedes andere feld als dezimalwert in liste einfügen
                elif mode == "decbin":
                    self.templistin.append(int(item))

        for item in outputdata:    #jedes header feld des outputs:
            if "." in item:                     #wenn IP addresse:
                y = []
                y.append(item.split("."))
                for ipitem in y[0]:
                    if mode == "bindec":
                        self.templistout.append(int(ipitem))    #jedes oktet als listenitem in temporäre liste einfügen:
                    elif mode == "decbin":
                        self.templistout.append(int(str(ipitem), 2))
            else:
                if mode == "bindec":
                    self.templistout.append(int(item))               #jedes andere feld in liste einfügen
                elif mode == "decbin":
                    self.templistout.append(int(str(item), 2))

    def outChecksum(self, mode, inputdata, outputdata): #IPv4Header = InputList, LogicData = OutputDict
        self.templistin = []
        self.templistout = []

        if mode == "bindec":
            self.calcChecksum(mode = "bindec", inputdata=inputdata, outputdata=outputdata)
        elif mode == "decbin":
            self.calcChecksum(mode = "decbin", inputdata=inputdata, outputdata=outputdata)

        self.inputchecksum = sum(self.templistin)  # liste summieren
        self.outputchecksum = sum(self.templistout)  # liste summieren

        return self.inputchecksum, self.outputchecksum