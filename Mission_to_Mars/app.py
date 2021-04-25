from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)
destination_data = None #Temp

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# @app.route("/")
# def home():  
#     global destination_data #Temp
#     destination_data = mongo.db.mars.find_one()
#     if destination_data is None:
#         scrape()
#     return render_template("index.html", mars=destination_data)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=destination_data)



# @app.route("/scrape")
# def scrape():  
#     global destination_data #Temp
#     mars_data = scrape_mars.scrape_info()
#     mongo.db.collection.update({}, mars_data, upsert=True)
#     destination_data = mars_data #Temp
#     return redirect ("/")
 
# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
       app.run(debug=True)


