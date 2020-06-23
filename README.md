# jn-lec-LAMP
assignment for LAMP lecture

## Using Flask & SQLALCHEMY
severh.py:
```python
#imports
from flask import Flask, render_template,url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

#defining the app and db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)#

#defining the User class
class User(db.Model):
  id = db.Column(db.Integer,primary_key = True)
  nickname = db.Column(db.String(20),unique=True,nullable = False)
  faculty = db.Column(db.String(50),unique=False,nullable = False)
  grade = db.Column(db.String(10),unique=False,nullable = False)

  def __repr__(self):
    return f"User('{self.nickname}','{self.faculty}','{self.grade}')"
```

## Registering user information to the db via CLI
terminal:
```
$python 
>>>from serverh import db
>>>db.create_all()
>>>from serverh import User
>>>user1 = User(nickname = "hhiromasa", faculty ="EI", grade = "B2")
>>>db.session.add(user1) 
>>>db.session.commit()
>>>User.query.all()
```

## returning html file with registered information
severh.py:
```python
@app.route("/")

#once localhost is requested, render index.html. Pass the user information to the index.html file.
def index():
  return render_template('index.html', users=User.query.all())
```
index.html:
```html
<!-- display the user information -->
{{users}}
```

## Run the app
severh.py:
```python
app.run(host="0.0.0.0", port=8080)
```

send a GET request to "ht<span>tp://0.0.0.0:8080/" to see the results. <br>
ht<span>tp://0.0.0.0:8080/:
 ```HTML
  [User('hhiromasa','EI','B2')]
 ```

