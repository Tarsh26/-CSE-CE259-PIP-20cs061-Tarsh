#20cs040 shubhangi nakrani
lis = []# list initialised and stored in variable l
num = int(input())  # number of entries stored in variable n
for i in range(num):
    # took values from user
    e = int(input())
    # elements gets append in list l
    lis.append(e)
 # to remove repetition of an element
l = set(lis)
# again converted to list
l = list(lis)
print(l)
# sorted the array
l.sort()
# runner's up means the second max that is second last element present in sorted list
r = l[num-2]
# printed runner up value
print( r)

