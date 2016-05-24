from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateTimeField
from wtforms.validators import DataRequired

class EventForm(Form):
	datetime = DateTimeField('date and time', validators=[DataRequired()])

