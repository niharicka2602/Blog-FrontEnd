from flask import Flask, app, render_template, request, redirect, url_for
from . import BinarySearch, Fibonnaci, Knapsack 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/BinarySearch.py', methods = ['GET', 'POST'])
def addbinary():
    if request.method == 'POST':
        arr = request.form.get("enterarray")
        x = request.form.get("pivot")
        return render_template("index.html")

@app.route('/Fibonnaci.py', methods = ['GET', 'POST'])
def addbinary():
    if request.method == 'POST':
        n = request.form.get("entern")
        return render_template("index.html")

@app.route('/Knapsack.py', methods = ['GET', 'POST'])
def addbinary():
    if request.method == 'POST':
        val = request.form.get("entervalue")
        wt = request.form.get("enterweight")
        W = request.form.get("entercapacity")
        return render_template("index.html")

if __name__ == "__main__":
    app.run()