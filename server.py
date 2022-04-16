from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

quiz_questions = {
    "1":{
        "quiz_id" : "1",
        "question" : "Watch the video and choose what violation/foul the player made.",
        "op1" : "24-second violation",
        "op2" : "8-second violation",
        "op3" : "Reach-In foul",
        "op4" : "No violation/foul",
        "ans" : "8-second violation",
        "vid" : "https://www.youtube.com/embed/QgmH11CoM80",
        "next_lesson" : "end"
    }
}

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

@app.route("/quiz/<quiz_id>")
def quiz(quiz_id):
    question = quiz_questions[quiz_id]
    return render_template("quiz.html", question = question)


if __name__ == '__main__':
   app.run(debug = True)
