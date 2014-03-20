def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return

def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3 and days < 7:
        return days * 40  - 20
    else:
        return days * 40
