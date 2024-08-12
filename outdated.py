months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    date = date.strip()
    if "/" in date:
        month, day, year = date.split("/")

        try:
            if int(month) > 12 or int(day) > 31: continue
            if len(day) == 1: day = "0" + day
            if len(month) == 1: month = "0" + month
        except ValueError:
            continue
        print(year, month, day, sep="-")
        break
    else:
        month, day, year = date.split(" ")
        try:
            month = months.index(month) +1
        except ValueError:
            continue
        if "," in day:
            day = day.removesuffix(",")
        else:
            continue
        if len(day) == 1: day = "0" + day
        if int(day) > 31: continue
        if month < 10:
            print(year,f"{month:02}", day, sep="-")
        else:
            print(year, month, day, sep="-")
        break
