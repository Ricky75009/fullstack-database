from flask import Flask, jsonify, send_file
from flask_cors import CORS 
import sqlite3

app = Flask(__name__)
# enable the api to be accessed by frontend running on localhost
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1"}})

# define what to do when the user navigates to "/"
# this serves a static html file. 
@app.route('/')
def index():
    return send_file("static/html/index.html")

# connect to database

# create function that ask to the database
def get_restaurants(neighborhood_input):

    # connect to the database file, and create a connection object
    db_connection = sqlite3.connect('restaurants.db')

    # create a database cursor object, which allows us to perform SQL on the database. 
    db_cursor = db_connection.cursor()

    # define a query, taking the string input for the neighborhood name 

    query = """SELECT restaurants.name FROM restaurants  
    INNER JOIN neighborhoods ON restaurants.NEIGHBORHOOD_ID=neighborhoods.ID 
    WHERE neighborhoods.NAME=
'{neighborhood_placeholder}'
            """.format(neighborhood_placeholder=neighborhood_input)

    db_cursor.execute(query)

    # store the result in a local variable. 
    # this will be a list of tuples, where each tuple represents a row in the table
    list_restaurants = db_cursor.fetchall()

    db_connection.close()

    return(list_restaurants)

# create the list of name
restaurants=[]
l= get_restaurants("Kreuzberg")
for restaurant in l:
    restaurants.append(restaurant[0])



# A HTTP RESTful API Route returning a list of names of restaurants

@app.route('/api/restaurants/names',  methods=['GET'])
def api_restaurants_names():

    return jsonify(restaurants)



# Run this application if the file is executed, e.g. as "python3 backend.py" 
if __name__ == '__main__':  
    app.testing=True
    app.run() 