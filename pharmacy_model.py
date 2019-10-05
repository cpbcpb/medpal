from app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#db = SQLAlchemy(app)

class Pharmacy(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(200), nullable=False)
    street_address1 = db.Column(db.String(200), nullable=False)
    street_address2 = db.Column(db.String(200), nullable=True)
    street_address3 = db.Column(db.String(200), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zip_code = db.Column(db.String(20), nullable=True)
    country = db.Column(db.String(100), default="USA")
    active = db.Column(db.Boolean)
    verified = db.Column(db.Boolean)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    store_manager_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customers = db.relationship('Customer', backref='customer')
    orders = db.relationship('Order', backref='order')
    deliveries = db.relationship('Delivery', backref='driver')

    def __init__(self, business_name, street_address1, street_address2=None, street_address3=None, 
                city=None, state=None, zip_code=None, country=None, active=False, verified=False, start_date=None, end_date=None):
        self.business_name = business_name
        self.street_address1 = street_address1
        self.street_address2 = street_address2
        self.street_address3 = street_address3
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.active = active
        self.verified = verified
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return "<Driver object: ID: {id} | First Name: {first_name} | Last Name: {last_name} | Active: {active} | Verified: {verified}>".format(
                    id=self.id, first_name=self.first_name, last_name=self.last_name, active=self.active, verified=self.verified)
