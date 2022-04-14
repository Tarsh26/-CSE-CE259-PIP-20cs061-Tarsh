'''20cs040 shubhangi nakrani'''
String = str(input()) #took from the user
new = " "#new string
for i in range(len(String)):
    #to convert lowercase
    if String[i].isupper():
        new += String[i].lower()
        #to convert uppercase
    elif String[i].islower():
        new += String[i].upper()
        #spacing or other symbols
    else:
        new += String[i]
#print the updated string
print(new)