myd={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max = max(myd.values())
max2 = 0
lis=[]
for k,v in myd.items():
    if v>max2 and v==max:
        max2 = v
        lis.append(k)
print(lis)

l=[]
for k,v in myd.items():
    if v==max:
        l.append(k)
print(l)

lists=[]
for k,v in myd.items():
    lists.append(k)
print(lists[-1::1])

lis=[]
c =""
mydict = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
for i in range(len(mydict)):
    if mydict[i]['Math']:
        #print(mydict[i]['Math'])
        lis.append(mydict[i]['Math'])
print(lis)
