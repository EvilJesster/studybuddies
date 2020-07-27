from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email, URL


class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class InfoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    studenttype = SelectField('High School or college?', choices=[('hs', 'High School'), ('C', 'College')],validators=[DataRequired()]) #TODO: look into having the skillist change based on this or smth
    contact = StringField('email', validators=[DataRequired(), Email()])
    skillList = [('calc1', 'Calc 1'), ('calc2', 'Calc 2'), ('calc3', 'Calc 3'), ('chem1', 'Chem 1'), ('chem2', 'Chem 2') ] #TODO: talk to amanda about what to put here
    strengths = SelectMultipleField('areas strong in', choices=skillList)
    weaknesses = SelectMultipleField('areas weak in', choices=skillList)
    pfp = StringField('url to your pfp', validators=[DataRequired(), URL() ])