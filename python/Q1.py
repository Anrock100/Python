intial='''WELCOME TO SUNWAY CHARACTER CHECK SYSTEM
                 MAITIDEVI, KATHMANDU'''
print(intial)
def string(s):
    specialChars=0
    d={"UPPER_CASE":0, "LOWER_CASE":0, "numbers":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        elif c.isdigit():
            d["numbers"] += 1 
        else:
             specialChars+=1
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
    print ("No. of Digits : ", d["numbers"])
    print("No. of SpecialCharacters :",specialChars)
    print ("Thank you for visit")
    
string(input("Enter a letter:"))
