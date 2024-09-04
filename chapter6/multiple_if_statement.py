a=int(input("Enter the age: "))
if(a%2==0):
    print("a is even")  
if(a>18):
    print("you are above the age of consent")
    print("good for you")
elif(a<0 or a==0):
    print("you are not entering a valid age")
else:
    print("you are below the age of consent")

print("End of the program")