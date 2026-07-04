def ft_water_reminder():
    days_since = int(input("Days since last watering: "))
    if days_since < 2:
        print("Plants are fine")
    else:
        print("Water the plants!")

# ft_water_reminder()
