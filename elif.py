A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))

if ((A < B) and (B < C)):
    print("The middle value is ", B)
elif (( C < B) and ( B < A)):
    print("The middle value is ", B)
elif ((A < C) and (C < B)):
    print("The middle value is ", C)
elif ((B < C) and (C < A)):
    print("The middle value is ", C)
else:
    print("The middle value is ", A)
    
