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






# Run this application if the file is executed, e.g. as "python3 backend.py" 
if __name__ == '__main__':  
    app.testing=True
    app.run() 