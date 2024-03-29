import re

from flask_wtf import Form
from wtforms.fields import BooleanField, TextField, PasswordField, DateTimeField, IntegerField,SelectField
from wtforms.validators import EqualTo, Email, InputRequired, Length

from ..data.models import User, LogUser
from ..fields import Predicate

def email_is_available(email):
    if not email:
        return True
    return not User.find_by_email(email)

def username_is_available(username):
    if not username:
        return True
    return not User.find_by_username(username)

def safe_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^[\w]+$', s) is not None


class LogUserForm(Form):

    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')

class secti(Form):
    hodnota1 = IntegerField("vlozHodnotu1", validators=[InputRequired(message="vyzadovano")])
    hodnota2 = IntegerField("vlozHodnotu2", validators=[InputRequired(message="vyzadovano")])
class masoform(Form):
    typ=SelectField('Typ', choices=[(1, "Hovezi"), (2, "Veprove")], default=2)

class zaciForm(Form):

    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')
    trida = IntegerField('Trida', validators=[
        InputRequired(message="You can't leave this empty")
    ])


    class vstupnitestform(Form):
        Jmeno = TextField('Jmeno tesujiciho', validators=[
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
        otazka1 = IntegerField('Kolik je 3 + 3?', validators=[
        InputRequired(message="You can't leave this empty")
        ])

        otazka2 = IntegerField('', validators=[
            InputRequired(message="You can't leave this empty")
        ])
        otazka3 = TextField('Ktery predmet je nejlepsi na SSPU?', validators=[
            InputRequired(message="You can't leave this empty")
        ])


class ValidateParent(Form):
    prijmeni = TextField("prijmeni", validators=[
        InputRequired(message="Vyzadovano.")])
    pohlavi = SelectField("pohlavi", choices=[(1, "zena"),(2, "muz")],
                          default=1,validators=[InputRequired()])

class ValidateDite(Form):
    parent_id = SelectField(choices=[])
    jmeno = TextField("prijmeni", validators=[
        InputRequired(message="Vyzadovano.")])