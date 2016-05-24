from flask import render_template
from app import app, db
from forms import EventForm

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html', title='Home')


@app.route('/index/blotter/')
def blotter():
	return render_template('blotter.html', title='Live Feed')

@app.route('/index/submit/')
def submit():
	form = EventForm()
	return render_template('submit.html', title='Event Submission')
