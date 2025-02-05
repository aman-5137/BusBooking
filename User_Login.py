import Database

mydb = Database.connectionDB()
mycursor = mydb.cursor()

def newUser(name, password, number):
    try:
        mycursor.execute(f"INSERT INTO User (uname, upassword, unumber) VALUES (\'{name}\', \'{password}\',\'{number}\')")
        mydb.commit()
        return "True"
    except Exception:
        return "User already exists. Try again."


# print(newUser('aman', 'abc123', '9125285861'))

def existingUser(user, password):
    # if user.isdigit():
    try:
        mycursor.execute(f"SELECT unumber, upassword FROM User where unumber = \'{user}\'")
        result = mycursor.fetchall()
        result = list(result[0])

        r1 = result[0]
        r2 = result[1]

        if r2 == password:
            return "True"
        else:
            return "Password does not match. Try again."
    except Exception:
        return "User does not exist. Try again"
    # else:
    #     try:
    #         mycursor.execute(f"SELECT uname, upassword FROM User where uname = \'{user}\'")
    #         result = mycursor.fetchall()
    #         result = list(result[0])
    #
    #         r1 = result[0]
    #         r2 = result[1]
    #         if r2 == password:
    #             return "True"
    #         else:
    #             return "Password does not match. Try again."
    #     except Exception:
    #         return "False 2"



def User_Profile(number, password):
    try:
        mycursor.execute(f"SELECT uname, unumber FROM User where unumber = \'{number}\'")
        result = mycursor.fetchall()
        result = list(result[0])

        r1 = result[0]
        r2 = result[1]
        return r1, r2
    except Exception:
        print("False")


# print(newUser("aman","abc123","9125285867"))
# print(existingUser("Ravi","ravi123"))
# User_Profile("9125285861","abc123")

# print(existingUser("9125285861","abc11"))