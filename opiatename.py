#Find the first 20 names of opiate overdose victims counted by the program.
import re 
opiate = raw_input("Enter File Name: ")
if len(opiate) < 1 : opiate = "njopiate.txt"
hand = open(opiate)
lst = list()
d = dict()
for line in hand:
    line = line.rstrip()
    names = re.findall('<a title="(.*?),', line)
    if len(names) <1 : continue
    for name in names:
        lst.append(name)
	for name in names:
		d[name] = d.get(name,0) + 1
#print lst
print "First 20 names: ", lst[:20]
print "Last 20 names: ", lst[-20:]
print "Number of first names counted by the program: ", len(lst)

namelist = list()
for key, val in d.items():
    namelist.append( (val, key) )
namelist.sort(reverse=True)
#print namelist

rank = 0
print "List of 100 most common names of overdose victims: "
for apple, orange in namelist[:100] :
	rank = rank + 1
	print rank, '-', orange, apple
