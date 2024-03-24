from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired
class ContactForm(FlaskForm):
    firstname = StringField(label="First Name", validators=[DataRequired()])
    lastname = StringField(label="Last Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired()])
    phone = IntegerField(label="Contact Number", validators=[DataRequired()])
    message = CKEditorField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label="Submit")