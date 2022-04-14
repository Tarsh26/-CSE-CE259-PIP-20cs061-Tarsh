'''
StudentID:    20CS040
Student Name: shubhangi nakrani
AIM: Write a Python script to add key to a dictionary
 '''
 #Creating three dictioaries with values and one empty one
dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d) # Using update function to add all values in empty dict
print(dic4)