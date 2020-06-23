from flask import Flask, render_template,url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy#

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)#

class User(db.Model):
  id = db.Column(db.Integer,primary_key = True)
  nickname = db.Column(db.String(20),unique=True,nullable = False)
  faculty = db.Column(db.String(50),unique=False,nullable = False)
  grade = db.Column(db.String(10),unique=False,nullable = False)

  def __repr__(self):
    return f"User('{self.nickname}','{self.faculty}','{self.grade}')"

@app.route("/")

def index():
  return render_template('index.html', users=User.query.all())

app.run(host="0.0.0.0", port=8080)