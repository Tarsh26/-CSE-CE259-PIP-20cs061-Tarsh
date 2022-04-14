'''
StudentID:    20CS040
Student Name: shubhangi nakrani
AIM: Write a Python program to add an item in a tuple.
 '''
#create a tuple
tuple1 = (4, 6, 2, 8, 3, 1) 
print(tuple1)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuple1 = tuple1 + (9,)
print(tuple1)
#adding items in a specific index
tuple1 = tuple1[:5] + (15, 20, 25) + tuple1[:5]
print(tuple1)
#converting the tuple to list
listx = list(tuple1) 
#use different ways to add items in list
listx.append(30)
tuple1 = tuple(listx)
print(tuple1)