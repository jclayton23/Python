EvenCount = 0
OddCount = 0
EvenTotal = 0
OddTotal = 0
amt = int(input("Enter number to include in average, -1 to end "))

while(amt != -1):
    if(amt %2 == 0):
        EvenTotal = EvenTotal + amt
        EvenCount = EvenCount + 1
        amt = int(input("Enter number to include in average, -1 to end "))
    else:
        OddTotal = OddTotal + amt
        OddCount = OddCount + 1
        amt = int(input("Enter number to include in average, -1 to end "))
print("even average is " + str(EvenTotal / EvenCount) ) 
print("odd average is " + str(OddTotal / OddCount) )
