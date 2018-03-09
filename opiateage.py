#Find the average, minimum, maximum, youngest 20, and oldest 20 ages for opiate-related overdoses in New Jersey.
import re 
opiate = raw_input("Enter File Name: ")
if len(opiate) < 1 : opiate = 'njopiate.txt'
hand = open(opiate)
lst = list()
d = dict()
for line in hand:
    line = line.rstrip()
    numbers = re.findall('<a title="?.*, ([0-9]+),', line)
    if len(numbers) <1 : continue
    for number in numbers:
        lst.append(float(number))
	for number in numbers:
		d[number] = d.get(number,0) + 1
lst.sort()

agelist = list()
for key, val in d.items():
    agelist.append( (val, key) )
agelist.sort(reverse=True)
print "Number of opiate overdoses for each particular age:", agelist

rank = 0
print "Number of opiate overdoses for each age sorted by number of overdoses: "
for apple, orange in agelist[:100] :
	rank = rank + 1
	print rank, '-', "Age:", orange+',', "Number of opiate overdoses:", apple

print "Number of opiate overdoses from 2004 to 2014:", len(lst)
print "Note: Number of opiate overdoses may not be accurate since the ages are omitted for a few observations."
print "Average age of opiate overdoses: ", sum(lst)/len(lst)
print "Median age of opiate overdose: ", lst[len(lst)/2]
print "Youngest age of opiate overdose: ", min(lst)
print "Oldest age of opiate overdose: ", max(lst) 
print "Youngest 20: ", lst[:20]
lst.sort(reverse=True)
print "Oldest 20: ", lst[:20]
