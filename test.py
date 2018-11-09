IPv4Header = ['1011', '10101', '10010', '10101', '1010101', '1011111', '10101', '010', '1011101', '011.110.1.11', '1.101.11.1']
testlist = []

for item in IPv4Header:  # jedes header feld:
    if "." in item:  # wenn IP addresse:
        x = []
        x.append(item.split("."))  # jedes oktet als listenitem in temporäre liste einfügen:
        for ipitem in x[0]:
            testlist.append(ipitem)

print(testlist)