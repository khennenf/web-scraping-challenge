from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db
mars_info = db.mars_info


@app.route("/")
def echo():  
    # <!-- teams = list(db.team.find()) -->
    li = ['Sam', 'Lyddie']
    player_dictionary = {"player_1": "Jessica", "player_2": "Mark"}
    return render_template("index.html", dogs = li, dict = player_dictionary)


# @app.route("/scrape")
# def scraper()


if __name__ == "__main__":
       app.run(debug=True)


