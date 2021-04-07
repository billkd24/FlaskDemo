from flask import Flask, render_template, url_for, request, redirect 

#toolkit and onbject-relation mapper for python
from flask_sqlalchemy import SQLAlchemy

#import datetime
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///root.db'

#initiialize the db with our app settings
db = SQLAlchemy(app)

#create the db model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(400), nullable=False)
    complete = db.Column(db.Integer, default=0)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __tsl__(self):
        return '<Entry %r>' &self.id

#from app import db
#db.create_all()



@app.route('/', methods = ['POST' , 'GET'])
def index ():
    if  request.method == 'POST':
        entry_content = request.form['content']
        new_entry = Task(content = entry_content)

        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/')
        except:
            return "Error Creating Task"
    else:
        entries = Task.query.order_by(Task.date_added).all()
        return render_template ('index.html', entries = entries)

if __name__ == "__main__":
    app.run(degub=True)







#@app.route("/")
#def default ():
    #return render_template('index.html')

#@app.route("/home")
#def home ():
     #return render_template('home.html') 

#@app.route("/courses")
#def greet():
    #return "Have a Good Day!"