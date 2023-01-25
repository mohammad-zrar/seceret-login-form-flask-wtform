from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(message='Required field'),
                                                   Email(message="Invalid email address")])
    # Install 'email_validator' for email validation support. --> # pip install email-validator
    password = PasswordField(label='password', validators=[DataRequired(message='Required field'),
                                                           Length(min=6, message='Length must at least 8 character long')])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "hahaha"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
