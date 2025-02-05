from flask import Flask, render_template, request, redirect, url_for, flash
from Bus import new_Bus

app = Flask(__name__)
app.secret_key = 'your_unique_secret_key'


@app.route('/')
def add_new_bus():
    return  render_template('add_busses.html')

@app.route('/added_new_bus', methods = ['POST', 'GET'])
def main_add():
    bus_number = request.form.get('busnumber')
    bus_name = request.form.get('busname')
    bus_type = request.form.get('bustype')
    bus_time = request.form.get('bustime')
    bus_source = request.form.get('bussource')
    bus_destination = request.form.get('busdestination')
    bus_distance = request.form.get('busdistance')
    bus_duration = request.form.get('busduration')
    bus_fare = request.form.get('busfare')
    bus_pickupplace = request.form.get('buspickupplace')
    bus_pickuptime = request.form.get('buspickuptime')
    bus_dropplace = request.form.get('busdropplace')
    bus_droptime = request.form.get('busdroptime')
    bus_seats = request.form.get('busseats')
    # print(bus_duration)

    result = new_Bus(bus_number, bus_name, bus_type, bus_time, bus_source, bus_destination, int(bus_distance), bus_duration, float(bus_fare), bus_pickupplace, bus_pickuptime, bus_dropplace, bus_droptime, int(bus_seats))
    if result == "True":
        return render_template('add_busses.html')
    else:
        flash(f"You gave a wrong inputs. {result}", "error")
        return redirect(url_for('add_new_bus'))

if __name__ == "__main__":
    app.run(debug=True)


# bus number
# bus name
# bus type
# bus time
# bus source
# bus destination
# bus distance
# bus duration
# bus fare
# bus pickup_place
# bus pickup_time
# bus drop_place
# bus drop_time
# bus seats

