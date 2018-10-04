import string

testlist = list(string.ascii_letters)

inputtest = ["123","a21","asva"]

for item in testlist:
    for listitem in inputtest:
        if item in listitem:
            print(item,listitem)