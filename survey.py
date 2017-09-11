from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="Secrettttttt"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("Error : Name cannot be blank")
        return redirect("/")
    elif len(request.form['comment']) <1:
        flash("Error: Comment cannot be blank")
        return redirect("/")
    elif len(request.form['comment']) > 120:
        flash("Error: Comment cannot be longer than 120 characters.")
        return redirect("/")
    else:
        return render_template("process.html",name = request.form["name"], location = request.form["location"], language = request.form["language"], comment = request.form["comment"])
        print name + location + language + comment
    return redirect("/")
app.run(debug=True)