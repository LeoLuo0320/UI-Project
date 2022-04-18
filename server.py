from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

violations_data = {
    "1":{
        "violation_id":"1",
        "title": "Violation Definition",
        "definition": "A violation in basketball is called on any player who breaks or violates a rule of the game defined in the league rulebook.",
        "media_type":"pic",
        "media": "images/violation_definition.png",
    },
    "2":{
        "violation_id":"2",
        "title": "24-Second Violation",
        "definition": "The offensive team must attempt to score a field goal before the shot clock expires; otherwise, the team has committed a shot clock violation.",
        "media_type":"video",
        "media": "https://www.youtube.com/embed/bS_glBGFXdM",
        "video_explanation":"In the video, the ball doesn't touch the basket or the board after 24 seconds, so it is a 24-second violation.",
    },
    "3":{
        "violation_id":"3",
        "title": "8-Second Violation",
        "definition": "After the offensive team recuperate the possession on their backcourt, they have 8 seconds to cross the midcourt line into the frontcourt; otherwise, it is a 8-second violation.",
        "media_type":"video",
        "media": "https://www.youtube.com/embed/HmH3MKwpLqo",
        "video_explanation":"In the video, the player with the ball does not cross the midcourt line after 8 seconds (pay attention to the player’s position when there is 16 seconds left)",
    },
    "4":{
        "violation_id":"4",
        "title": "5-Second Violation",
        "definition": "A team attempting to throw a ball in-bounds has five seconds to release the ball towards the court. The five second clock starts when the teamthrowing it gets the ball.",
        "media_type":"video",
        "media": "https://www.youtube.com/embed/1FxghvK3clo",
        "video_explanation":"In the video, the player with the ball does not cross the midcourt line after 8 seconds (pay attention to the player’s position when there is 16 seconds left)",
    },
}

fouls_data = {
    "1":{
        "foul_id":"1",
        "title": "Fouls Definition & Difference With Violations",
        "definition": "A foul refers to illegal personal contact or unsportsmanlike conduct on the court or sidelines of a game. Most player fouls involve contact that impedes an opposing player's gameplay.",
        "media_type":"pic",
        "media": "images/foul_definition.png",
    },
    "2":{
        "foul_id":"2",
        "title": "Blocking Foul",
        "definition": "A blocking foul is a foul assessed to a defensive player who is not properly positioned and makes contact with an offensive player to stop their movement.",
        "media_type":"video",
        "media": "https://www.youtube.com/embed/VtSiSP0R0hw",
        "video_explanation":"In the video, the defensive player in black is still moving, does not have his feet planted and makes contact with offensive player. It is considered as improper positioned. So it is a blocking foul.",
    },
    "3":{
        "foul_id":"3",
        "title": "Holding Foul",
        "definition": "A holding foul occurs when a defender holds, grabs, or pulls an offensive player (it doesn’t matter if the offensive player has possession of the ball or not)",
        "media_type":"video",
        "media": "https://www.youtube.com/embed/9NJhQ3cWTg8",
        "video_explanation":"In the video, the defensive player wearing No. 11 red jersey holds the offensive player's waist, which is an illegal defensive play. So it is a holding foul.",
    },
    "4":{
        "foul_id":"4",
        "title": "Charging Foul",
        "definition": "A charging foul is called when an offensive player collides illegally with a defender. To make a charging foul, defenders would stand straight up with their feet facing the offensive player",
        "media_type":"video",
        "media": "https://www.youtube.com/embed/yXEKTsNrhtg",
        "video_explanation":"In the video, the defensive player remains planted and does not move before being impacted by the offensive player, so it is a charging foul.",
    },
}

quiz_questions = {
    "1":{
        "quiz_id" : "1",
        "question" : "Watch the video and choose what violation/foul the player made.",
        "num": 0,
        "op1" : '24-second violation',
        "op2" : '8-second violation',
        "op3" : 'Reach-In foul',
        "op4" : 'No violation/foul',
        "ans" : '8-second violation',
        "vid" : "https://www.youtube.com/embed/QgmH11CoM80",
        "score": 0,
        "next_lesson" : "2"
    },
    "2":{
        "quiz_id" : "2",
        "question" : "Watch the video and choose what violation/foul the player made.",
        "num": 1,
        "op1" : '24-second violation',
        "op2" : 'Blocking foul',
        "op3" : '5-second violation',
        "op4" : 'No violation/foul',
        "ans" : '5-second violation',
        "vid" : "https://www.youtube.com/embed/exuw3rPw6vg",
        "score" : 0,
        "next_lesson" : "end"
    }
}

user_info = {
    "num_corret_quiz": "0"
}



# ROUTES
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route("/violations/<violation_id>")
def violations(violation_id):
    violation = violations_data[violation_id]
    return render_template("violations.html", violation=violation)

@app.route("/fouls/<foul_id>")
def fouls(foul_id):
    foul = fouls_data[foul_id]
    return render_template("fouls.html", foul=foul)

@app.route("/quiz/home")
def quiz_home():
    return render_template("quiz_home.html")

@app.route("/quiz/<quiz_id>")
def quiz(quiz_id):
    question = quiz_questions[quiz_id]
    return render_template("quiz.html", question = question, user_info=user_info)

@app.route('/correct_answer', methods=['GET', 'POST', 'PUT'])
def correct_answer():
    user_info["num_corret_quiz"] = str(int(user_info["num_corret_quiz"])+1)
    return user_info

@app.route('/reset_quiz', methods=['GET', 'POST', 'PUT'])
def reset_quiz():
    user_info["num_corret_quiz"] = "0"
    return user_info

if __name__ == '__main__':
   app.run(debug = True)
