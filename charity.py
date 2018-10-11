#!/usr/bin/python

from flask import Flask, redirect, request, render_template

app = Flask(__name__)

balance = 0

@app.route("/", methods=["GET", "POST"])
def root():
    return redirect("/index.html")

@app.route("/index.html", methods=["GET", "POST"])
def index():
    global balance
    pledge = float(request.values.get("pledge", 0))
    balance = balance + pledge
    return render_template("index.html", balance=balance, pledge=pledge)

if __name__ == '__main__':
    app.run(debug=True)

