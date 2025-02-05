import Database

mydb = Database.connectionDB()
mycursor = mydb.cursor()

def new_Bus(number, name, type, time, source, destination, distance, duration, fare, pickupPlace, pickupTime, dropPlace, dropTime, seats):
    number = number.lower()
    name = name.lower()
    type = type.lower()
    source = source.lower()
    destination = destination.lower()
    pickupPlace = pickupPlace.lower()
    dropPlace = dropPlace.lower()
    if seats<=0:
        return "False"


    try:
        mycursor.execute(f"INSERT INTO bus_detail (bnumber, bname, btype, btime, bsource, bdestination, bdistance, bduration, bfare, bpickupPlace, bpickupTime, bdropPlace, bdropTime, bseats)"
                         f" VALUES (\'{number}\',"
                         f" \'{name}\',"
                         f"\'{type}\',"
                         f"\'{time}\',"
                         f"\'{source}\',"
                         f"\'{destination}\',"
                         f"\'{distance}\',"
                         f"\'{duration}\',"
                         f"\'{fare}\',"
                         f"\'{pickupPlace}\',"
                         f"\'{pickupTime}\',"
                         f"\'{dropPlace}\',"
                         f"\'{dropTime}\',"
                         f"\'{seats}\')")
        mydb.commit()
        return "True"
    except Exception as e:
        return e


# print(new_Bus("UP50AB4321", "VOLVO", "AC", '04:55', "Delhi", "Azamgarh", 870.23, 15, 1200, "Kausambi Delhi", '15:40', "Bhavarnath Azamgarh", '04:00', 44))
# print(new_Bus("UP50AB1234", "VOLVO-1", "AC", '04:55', "Delhi", "Azamgarh", 870.23, 15, 1400, "Kausambi Delhi", '15:40', "Bhavarnath Azamgarh", '04:00', 44))

def update_bus(number, name, type, time, source, destination, distance, duration, fare, pickupPlace, pickupTime, dropPlace, dropTime, seats):
    try:
        mycursor.execute(f"UPDATE bus_detail SET "
                         f"bnumber = \'{number}\', "
                         f"bname = \'{name}\', "
                         f"btype = \'{type}\', "
                         f"btime = \'{time}\', "
                         f"bsource = \'{source}\', "
                         f"bdestination = \'{destination}\', "
                         f"bdistance = \'{distance}\', "
                         f"bduration = \'{duration}\', "
                         f"bfare = \'{fare}\', "
                         f"bpickupPlace = \'{pickupPlace}\', "
                         f"bpickupTime = \'{pickupTime}\', "
                         f"bdropPlace = \'{dropPlace}\', "
                         f"bdropTime = \'{dropTime}\',"
                         f"bseats = \'{seats}\' WHERE bnumber = \'{number}\'")
        mydb.commit()
        if mycursor.rowcount == 0:
            return "False1"
        return "True"
    except Exception as e:
        return e


# print(update_bus("UP50AB4321", "VOLV", "AC", '04:55', "Delhi", "Azamgarh", 870.23, 15, 1200, "Kausambi Delhi", '15:40', "Bhavarnath Azamgarh", '04:00', 44))




def delete_bus(number):
    try:
        mycursor.execute(f"DELETE FROM bus_detail WHERE bnumber = \'{number}\';")
        mydb.commit()
        if mycursor.rowcount == 0:
            return "False"
        return "True"
    except Exception:
        return "False"


# print(delete_bus("UP50AB1234"))


def existing_bus(source, destination):
    try:
        sqls = f"""
                SELECT * 
                FROM bus_detail 
                WHERE (bsource = '{source}' OR bpickupPlace = '{source}')
                  AND (bdestination = '{destination}' OR bdropPlace = '{destination}');
                """
        mycursor.execute(sqls)
        result = mycursor.fetchall()
        return result

    except Exception:
        print("False")
# print(existing_bus("delhi", "azamgarh"))


def selectBus(number):
    try:
        mycursor.execute(f"SELECT bname, bsource, bdestination, btype, bpickupPlace, bpickupTime, bdropPlace, bdropTime, bseats FROM bus_detail WHERE bnumber = \'{number}\';")
        result = mycursor.fetchall()
        lists = []
        for i in range(len(result[0])):
            if i == 5 or i == 7:
                time = str(result[0][i])
                time = time[:-3]
                lists.append(time)
                continue
            lists.append(str(result[0][i]))
        return lists

    except Exception:
        return "False"


# print(selectBus("UP50AB1234"))


