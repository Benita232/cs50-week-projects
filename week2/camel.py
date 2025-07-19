user= input("Camel case: ")
for i in user:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")