from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
db = SQLAlchemy(app)
# /// - relative path ,////->absolute path

clas  todo(db.model):
   id- db.Column
@app.route('/')
           
def f1():
   return render_template('index.html')   
      
if __name__ =="__main__":
   app.run(debug=True)
         