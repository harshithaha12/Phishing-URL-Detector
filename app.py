from flask import Flask, render_template, request
from detector import analyze_url

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        url = request.form["url"]

        (
            prediction,
            color,
            score,
            features
        ) = analyze_url(url)

        result = {
            "url": url,
            "prediction": prediction,
            "color": color,
            "score": score,
            "features": features
        }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)