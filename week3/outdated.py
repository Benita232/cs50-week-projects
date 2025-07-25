# outdated.py
def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    while True:
        s = input("Date: ").strip()
        
        # Format: Month Day, Year (September 8, 1636)
        if ',' in s:
            parts = s.split()
            if len(parts) != 3:
                continue
                
            month_str, day_str, year_str = parts
            day_str = day_str.rstrip(',')
            
            if not day_str.isdigit():
                continue
                
            try:
                day = int(day_str)
                year = int(year_str)
            except ValueError:
                continue
                
            month_str = month_str.title()
            if month_str in months:
                month = months.index(month_str) + 1
                if 1 <= day <= 31:
                    print(f"{year}-{month:02d}-{day:02d}")
                    return
        
        # Format: MM/DD/YYYY (9/8/1636)
        elif '/' in s:
            parts = s.split('/')
            if len(parts) != 3:
                continue
                
            try:
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])
            except ValueError:
                continue
                
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02d}-{day:02d}")
                return

if __name__ == "__main__":
    main()


