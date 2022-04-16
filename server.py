from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# ROUTES
@app.route('/')
def welcome():
    return render_template('welcome.html')   

@app.route("/violations")
def violations():
    return render_template("violations.html")

@app.route("/fouls")
def fouls():
    return render_template("fouls.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


if __name__ == '__main__':
   app.run(debug = True)




