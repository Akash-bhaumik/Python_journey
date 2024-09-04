a=int(input("Enter the number: "))

print("Generating multiplication table of the number...... ")
for i in range(1,10):
    print(f"{a}x{i}={a*i}")
    i+=1