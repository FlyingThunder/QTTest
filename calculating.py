import json
import os


class IPv4Calc:
    IPv4Header = {}
    calctype = ""
    datalist = ["Version", "TOS", "Length", "Identification", "Flag", "Offset", "TTL", "Protocol",
                "Source", "Destination"]

    def CallPrompt(self):
        calctype = self.calctype
        try:
            with open('test.json','r') as infile:
                if os.stat('test.json').st_size != 0:
                    jsonimport = json.load(infile)
                    for datatype, inputdata in zip(self.datalist, jsonimport):
                        self.InputPrompt(type=calctype, data=datatype, inputdata=inputdata)

        except:
            pass

    def IPConvert(self, input, data, type):
        item2 = []
        item2.append(input.split("."))
        if type == 1:
            for i in range(4):
                item2[0][i] = bin(int(item2[0][i]))
            item2[0] = ([s.replace('0b', '') for s in item2[0]])
        elif type == 2:
            for i in range(4):
                item2[0][i] = str(int(str(item2[0][i]), 2))
        self.IPv4Header[data] = str(item2[0][0] + "." + item2[0][1] + "." + item2[0][2] + "." + item2[0][3])


    def InputPrompt(self, type, data, inputdata):
        if data in ["Source", "Destination"]:
            if "." in inputdata and inputdata.count(".")==3:
                if type == "decbin":
                    self.IPConvert(input=inputdata, data=data, type=1)
                elif type == "bindec":
                    self.IPConvert(input=inputdata, data=data, type=2)
            else:
                print("Invalid IP!")

        else:
            try:
                if type == "decbin":
                    self.IPv4Header[data] = str((bin(int(inputdata)))[2:].zfill(8))
                elif type == "bindec":
                    self.IPv4Header[data] = str((int(inputdata, 2)))
            except:
                pass

if __name__ == "__main__":
    IPv4Calc()


