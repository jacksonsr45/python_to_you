from flask import abort, render_template


def index():
    title = "Home"
    return render_template("index.html", title=title)