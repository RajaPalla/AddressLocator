from flask import Flask, render_template

# encapsulating this program in Flask framework server before running it
app = Flask(__name__)

# Application Home page
@app.route('/')
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
