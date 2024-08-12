def main():
    formatted_time = convert(input("What time is it? "))

    if 7 <= formatted_time <= 8:
        print("breakfast time")
    elif 12 <= formatted_time <= 13:
        print("lunch time")
    elif 18 <= formatted_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60

if __name__ == "__main__":
    main()
