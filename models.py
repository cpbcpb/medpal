import app
from tools import convert_address_to_lonlat
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)



class Address():

    def __init__(self, business_name, street_address1, street_address2=None, street_address3=None, 
                city=None, state=None, zip_code=None, country=None, active=False, verified=False, start_date=None, end_date=None):
        self.street_address1 = street_address1
        self.street_address2 = street_address2
        self.street_address3 = street_address3
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

class Medicine(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    product_ndc = db.Column(db.String(50))              #National drug code FDA
    proprietary_name = db.Column(db.String(200))
    nonproprietary_name = db.Column(db.String(1000))
    date_added = db.Column(db.DateTime)

    def __init__(self, medicine_id, product_ndc, proprietary_name, nonproprietary_name, date_added):

        self.id = medicine_id
        self.nonproprietary_name = nonproprietary_name
        self.product_ndc = product_ndc
        self.proprietary_name = proprietary_name

class Delivery(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.integer, db.ForeignKey("driver.id"))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    package = db.Column(db.Integer(2000), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(2000))
    patient_comments = db.Column(db.String(2000))
    location = db.Column(db.String(120), nullable=False)


    def __init__(self, driver_id, patient_id, package, status, notes, patient_comments, location):

        #self.id = delivery_id
        self.driver_id = driver_id
        self.patient_id = patient_id
        self.package = package
        self.status = status
        self.notes = notes
        self.patient_comments = patient_comments
        self.location = location


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
    customers = db.relationship('Patients', backref='patient')
    #no orders DB
    orders = db.relationship('Order', backref='order')
    #no driver DB
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

class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    address = db.Column(db.String(1000), nullable=False)
    meds = db.Column(db.String(3000))
    risk_assessment = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    pharmacy = db.Column(db.Integer, db.ForeignKey(Pharmacy.id), nullable=False)
    last_filled = db.Column(db.DateTime)
    last_filled_amount = db.Column(db.Float)
    dob = db.Column(db.DateTime, nullable=False)
    insurance = db.Column(db.String(120))
    group_no = db.Column(db.String(120))
    ss_no = db.Column(db.String(120))
    Rx_no = db.Column(db.String(120))
    chronic_conditions = db.Column(db.String(2000))
    allergies = db.Column(db.String(2000))
    cell_phone = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    location = db.Column(db.String(200))
    
    deliveries = db.relationship("Delivery", backref="patient_id")
    
 
    def __init__(self, name, last_name, phone, email, address, meds, risk_assessment, created_date, pharmacy, last_filled, last_filled_amount, dob, insurance, group_no, ss_no, Rx_no, chronic_conditions, allergies, cell_phone, gender):

        
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.meds = meds
        # self.status = status
        self.risk_assessment = risk_assessment
        self.created_date = created_date
        self.pharmacy = pharmacy
        self.last_filled = last_name
        self.last_filled_amount = last_filled_amount
        self.dob = dob
        self.allergies = allergies
        self.group_no = group_no
        self.ss_no = ss_no
        self.chronic_conditions = chronic_conditions
        self.Rx_no = Rx_no
        self.location = convert_address_to_lonlat(self.location)
