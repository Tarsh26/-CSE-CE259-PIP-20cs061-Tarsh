'''
StudentID:    20CS040
Student Name: shubhangi nakrani
AIM: Write a Python script to merge two Python dictionaries
 '''
#Create Dictionary
mydict1 = {"fast": "In a quick manner",
           "Sam": "A coder",
           "marks": [2, 3, 4, 5],
           "anotherDict": {'shubhangi': 'Player'},
           1: 2}
# Creating a Dictionary to update the values
updateDict = {
    'krisha': 'Friend',
    "mayesha": "Friend",
    "Divya": "Friend",
    "Sam": "A Dancer",
}
# Using update function to update and add the values to mydict1
mydict1.update(updateDict)
print(mydict1)