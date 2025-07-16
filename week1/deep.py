user= input("What is the answer to the great question of life, the universe, and everything? ").lower().strip()
match user:
    case "42"|"forty-two"|"forty two":
        print("Yes") 
        
         
    case _:
        print ("No") 