#Identify the towns with the highest number of opiate-related overdoses in New Jersey between 2004 and 2014.
import re 
opiate = raw_input("Enter File Name: ")
hand = open(opiate)
d = dict()
for line in hand:
    line = line.rstrip()
    towns = re.findall('<a title=".*,.*,(.*),', line)
    if len(towns) <1 : continue
    for town in towns:
        d[town] = d.get(town,0) + 1
#print d

lst = list()
for key, val in d.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

print "50 towns with the most opiate overdoses between 2004 and 2014: ", lst[:50]
#print "50 towns with the opiate overdoses: ", lst[-50:]
print "Number of towns with opiate overdoses from 2004 to 2014: ", len(lst)