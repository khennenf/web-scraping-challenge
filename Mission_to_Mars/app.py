from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)
destination_data = None #Temp


# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():  
    global destination_data #Temp
    # destination_data = mongo.db.mars.find_one()
    return render_template("index.html", mars=destination_data)

@app.route("/scrape")
def scrape():  
    global destination_data #Temp
    mars_data = scrape_mars.scrape_info()
    # mongo.db.collection.update({}, mars_data, upsert=True)
    destination_data = mars_data #Temp
    return redirect ("/")
 


if __name__ == "__main__":
       app.run(debug=True)


