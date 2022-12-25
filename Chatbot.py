
print(".............Welcome to my World................")
a = input(".........How can I help you?..........")
if("name" in a) or ("your" in a):
    print("My name is Sunny")
elif ("want" in a) or ("information" in a) or ("project" in a) or ("need" in a):
    b = input("<<<<<.....Which kind of inforation you want?.....>>>>>")
    if("about" in b) and ("project" in b):
        c=input("Which kind of your project is?")
        if("C++" in c) or ("Python" in c) or ("Java" in c):
            print("You can search it online. You will find it easily.")
b = input(".........Any Other Question? Y/N..........")
if("N" in b) or ("n" in b):
 print("Thank you for your Contact")
elif("Y" in b) or ("y" in b):
    a=input("You can ask any kind of question.")
    if("university" in a):
        print("")