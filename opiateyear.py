#Find the number of opiate-related overdoses in New Jersey for each year between 2004 and 2014. 
import re 
opiate = raw_input("Enter File Name: ")
hand = open(opiate)
d = dict()
for line in hand:
    line = line.rstrip()
    years = re.findall('<a title=".*,.*,.*,(.*?)"', line)
    if len(years) <1 : continue
    for year in years:
        d[year] = d.get(year,0) + 1
#print d
#"d" would be printed in hash order, so it would not be sorted by year.

lst = d.keys()
lst.sort()
for key in lst:
    print key, d[key]