def main():
    plate=input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1:].isalnum():
        return False
    if s[-1].isdigit():
        for i in range(len(s)-1):
            if s[i].isdigit():
                return False
    if " " in s:
        return False
    return True

if __name__ == "__main__":
    main()