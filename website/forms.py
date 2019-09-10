from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp, Email

class CheckForm(FlaskForm):
    code = StringField("Course Code", validators = [DataRequired(), Regexp("\d+")])
    submit_code = SubmitField("Find Class")
    

class EmailForm(FlaskForm):
    email = StringField("Enter your email here:", validators = [DataRequired(), Email()])
    submit_email = SubmitField("Send me a notification email when the class is OPEN")


class UserForm(FlaskForm):
    email = StringField("Enter your email here:", validators = [DataRequired(), Email()])
    submit_email = SubmitField("Find Registered Classes")


class DropForm(FlaskForm):
    code = StringField("Course Code", validators = [DataRequired(), Regexp("\d+")])
    submit_code = SubmitField("Stop tracking this course")
