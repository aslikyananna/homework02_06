print("write an hour from the range 0-12")
hour = float(input(" hour "))
print("if am write 1, else write 2")
am_pm = float(input("am(pm) "))
hours = float(input("hours "))
if am_pm == 1:
    if (hour + hours >= 12) and (hour + hours <= 24):
        print((hour + hours - 12), "pm")
    elif hour + hours <= 12:
        print((hour + hours), "am")
    else:
        day = (hour + hours)//24
        rem = (hour + hours) % 24
        if rem >= 12:
            print("after", day, "days", (rem - 12), "pm")
        else:
            print("after", day, "days", rem, "am")
else:
    if (hour + hours >= 12) and (hour + hours <= 24):
        print((hour + hours - 12), "am")
    elif hour + hours <= 12:
        print((hour + hours), "pm")
    else:
        day = (hour + hours) // 24
        rem = (hour + hours) % 24
        if rem >= 12:
            print("after", day, "days", (rem - 12), "pm")
        else:
            print("after", day, "days", rem, "am")
