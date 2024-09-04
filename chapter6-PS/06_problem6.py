marks1=int(input("Enter the marks1: "))
marks2=int(input("Enter the marks2: "))
marks3=int(input("Enter the marks3: "))

total_percentage=(100*(marks1+marks2+marks3)/300)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed: ",total_percentage)
else:
    print("you are failed: ",total_percentage)

print("generating your grade........ ")

if(total_percentage>=90 and total_percentage<=100):
    garde="Ex"
elif(total_percentage>=80 and total_percentage<90):
    garde="A"
elif(total_percentage>=70 and total_percentage<80):
    garde="B"
elif(total_percentage>=60 and total_percentage<70):
    garde="C"
elif(total_percentage>=50 and total_percentage<60):
    garde="D"
elif(total_percentage<50):
    garde="F"

print("your obtained grade is: ",garde)