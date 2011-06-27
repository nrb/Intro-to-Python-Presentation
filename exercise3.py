quit = False


def is_weekday(day):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    if day in weekdays:
        return "weekday"
    elif day in ["saturday", "sunday"]:
        return "weekend"
    else:
        return "neither"

while not quit:
    day = raw_input("Enter a day name >> ")
    if day == "quit":
        break
    print is_weekday(day)


