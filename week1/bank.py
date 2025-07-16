'''
user= input("Enter your greeting: ").lower().strip
if user.startswith("h"): 
    print("$20")
elif user == "hello":
    print("$0")
else:
    print("$100")
'''

user = input("Enter your greeting: ").lower().strip()

if user.startswith("hello"):
    print("$0")
elif user.startswith('h'):
    print("$20")
else:
    print("$100")
    