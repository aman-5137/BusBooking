# login func
# signup func
# profile func
# home func
# select_bus func
# confirm_booking func
# booking func
# >> booked func
# >> cancelled func
from User_Login import existingUser, newUser, User_Profile


def login(number, password):
    if len(number) == 10:
        if number.isdigit():
            pass
        else:
            return "Not a valid number"
    else:
        return "Not a valid number"

    # if returns false then "the number or the password does not match"
    return existingUser(number, password)


def signup(name, number, password):
    if len(number) == 10:
        if number.isdigit():
            pass
        else:
            return "Not a valid number"
    else:
        return "Not a valid number"

    # if returns "false" then "user already exists"
    return newUser(name, password, number)


def user_phnumber():
    with open("phno.txt", "r") as file:
        content = file.read()
        return content


def user_profile(number, password):
    if len(number) == 10:
        if number.isdigit():
            pass
        else:
            return "Not a valid number"
    else:
        return "Not a valid number"

    # false if user does not exist
    name, number = User_Profile(number, password)
    return [name, number]


from Bus import existing_bus, selectBus, show_bookings


def home(source, destination, day):
    source = source.lower()
    destination = destination.lower()
    r = existing_bus(source, destination)
    lists = []
    for i in range(len(r)):

        bus_number = r[i][0]
        bus_number = bus_number.upper()
        bus_name = r[i][1]
        bus_name = bus_name.upper()
        bus_type = r[i][2]
        bus_type = bus_type.upper()
        bus_source = r[i][4]
        bus_destination = r[i][5]
        bus_fare = r[i][8]
        bus_pickupplace = r[i][9]
        bus_dropplace = r[i][11]
        bus_pickup_time = r[i][10]
        bus_pickup_time = str(bus_pickup_time)
        bus_pickup_time = bus_pickup_time[:-3]

        bus_drop_time = r[i][12]
        bus_drop_time = str(bus_drop_time)
        bus_drop_time = bus_drop_time[:-3]
        bus_seats = r[i][13]
        newbus_fare = bus_fare

        if day == "1":
            bus_fare = newbus_fare
            new_bus_fare = bus_fare * (20 / 100)
            bus_fare = bus_fare + new_bus_fare
        elif day == "2":
            bus_fare = newbus_fare
            new_bus_fare = bus_fare * (10 / 100)
            bus_fare = bus_fare + new_bus_fare
        elif day == "3":
            bus_fare = newbus_fare
            new_bus_fare = bus_fare * (5 / 100)
            bus_fare = bus_fare + new_bus_fare

        bus_source = bus_source + ", " + bus_pickupplace
        text = bus_source
        capitalized_text1 = ' '.join(word.capitalize() for word in text.split())
        bus_source = capitalized_text1

        bus_destination = bus_destination + ", " + bus_dropplace
        text = bus_destination
        capitalized_text2 = ' '.join(word.capitalize() for word in text.split())
        bus_destination = capitalized_text2

        l1 = [bus_number, bus_name, bus_type, bus_fare, bus_source, bus_destination, bus_pickup_time, bus_drop_time,
              str(bus_seats)]
        lists.append(l1)

    # if returns empty list then place does not exist
    return lists


def select_bus(bus_number, bfare):
    r = selectBus(bus_number)
    lists = []

    bus_number = bus_number.upper()
    bus_name = r[0]
    bus_name = bus_name.upper()
    bus_type = r[3]
    bus_type = bus_type.upper()
    bus_source = r[1]
    bus_destination = r[2]
    bus_pickupplace = r[4]
    bus_dropplace = r[6]
    bus_pickup_time = r[5]
    bus_pickup_time = str(bus_pickup_time)
    bus_drop_time = r[7]
    bus_drop_time = str(bus_drop_time)
    bus_seats = r[8]
    bus_fare = bfare

    bus_source = bus_source + ", " + bus_pickupplace
    text = bus_source
    capitalized_text1 = ' '.join(word.capitalize() for word in text.split())
    bus_source = capitalized_text1

    bus_destination = bus_destination + ", " + bus_dropplace
    text = bus_destination
    capitalized_text2 = ' '.join(word.capitalize() for word in text.split())
    bus_destination = capitalized_text2

    l1 = [bus_number, bus_name, bus_type, bus_fare, bus_source, bus_destination, bus_pickup_time, bus_drop_time,
          str(bus_seats)]
    lists.append(l1)

    return lists[0]


# --------------------------------------------------------------------------->>>



# Don't forget to add sum of bus fare for each passenger
# --------------------------------------------------------------->>>


from Bus import booked_buses, cancel_books


def confirm_bookings(user_phno, seats, bus_number, passengers_list, bus_fare, activity="yes"):
    bus_number = bus_number.lower()


    result, booking_id = booked_buses(bus_number, seats, user_phno, bus_fare, activity, passengers_list)
    # returns true or false and booking_id

    return [result, booking_id]


def show_bus_bookings(user_number):
    return show_bookings(user_number, activity="yes")

def cancel_bus(booking_id, user_no):
    cancel_books(booking_id, user_no)
    return

def show_cancelled_bookings(user_number):
    return show_bookings(user_number, activity="no")


# print(login("9125285861", "abc123"))
# print(signup("Aman Kumar Yadav", "9125285863", "aman5137"))
# print(user_profile("9125285861","abc123"))
# print(home("Delhi","Azamgarh", 3))
# print(select_bus("up50ab1234", 1499))
# print(passengers_list(2))
# print(confirm_bookings("9125285861", 3, "UP50AB1234", [['aman', 22, 'male'],['manish', 21, 'male'],['ravi', 22, 'male']], 900))





