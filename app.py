from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(20),nullable=False)
    password=db.Column(db.String(20),nullable=False)


    def __repr__(self):
        return f'<User name {self.username}>'
    
@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/success',methods=['GET','POST'])
def success():
    if request.method =='POST':
        try:
            with app.app_context():
                uname=request.form['uname']
                email=request.form['email']
                passw=request.form['pass']
                new_user=User(username=uname,email=email,password=passw)
                db.session.add(new_user)
                db.session.commit()
        except:
            print(f"Error has occured")
    return render_template('sucess.html')


if __name__=='__main__':
    with app.app_context():
        db.create_all()
      
        # Retrieve all users from the 'User' table
        users = User.query.all()

        # Do something with the data
        for user in users:
            print(user.id, user.username, user.email, user.password)
    app.run(debug=True)
