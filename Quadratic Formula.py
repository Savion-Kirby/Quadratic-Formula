#Savion Kirby - The Quadratic Formula
import math

#Check Discriminate 
def checkDisc(A,B,C):
    disc = B*B-4*A*C
    print("Discriminate = ", disc)
    if disc<0:
         print("Complex roots")
    if disc == 0:
         print("Only one root")  
    return disc
#Check Odd or Even
def oddeven(x):
    if x%2 == 0:
        print("The value", x, "is even")
    else:
        print("The value",x,"is odd")
    return oddeven

#Start of Code 
print("Quadratic Formula")
print(" ")
A = 0
B = 0
C = 0
loop = 0 #loop

while loop == 0:    
    A = int(input("Please input a value for A"))
    x = A
    x = oddeven(x)
    print(" ")
    B = int(input("Please input a value for B"))
    x = B
    x = oddeven(x)
    print(" ")
    C = int(input("Please input a value for C"))
    x = C
    x = oddeven(x)
    #Solve for the discriminate
    print(" ")
    #Determine if the discrimanate is less than zero
    disc = checkDisc(A,B,C)
    if disc >= 0:
        print("Two roots")
        ROOTONE= (-B + math.sqrt(disc))/(2*A)
        ROOTWO= (-B - math.sqrt(disc))/(2*A)
        print("Root 1 =", ROOTONE)
        print("Root 2 =", ROOTWO)
    print("Run Again?")
    loop = str(input("y|n:"))
    print(" ")
    if loop == "y" or loop == "Y":
        loop = 0
    else:
        loop = 1
        print("Goodbye")

