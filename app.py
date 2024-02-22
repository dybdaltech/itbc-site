from flask import Flask, render_template, request

app = Flask(__name__)

secret_text = "Correct Answer!"  # Replace with your actual secret text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def process_input():
    user_input = request.form["user_input"]

    if user_input == secret_text:
        return render_template("index.html", show_secret=True, secret_text="Congratulations, you made it!")
    else:
        return render_template("index.html", show_secret=False)

if __name__ == "__main__":
    app.run(debug=False)