from flask import Flask, render_template
from business import getCoordinates

# encapsulating this program in Flask framework server before running it
app = Flask(__name__)

# Api to show 4 types of maps with mapIds as ROADMAP, TERRAIN, HYBRID, SATELLITE
@app.route('/<place>')
def getMap(place):
    dictMap = getCoordinates(place)
    return render_template("mappy.html", locator=dictMap, place=place)

# Application Home page
@app.route('/')
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
