'''
StudentID:    20CS040
Student Name: shubhangi nakrani
AIM: Write a Python program to find the most common elements and theri counts from list,tuple.
 '''
 # For List:
# def most_frequent(List):
#     counter = 0
#     num = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency> counter):
#             counter = curr_frequency
#             num = i
 
#     return num
 
# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(List))


# For Tuple:
def most_frequent(t1):
    counter = 0
    num = t1[0]
     
    for i in t1:
        curr_frequency = t1.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
t1 = (2, 1, 2, 2, 1, 3)
print(most_frequent(t1))

