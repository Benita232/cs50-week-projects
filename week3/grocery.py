def main():
    grocery_list = {}
    
    try:
        while True:
            item = input().strip().upper()
            if item:  # Ignore empty inputs
                grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass
    
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item}")

if __name__ == "_main_":
    main()