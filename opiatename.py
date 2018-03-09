#Find the first 20 names of opiate overdose victims counted by the program.
import re 
opiate = raw_input("Enter File Name: ")
hand = open(opiate)
lst = list()
for line in hand:
    line = line.rstrip()
    names = re.findall('<a title="(.*?),', line)
    if len(names) <1 : continue
    for name in names:
        lst.append(name)
print "First 20 names: ", lst[:20]
print "Last 20 names: ", lst[-20:]
print "Total number of first names counted by the program: ", len(lst)