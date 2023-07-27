from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
    print(name, email, message)

    return render_template("submit.html")




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)