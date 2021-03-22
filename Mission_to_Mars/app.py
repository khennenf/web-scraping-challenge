from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():  
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=destination_data)

@app.route("/scrape")
def scrape():
    results = scrape_mars.scrape_info()
    mongo.db.collection({}, results, upsert=True)
 


if __name__ == "__main__":
       app.run(debug=True)


