from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def echo():
    li = ['Sam', 'Lyddie']
    player_dictionary = {"player_1": "Jessica", "player_2": "Mark"}
    return render_template("index.html", dogs = li, dict = player_dictionary)

if __name__ == "__main__":
    app.run(debug=True)


