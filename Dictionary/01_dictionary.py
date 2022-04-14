'''
StudentID:    20CS040
Student Name: shubhangi nakrani
AIM: Write a Python script to check whether a given key already exists in a dictionary'''
# Creating a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def keyPresent(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
keyPresent(5)
# keyAbsent(9)
