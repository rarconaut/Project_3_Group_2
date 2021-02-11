import os
from forms import AddForm, DelForm
from flask import Flask, render_template, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# Database
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/job_change"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db = SQLAlchemy(app)
Migrate(app, db)

#######################
# Models
#######################

class Person(db.Model):

    __tablename__ = 'response'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.Text)
    gender = db.Column(db.Text)
    experience = db.Column(db.Text)
    education = db.Column(db.Text)
    major = db.Column(db.Text)
    industry = db.Column(db.Text)
    company_size = db.Column(db.Text)
    
    def __init__(self,location,gender,experience,education,major,industry,company_size):
        self.location = location
        self.gender = gender
        self.experience = experience
        self.education = education
        self.major = major
        self.industry = industry
        self.company_size = company_size
        
    def __repr__(self):
        return f'Location: {self.location}, Gender: {self.gender}, ' \
               f'Experience: {self.experience}, Education: {self.education}, Major: {self.major}, ' \
               f'Industry: {self.industry}, Company Size: {self.company_size}'

    
######
# View functions

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET','POST'])
def add_person():
    form = AddForm()
    
    if form.validate_on_submit():
        location = form.location.data
        gender = form.gender.data
        experience = form.experience.data
        education = form.education.data
        major = form.major.data
        industry = form.industry.data
        company_size = form.company_size.data

        new_entry = Person(location,gender,experience,education,major,industry,company_size)
        db.session.add(new_entry)        
        db.session.commit()    

        return redirect(url_for('list_person'))
    
    return render_template('add.html',form=form)


@app.route('/list')
def list_person():
    person = Person.query.all()
    return render_template('list.html', person=person)

@app.route('/delete', methods=['GET', 'POST'])
def delete_person():

    form = DelForm()
    
    if form.validate_on_submit():
        id = form.id.data
        person= Person.query.get(id)        
        db.session.delete(person)
        db.session.commit()
        

        return redirect(url_for('list_person'))
    
    return render_template('delete.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)