from flask import Flask, render_template, request
from models.score import Score


app = Flask(__name__)


@app.route("/")
def home():
    score = Score("score.json")
    all_scores = score.get_scores()
    return render_template("home.html", scores=all_scores)


@app.route("/add/score", methods=["POST"])
def add():
    score = Score("score.json")
    data = request.json
    score.add_score(data["score"], data["id"])
    score.save()
    return "", 200


if __name__ == "__main__":
    app.run(debug=True)
