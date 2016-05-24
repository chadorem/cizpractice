from app import db

class GenLoc(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	sublocs = db.relationship('SubLoc', backref='general_location', lazy='dynamic')
	events = db.relationship('Event', backref='general_location', lazy='dynamic')	

	def __repr__(self):
		return '<General location %r>' % (self.name)

class SubLoc(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	gen_loc = db.Column(db.Integer, db.ForeignKey('gen_loc.id'))
	events = db.relationship('Event', backref='sublocation', lazy='dynamic')

	def __repr__(self):
		return '<Sublocation %r>' % (self.name)

class EventType(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	subtypes = db.relationship('EventSubtype', backref='general_event_type', lazy='dynamic')
	events = db.relationship('Event', backref='event_type', lazy='dynamic')

	def __repr__(self):
		return '<Event type %r>' % (self.name)

class EventSubtype(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	gen_type = db.Column(db.Integer, db.ForeignKey('event_type.id'))
	events = db.relationship('Event', backref='event_specifics', lazy='dynamic')

	def __repr__(self):
		return '<Event subtype %r>' % (self.name)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	gen_loc = db.Column(db.Integer, db.ForeignKey('gen_loc.id'))
	gen_type = db.Column(db.Integer, db.ForeignKey('event_type.id'))
	subtype = db.Column(db.Integer, db.ForeignKey('event_subtype.id'))
	subloc = db.Column(db.Integer, db.ForeignKey('sub_loc.id'))
	synopsis = db.Column(db.String(500))
	timestamp = db.Column(db.DateTime)

	def __repr__(self):
		return '<Event %r>' % (self.id)
