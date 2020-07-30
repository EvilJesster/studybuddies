from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SelectMultipleField, FormField, FieldList, TextAreaField
from wtforms.validators import DataRequired, Email, URL

strengths_label = "I'm strong in..."
weaknesses_label = "I need help in..."

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class InfoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    contact = StringField('email', validators=[DataRequired(), Email()])
    studenttype = SelectField('High School or college?', choices=[('HS', 'High School'), ('C', 'College')],validators=[DataRequired()]) #TODO: look into having the skillist change based on this or smth

    # skillList = [('calc', 'Calculus'), ('calc2', 'Calc 2'), ('calc3', 'Calc 3'),
    #              ('chem1', 'Chem 1'), ('chem2', 'Chem 2') ] #TODO: talk to amanda about what to put here
    #
    # strengths = SelectMultipleField('areas strong in', choices=skillList)
    # weaknesses = SelectMultipleField('areas weak in', choices=skillList)
   # pfp = StringField('url to your pfp', validators=[ URL() ]) We'll do this one later


class MathForm(FlaskForm):
    sublist = [('Calculus', 'Calculus'), ('Algebra', 'Algebra'),
               ('Statistics', 'Statistics'), ('Other math', 'Other math')]
    strengths = SelectMultipleField(strengths_label, choices=sublist)
    weaknesses = SelectMultipleField(weaknesses_label, choices=sublist)


class BusinessForm(FlaskForm):
    sublist = [('Communications', 'Communications'), ('Economics', 'Economics'),
               ('Marketing', 'Marketing'), ('Management', 'Management')]
    strengths = SelectMultipleField(strengths_label, choices=sublist)
    weaknesses = SelectMultipleField(weaknesses_label, choices=sublist)


class ScienceForm(FlaskForm):
    sublist = [('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Psychology', 'Psychology')]
    strengths = SelectMultipleField(strengths_label, choices=sublist)
    weaknesses = SelectMultipleField(weaknesses_label, choices=sublist)


class EngineeringForm(FlaskForm):
    sublist = [('Architecture', 'Architecture'), ('Biomedical', 'Biomedical'), ('Chemical', 'Chemical'),
               ('Civil', 'Civil'), ('Electrical', 'Electrical'), ('Mechanical', 'Mechanical')]
    strengths = SelectMultipleField(strengths_label, choices=sublist)
    weaknesses = SelectMultipleField(weaknesses_label, choices=sublist)


class HumanitiesForm(FlaskForm):
    sublist = [('Anthropology', 'Anthropology'), ('English', 'English'),('Gender Studies', 'Gender Studies'),
               ('Philosophy', 'Philosophy'), ('History', 'History'), ('Political Science', 'Political Science'),
               ('Foreign Languages', 'Foreign Languages'), ('Pre-law', 'Pre-law')]
    strengths = SelectMultipleField(strengths_label, choices=sublist)
    weaknesses = SelectMultipleField(weaknesses_label, choices=sublist)

class ArtForm(FlaskForm):
    sublist = [('Performing', 'Performing'), ('Visual', 'Visual')]
    strengths = SelectMultipleField(strengths_label, choices=sublist)
    weaknesses = SelectMultipleField(weaknesses_label, choices=sublist)

class SetupForm(FlaskForm):
    userinfo = FormField(InfoForm)
    math = FormField(MathForm)
    business = FormField(BusinessForm)
    science = FormField(ScienceForm)
    engineering = FormField(EngineeringForm)
    humanities = FormField(HumanitiesForm)
    art = FormField(ArtForm)



class SearchForm(FlaskForm):
    uname = StringField('Username')
    math = FormField(MathForm)
    business = FormField(BusinessForm)
    science = FormField(ScienceForm)
    engineering = FormField(EngineeringForm)
    humanities = FormField(HumanitiesForm)
    art = FormField(ArtForm)


class PfpForm(FlaskForm):
    pfp = StringField('url to your pfp', validators=[DataRequired(), URL()])

class PostForm(FlaskForm):
    post = TextAreaField('Write your post here')