def lists_addresses():

    try:
        mycursor.execute(f"SELECT bsource, bpickupPlace FROM bus_detail;")
        result1 = mycursor.fetchall()
        result1 = list(result1[0])
    except Exception:
        return "False"

    try:
        mycursor.execute(f"SELECT bdestination, bdropPlace FROM bus_detail;")
        result2 = mycursor.fetchall()
        result2 = list(result2[0])


    except Exception:
        return "False"
    result = [result1,result2]
    # returns the list of sources and destinations in 2d list
    return result

# print(lists_addresses())



def update_seats(bus_number,add_or_subtract , booked_seats):
    try:
        mycursor.execute(f"SELECT bseats FROM bus_detail WHERE bnumber = \'{bus_number}\';")
        result1 = mycursor.fetchall()
        result1 = list(result1[0])
        result1 = result1[0]

    except Exception:
        return "False"

    seats = None
    if add_or_subtract =="add":
        seats = result1 + booked_seats
    elif add_or_subtract =="subtract":
        seats = result1 - booked_seats

    try:
        mycursor.execute(f"UPDATE bus_detail SET bseats = \'{seats}\' WHERE bnumber = \'{bus_number}\';")
        mydb.commit()
        if mycursor.rowcount == 0:
            return "False"
        return "True"

    except Exception:
        return "False"
    #

# print(update_seats("UP50AB4321","subtract", 4))


def booked_buses(busno, seats, userphno, bfare, activity, pdetails):# pnames: list of passengers name, age and gender; activity: yes/no
    try:
        mycursor.execute(f"INSERT INTO booked_buses (busno, busfare, userphno, seats, activity) VALUES"
                         f"(\'{busno}\',"
                         f"\'{bfare}\',"
                         f"\'{userphno}\',"
                         f"\'{seats}\',"
                         f"\'{activity}\');")
        mydb.commit()

    except Exception:
        return "False"

    try:
        mycursor.execute("SELECT booking_id FROM booked_buses;")
        booking_id = mycursor.fetchall()

    except Exception:
        return "False"
    booking_id = booking_id[len(booking_id)-1]
    booking_id = booking_id[0]

    try:
        for i in range(seats):
            mycursor.execute(f"INSERT INTO passengers (booking_id, p_name, p_age, p_gender) VALUES (\'{booking_id}\',\'{pdetails[i][0]}\', \'{pdetails[i][1]}\', \'{pdetails[i][2]}\');")
            mydb.commit()

        return "True", booking_id
    except Exception:
        return "No Passenger", None



def show_bookings(user_number, activity):

    try:
        mycursor.execute(f"SELECT booking_id, busno, seats, busfare FROM booked_buses WHERE userphno = \'{user_number}\' AND activity = \'{activity}\';")
        result1 = mycursor.fetchall()
    except Exception as e:
        return e



    result4 = []
    result5 =[]
    try:
        for i in range(len(result1)):
            bus_no = result1[i][1]
            mycursor.execute(f"SELECT bname, bnumber, bsource, bpickupPlace, bdestination, bdropPlace, bpickupTime, bdropTime FROM bus_detail WHERE bnumber = \'{bus_no}\'; ")
            result3 = mycursor.fetchall()
            result4.append(result3[0])

            result5.append(result4[0])
        # print(result5[0])
    except Exception as e:
        return e

    result = []
    for i in range(len(result5)):
        booking_ids = result1[i][0]
        busnumber = result5[i][1]
        busname = result5[i][0]
        pickupplace = result5[i][2]+", "+ result5[i][3]
        pickuptime = result5[i][6]
        dropplace = result5[i][4]+", "+ result5[i][5]
        droptime = result5[i][7]

        passengers = result1[i][2]


        busnumber = busnumber.upper()
        busname = busname.upper()

        text = pickupplace
        capitalized_text1 = ' '.join(word.capitalize() for word in text.split())
        pickupplace = capitalized_text1

        text = dropplace
        capitalized_text2 = ' '.join(word.capitalize() for word in text.split())
        dropplace = capitalized_text2


        pickuptime = str(pickuptime)
        pickuptime = pickuptime[:-3]
        droptime = str(droptime)
        droptime = droptime[:-3]
        emp = [busnumber, busname, pickupplace, pickuptime, dropplace, droptime, str(passengers), str(booking_ids)]
        result.append(emp)
    return result[::-1]

# print(show_bookings("9125285867", "yes"))

def cancel_books(booking_id, userphno):
    activity = "no"
    try:
        mycursor.execute(f"UPDATE booked_buses SET activity = \'{activity}\' WHERE userphno= \'{userphno}\' AND booking_id = \'{booking_id}\';")
        mydb.commit()

        return True
    except Exception:
        return False



# print(cancel_books(39, "9125285861"))
# print(booked_buses("up50ab1234", 3, "9125285861", 1449, 'yes', [['aman', 22, 'male'],['manish', 21, 'male'],['ravi', 22, 'male']]))




















