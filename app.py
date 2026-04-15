from flask import Flask, render_template, request
from model import predict_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    result_class = ""   # ✅ ALWAYS define it

    if request.method == "POST":
        message = request.form["message"]
        result = predict_message(message)

        if result == "spam":
            prediction = "🚫 Spam Message"
            result_class = "spam"
        else:
            prediction = "✅ Not Spam"
            result_class = "ham"

    return render_template(
        "index.html",
        prediction=prediction,
        result_class=result_class
    )

if __name__ == "__main__":
    app.run(debug=True)