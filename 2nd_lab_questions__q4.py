n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
n3=int(input("Enter Third Number: "))

if(n1==n2==n3):
    print("All Numbers are equal")
elif(n1==n2):
    print("Number 1 and 2 are Equal")
elif(n2==n3):
    print("Number 2 and 3 are Equal")
elif(n1==n3):
    print("Number 1 and 3 are Equal")  
else: 
    print("No Match")  