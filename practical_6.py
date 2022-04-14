from collections import Counter #import counter from the collection
l=[]
for i in range(int(input())):#append element
    l.append(input())
#intilized variable and pass list
c=Counter(l)
print(len(c))
for i in c:
    print(c.get(i),end=' ')
print()
