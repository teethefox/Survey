from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    return render_template("process.html",name = request.form["name"], location = request.form["location"], language = request.form["language"], comment = request.form["comment"])
    print name + location + language + comment
    return redirect(url_for("/"))
app.run(debug=True)