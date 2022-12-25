condition=1
print(".............Welcome to shopping website................")
a = input(".........How can we help you?..........")
if("want" in a) or ("shop" in a) or ("buy" in a):
    print("You can buy anything available on this website.")
b = input("...........What you want to buy?............")
if ("shoes" in b) or ("available" in b):
    print("Yes, Shoes are available")
c = input("")
if("price" in c) and ("shoes" in c):
    print("Price of shoes is Rs.3000")
d = input("")
if("discount" in d) and ("price" in d) or ("discount" in d) and ("shoes" in d):
    print("No, There is no discount on shoes")
while(condition==1):
    e = str(input("<<<<<.....Anything else you want to buy?.....>>>>>"))
    if("tshirt" in e) or ("available" in e):
     print("Yes, T shirts are available.")
    f = str(input(""))
    if("price" in f) and  ("tshirt" in f):
     print("Price of 1 T shirt is 2000")
    g = str(input(""))
    if("discount" in g) and ("price" in g) or ("discount" in g) and ("tshirt" in g):
     print("No, There is no discount on T Shirt")

    if("end" in e) or ("nothing" in e):
        condition=2
        print("Thanks for shopping here")