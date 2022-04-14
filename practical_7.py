l = []
n = int(input())
#append the element
for i in range(n):
    e = input()
    l.append(e)
for i in range(n):
    #get length
    s = len(l[i])
    #variable s for assign the length s%2===0
    if s % 2 == 0:
        #divide index into two parts
        first = l[i][0:int(s / 2)]
        #if odd number then start to second half to endling
        second = l[i][int(s / 2):int(s)]
        third = second[::-1]  # to reverse string stored in second
    else:
        #for even
        first = l[i][0:int(s / 2)]
        second = l[i][int(s / 2) + 1:int(s)]
        third= second[::-1]
        #chack lapindromes
    if first == second or first == third:
        print("YES")
    else:
        print("NO")
