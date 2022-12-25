# prime number
num =int(input("Enter a Number: "))

if num > 1:
 for i in range(2, int(num/2)+1):
    if(num % i) ==0:
        print(num, "is not a prime number")
        break
    
    else:
        print(num, "is a prime number")
        break
else:
    print(num, "is not a prime number")

def fact(n):
    return 1 if(n==1 or n==0) else n*fact(n-1);
print("Factorial of ",num,"is",fact(num))
