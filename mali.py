import random
import string

letters = string.ascii_lowercase

forbidden = ["c","h","j","q","x","y","z"]
vowels = ["a", "e", "i", "o", "u"]
consonants = [x for x in letters if x not in vowels and x not in forbidden]


def rm(letter):
    if letter == "rc":
        return random.choice(consonants)
    elif letter == "rv":
        return random.choice(vowels)


mali = [rm("rc"),rm("rv"),rm("rc"),rm("rc"),rm("rv"),rm("rc")]


maliname = ''.join(mali)
print(maliname)
