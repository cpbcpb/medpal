from main import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#db = SQLAlchemy(app)

class Driver(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean)
    verified = db.Column(db.Boolean)
    start_date = db.Column(db.DateTime)
    termination_date = db.Column(db.DateTime)
    deliveries = db.relationship('Delivery', backref='driver')

    def __init__(self, first_name, last_name, email, password, active=False, verified=False, start_date=None, termination_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = active
        self.verified = verified
        self.start_date = start_date
        self.termination_date = termination_date

    def __repr__(self):
        return "<Driver object: ID: {id} | First Name: {first_name} | Last Name: {last_name} | Active: {active} | Verified: {verified}>".format(
                    id=self.id, first_name=self.first_name, last_name=self.last_name, active=self.active, verified=self.verified)
