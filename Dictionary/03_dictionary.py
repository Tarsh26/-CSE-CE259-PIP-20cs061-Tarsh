'''        
StudentID:    20CS040
Student Name: shubhangi nakrani
AIM: Write a Python program to sum all the items in a dictionary
 '''
 # Calculating the sum
def calculateSum(myDict):
     
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
     
    return final
# Create a Dictionary
dict = {'a': 500, 'b':100, 'c':300}
print("Sum :", calculateSum(dict))