intialDisplay='''Sunway Int'l College Grading System 
                            Maitidevi,Kathmandu     
                                                    Date:'''
print(intialDisplay)
StudentName=input("Enter a name of student :")
StudentAddress=input("Enter your address :")
StudentFaculty=input("Enter your faculty :")
StudentProgrammes=input("Enter your programmes :")
StudentIntake=input("Enter your intake:")
AppliedProgramming, DSA, MIS, DMath, Python=input("Enter marks for each subject, 1.Applied,2.DSA,3.MIS,4.MAth,5.Python").split(",")
print(AppliedProgramming, DSA, MIS, DMath, Python)
Percentage=(int(AppliedProgramming) + int(DSA) + int(MIS) + int(DMath) + int(Python)/500)
if(Percentage>90):
    print("The Grade is A+")
elif(80<Percentage<90):
    print("The Grade is A")
    
elif(70>Percentage<80):
    print("The Grade is B+")
    
elif(60>Percentage<70):
    print("The Grade is B-")
    
elif(50>Percentage<60):
    print("The Grade is B")
    
elif(40>Percentage<50):
    print("The Grade is C+")
    
elif(30>Percentage<40):
    print("The Grade is D+")
    
elif(Percentage<30):
    print("The Grade is Fail")
    
else:
    print("The student grade is {StudentName}")
    
    
    