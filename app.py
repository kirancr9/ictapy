from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def serv():
    return render_template("services.html")

@app.route("/register")
def reg():
    return render_template("reg.html")

if __name__ == "__main__":
    app.run(debug=True)