#Find the number of opiate-related overdoses and the 50 towns with the most opiate-related overdoses in 2014 only.
hand = open(opiate)
d = dict()
overdoses = list()
for line in hand:
    line = line.rstrip()
    years = re.findall('<a title=".*,.*,.*, 2014"', line)
    if len(years) < 1 : continue
    #print years
    if years not in overdoses:
        overdoses.append(years)
    towns = re.findall('<a title=".*,.*,(.*), 2014"', line)
    if len(towns) <1 : continue
    for town in towns:
        d[town] = d.get(town,0) + 1
print "Number of opiate overdoses in 2014 alone: ",len(overdoses)
#print d

lst = list()
for key, val in d.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

#print "50 towns with the most opiate overdoses in 2014 alone: ", lst[:50]
#print "50 towns with the least opiate overdoses in 2014 alone: ", lst[-50:]
print "Number of towns with opiate overdoses in 2014 alone: ", len(lst)

print "List of 50 towns with the most opiate overdoses in 2014 only: "
for apple, orange in lst[:50] :
	print orange, "-", apple
