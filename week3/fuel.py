def main():
    while True:
        try:
            user= input("Enter fraction: ")
            x,y= user.split('/')
            x = int(x) 
            y = int(y)
            if y == 0 or x > y or x < 0 or y < 0:
                raise ValueError("Invalid fraction")
            percentage = round(x / y) * 100
            if percentage < 1:
                print("E")
            elif percentage > 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            continue
        
if __name__ == "__main__":
    main()