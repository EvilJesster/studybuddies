from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class InfoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    studenttype = SelectField('High School or college?', choices=[('hs', 'High School'), ('c', 'College')],validators=[DataRequired()])
    contact = StringField('email', validators=[DataRequired(), Email()])
    skillList = [('calc1', 'Calc 1'), ('calc2', 'Calc 2'), ('calc3', 'Calc 3'), ('chem1', 'Chem 1'), ('chem2', 'Chem 2'), ]
    skills = SelectMultipleField('areas skilled in', choices=skillList)