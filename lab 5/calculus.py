
#1
import re
file = open("row.txt", "r")
string = file.read()
file.close()

x = re.search(".*a+b*.*", string)

if x:
    print(x)
else:
    print("No such")

#2 x = re.search(".*ab{2}|b{3}", string)

#3
x = re.findall("[a-z]*_[a-z]*", string)  #4
x = re.findall("[A-Z]{1}[a-z]*", string)

#5
x = re.search(".*a*.*b$", string)
 #6
x = re.sub("[,. ]", ":", string)

#7
y = re.search("_(\w)", string)
x = re.sub("_(\w)", y[1].upper(), string)

#8
x = re.split("[A-Z]", string)

#9
x = re.sub(r"([a-z]*)([A-Z])", r"\1 \2", string)

#10
x = re.sub(r"([a-z])([A-Z])", lambda match: match.group(1) + "_" + match.group(2).lower(), string)

