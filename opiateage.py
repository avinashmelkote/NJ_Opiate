#Find the average, minimum, maximum, youngest 20, and oldest 20 ages for opiate-related overdoses in New Jersey.
import re 
opiate = raw_input("Enter File Name: ")
hand = open(opiate)
lst = list()
for line in hand:
    line = line.rstrip()
    numbers = re.findall('<a title="?.*, ([0-9]+),', line)
    if len(numbers) <1 : continue
    for number in numbers:
        lst.append(float(number))
lst.sort()
print "Number of opiate overdoses from 2004 to 2014:", len(lst)
print "Note: Number of opiate overdoses may not be accurate since the ages are omitted for a few observations."
print "Average age of opiate overdoses:", sum(lst)/len(lst)
print "Median opiate overdose age:", lst[len(lst)/2]
print "Youngest opiate overdose age:", min(lst)
print "Oldest opiate overdose age:", max(lst) 
print "Youngest 20:", lst[:20]
lst.sort(reverse=True)
print "Oldest 20:", lst[:20]