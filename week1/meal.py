#defining a programm that checks the time and tell if breakfast lunch or dinner
def main():
    time = input("What time is the time? ")
    time_in_hours = convert(time)

    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")
    # If it's not any of those times,  print invalid
    else:
        print("invalid")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()