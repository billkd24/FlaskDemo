from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_templates('index.html')

@app.route("/home")
 def home():
     return render_templates('home.html') 

@app.route("/courses")
def greet():
    return "Have a Good Day!"