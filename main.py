from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField
from flask_bootstrap import Bootstrap5
from forms import ContactForm


class Base(DeclarativeBase):
    pass
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_list.db'
Bootstrap5(app)
db = SQLAlchemy(model_class=Base)

db.init_app(app)

class ContactUs(db.Model):
    # __tablename__ == "contact"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    mobile: Mapped[str] = mapped_column(Integer, unique=True, nullable=False)
    message: Mapped[str] = mapped_column(String(500), nullable=True)


# with app.app_context():
#     db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_user = ContactUs(
            firstname= form.firstname.data,
            lastname= form.lastname.data,
            email= form.email.data,
            mobile= form.phone.data,
            message= form.message.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("contact.html", form=form)


@app.route('/fitness')
def fitness():
    return render_template('fitness.html')

if __name__ == "__main__":
    app.run(debug=True)