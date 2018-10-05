example = "0.111.256.100"


def ipChecker(ip):
    iplist = ip.split(".")

    for part in iplist:
        if part != ".":
            if int(part) not in range(255):
                print("test")

ipChecker(example)