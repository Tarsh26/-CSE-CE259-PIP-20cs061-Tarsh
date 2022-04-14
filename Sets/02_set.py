'''
StudentID:    20CS040
Student Name: shubhangi nakrani
AIM: Write a Python program to remove an item from a set if it is present in the set.
 '''
prime_numbers = {2, 3, 5, 7}

# add 11 to prime_numbers
prime_numbers.add(11)


print(prime_numbers)

if 2 in prime_numbers:
    prime_numbers.remove(2)
print(prime_numbers)
