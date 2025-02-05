from flask import Flask, render_template, request, redirect, url_for, flash
from backend import login,signup, user_profile, home, select_bus, confirm_bookings, show_bus_bookings, show_cancelled_bookings, cancel_bus, user_phnumber
import ast


app = Flask(__name__)
app.secret_key = 'the_secret_key'

phnumber = None
uspassword = None



@app.route('/')
def welcome():

    return render_template('welcome.html')

@app.route('/login', methods = ['POST', 'GET'])
def loginPage():
    return render_template('login.html')




@app.route('/signup')
def signupPage():
    return render_template('signup.html')

@app.route('/raindeer-lgn', methods = ['POST', 'GET'])
def lgn():
    user_phno = request.form.get('userphno')
    user_phno = str(user_phno)
    user_password = request.form.get('password')
    result = login(user_phno, user_password)

    global phnumber,uspassword
    phnumber = user_phno
    uspassword = user_password

    if result == "True":
        with open("phno.txt", "w") as file:
            file.write(user_phno)
        return redirect(url_for('homePage'))
    elif result == "Not a valid number":
        flash("Not a valid number. Please Try Again.", "error")
        return redirect(url_for("loginPage"))
    else:
        flash(result, "error")
        return redirect(url_for('loginPage'))

@app.route('/raindeer-sgnp', methods = ['POST', 'GET'])
def sgnup():
    user_name = request.form.get('name')
    user_phno = request.form.get('user_phno')
    user_phno = str(user_phno)
    user_password = request.form.get('password')

    global phnumber, uspassword
    phnumber = user_phno
    uspassword = user_password

    result = signup(user_name, user_phno, user_password)

    if result == "True":
        with open("phno.txt", "w") as file:
            file.write(user_phno)
        return redirect(url_for('homePage'))

    elif result == "Not a valid number":
        flash("Not a valid number. Please Try Again.", "error")
        return redirect(url_for('signupPage'))
    else:
        flash(result, "error")
        return redirect(url_for('signupPage'))



@app.route('/profile', methods=['POST', 'GET'])
def profile():
    user_no = user_phnumber()
    result = user_profile(user_no, uspassword)
    username = result[0]
    number = result[1]
    return render_template('profile.html', name = username, phnumber = number)

@app.route('/raindeer-home',methods = ['POST', 'GET'])
def homePage():
    return render_template('home.html')

@app.route('/raindeer-hm', methods= ['POST', 'GET'])
def hom():


    source = request.form.get('source')
    source = source.capitalize()
    destination = request.form.get('destination')
    destination = destination.capitalize()
    day = request.form.get('day')

    result = home(source, destination, day)

    if result == []:
        flash('Wrong Location! Or buses not available.')
        return redirect('raindeer-home')
    else:
        return render_template('search_bus.html', source = source, destination = destination, result = result )





@app.route('/selected-bus', methods= ['POST', 'GET'])
def selected_buss():

    source = request.form.get('bus_source')
    print(source, ": source")
    destination = request.form.get('bus_destination')

    bus_id = request.form.get('bus_id')
    bfare = request.form.get('fare')

    lists = request.form.get('data')
    dlists = lists
    lists = ast.literal_eval(lists)
    result = select_bus(bus_id, bfare)



    return render_template('selected_bus.html', data = result, lists = lists, source = source, destination = destination, bfare = bfare, dlists = dlists)



buss_details = []
user_details = []


@app.route('/confirm-booking', methods=['POST', 'GET'])
def confirm_booking():

    user_phno = phnumber
    seats = request.form.get('book_seats')
    availableSeats = request.form.get('availableSeats')

    data = request.form.get('data')
    source = request.form.get('source')
    destination = request.form.get('destination')
    bfare = request.form.get('bfare')
    dlists = request.form.get('dlists')

    lists = dlists
    lists = ast.literal_eval(lists)
    data = ast.literal_eval(data)


    if int(seats)<=0:
        flash("Not a valid number of seats. Please Try Again.", "error")
        return render_template('selected_bus.html', data = data, lists = lists, source = source, destination = destination, bfare = bfare, dlists = dlists)
    if int(seats) > int(availableSeats):
        flash(f"{seats} are not available. Please Try Again.", "error")
        return render_template('selected_bus.html', data = data, lists = lists, source = source, destination = destination, bfare = bfare, dlists = dlists)


    bus_details = request.form.get('data')
    try:
        bus_details = ast.literal_eval(bus_details) if bus_details else []
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing bus_details: {e}")
        bus_details = []


    lists = [user_phno, int(seats)] if seats else [user_phno]

    global buss_details, user_details
    buss_details = bus_details
    user_details = lists
    fare = buss_details[3]
    fare = float(fare) * int(seats)
    buss_details[3] = str(fare)
    passenger_data = []

    return render_template('confirmbooking.html', lists=lists, bus_details=bus_details, seats=seats, passenger_data = passenger_data)


@app.route('/booking-detail', methods=['POST', 'GET'])
def booking_details():
    global user_details, buss_details


    passenger_data = []

    number = request.form.get('seats')
    try:
        number_as_int = int(number)
        for i in range(number_as_int):
            name = request.form.get(f'name_{i}')
            gender = request.form.get(f'gender_{i}')
            age = request.form.get(f'age_{i}')
            pd =[]
            if name and gender and age:
                pd.append(name)
                pd.append(age)
                pd.append(gender)
            passenger_data.append(pd)

    except ValueError:
        print("The provided input is not a valid integer.")


    if not passenger_data:
        return redirect(url_for('confirm_booking'))

    result = confirm_bookings(user_details[0],int(number),buss_details[0],passenger_data,buss_details[3])
    if result == "False":
        return render_template('test.html', result = result)


    return render_template('confirmbooking.html', lists=user_details, bus_details=buss_details,
                           passenger_data=passenger_data, result = result[0])

@app.route('/congrats')
def congrats():
    result = request.form.get('result')
    return render_template('done.html')



@app.route('/booking')
def bookings_done():
    user_no = user_phnumber()
    result = show_bus_bookings(user_no)
    result2 = show_cancelled_bookings(user_no)
    return render_template('bookings.html', result = result, result2 = result2)

@app.route('/raindeer-bookings', methods =['POST'])
def bookings():
    user_no = user_phnumber()

    result = show_bus_bookings(user_no)
    result2 = show_cancelled_bookings(user_no)

    booking_id = request.form.get('booking')
    if booking_id:
        cancel_bus(booking_id, user_no)
        return redirect(url_for('bookings_done', result=result, result2=result2))



@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)



