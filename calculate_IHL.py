class calculate_IHL:

    def getFields(self,item):
        added_length = 4+4+8+16+16+3+13+8+8+16+32+32
        IHL_value = added_length/32

        if item == "bindec":
            return int(IHL_value)
        elif item == "decbin":
            return bin(int(IHL_value)).lstrip("0b")
