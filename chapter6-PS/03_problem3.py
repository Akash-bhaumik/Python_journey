p1="make a lot of money"
p2="click here"
p3="subscribe this"
p4="buy now"

message=input("enter the message: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("spam detected")
else:
    print("this comment is spam")