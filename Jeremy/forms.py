from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    location = SelectField('Course Location: ',choices=[('Berkely', 'Berkeley'), ('UCSD', 'UCSD')])
    gender = SelectField('Gender: ',choices=[('Male', 'Male'), ('Female', 'Female')])
    experience = SelectField('Relevant Data Science Experience: ',choices=[('yes', 'Has Relevant Experience'), ('some', 'Has Some Relevant Experience'), ('none', 'Has No Relevant Experience')])
    education = SelectField('Education: ',choices=[('HS', 'High School'), ('AA', 'AA'), ('Undergrad', 'Undergrad'), ('Masters', 'Masters'), ('Other', 'Other')])
    major = SelectField('Major: ',choices=[('Liberal Arts', 'Liberal Arts'), ('Business-Finance/Accounting', 'Business-Finance/Accounting'), ('Sciences- Data, Computer', 'Sciences- Data, Computer'), ('Sciences- Bio, Chem, other..', 'Sciences- Bio, Chem, other..'), ('Other', 'Other')])
    industry = SelectField('Industry: ',choices=[('Tech/Start-up', 'Tech/Start-up'), ('Hospitality', 'Hospitality'), ('Media Entertainment', 'Media Entertainment'), ('Financial Institutions/Banking', 'Financial Institutions/Banking'), ('Other', 'Other')])
    company_size = SelectField('Company Size: ',choices=[('1-50', '1-50'), ('50-100', '50-100'), ('100-150', '100-150'), ('150-300', '150-300'), ('300+', '300+')])
    submit = SubmitField('Submit')

class DelForm(FlaskForm):
    id = IntegerField("Id Number of person to remove: ")
    submit = SubmitField("Remove Person")


    