# import models
from flask_sqlalchemy import SQLAlchemy
from tools import convert_address_to_lonlat
import nexmo
from flask import Flask, request, render_template, session, flash, redirect, url_for

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://medpal:password@localhost:3306/medpal'
app.config['SQLALCHEMY_ECHO'] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "MedPal"


# from flask_sqlalchemy import SQLAlchemy
# db=db
# db = SQLAlchemy(app)
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://medpal:password@localhost:3306/medpal'
# app.config['SQLALCHEMY_ECHO'] = True


# class Address():

#     def __init__(self, business_name, street_address1, street_address2=None, street_address3=None, 
#                 city=None, state=None, zip_code=None, country=None, active=False, verified=False, start_date=None, end_date=None):
#         self.street_address1 = street_address1
#         self.street_address2 = street_address2
#         self.street_address3 = street_address3
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code
#         self.country = country

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
    driver_id = db.Column(db.Integer)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    package = db.Column(db.String(2000), nullable=False)
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
    store_manager_id = db.Column(db.Integer)
    customers = db.relationship('Patient', backref='patient')
    #no orders DB
    #orders = db.relationship('Order', backref='order')
    #no driver DB
    #deliveries = db.relationship('Delivery', backref='driver')

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
    
    #deliveries = db.relationship("Delivery", backref="patient_id")
    
 
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
        #self.location = convert_address_to_lonlat(self.location)


client = nexmo.Client(key='7d3b3494', secret='vMF3mb7GNxMMDt9s')

risk_levels = ["None", "Low", "Medium", "High"]

@app.route('/', methods=["GET"])
def index():
    
    # client.send_message({
    #     'from': '15859357147',
    #     'to': '18134849281',
    #     'text': 'Hello from Nexmo',
    # })

    return render_template("base2.html")

@app.route('/signup', methods=["GET"])
def signup():

    return 'SIGNUP VIEW (This is not necessary)'

@app.route('/patient/signup', methods=["POST"])
def patient_signup():

    if request.method == "POST":

        name = request.form['name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        meds = request.form['meds']
        risk_assessment = request.form['risk_assessment']
        created_date = request.form['created_date']
        pharmacy = request.form['pharmacy']
        last_filled = request.form['last_filled']
        last_filled_amount = request.form['last_filled_amount']
        dob = request.form["dob"]
        insurance = request.form['insurance']
        group_no = request.form['group_no']
        ss_no = request.form['ss_no']
        Rx_no = request.form['Rx_no']
        chronic_conditions = request.form['chronic_conditions']
        allergies = request.form['allergies']
        cell_phone = request.form['cell_phone']
        gender = request.form['gender']

        new_patient = Patient(name=name,
            last_name=last_name,
            phone=phone,
            email=email,
            address=address,
            meds=meds,
            risk_assessment=risk_assessment,
            created_date=created_date,
            pharmacy=pharmacy,
            last_filled=last_filled,
            last_filled_amount=last_filled_amount,
            dob=dob,
            insurance=insurance,
            group_no=group_no,
            ss_no=ss_no,
            Rx_no=Rx_no,
            chronic_conditions=chronic_conditions,
            allergies=allergies,
            cell_phone=cell_phone,
            gender=gender)

        db.session.add(new_patient)
        db.session.commit()
    return 'SIGNUP VIEW (This is not necessary)'

@app.route('/pharmacy', methods=["GET"])
def pharmacy():

    return 'PHARMACY VIEW'

@app.route('/pharmacy/signup', methods=["POST" ])
def pharmacy_signup():

    if request.method == "POST":

        business_name = request.form["name"]
        street_address1 = request.form['street_address1']
        street_address2 = request.form['street_address2']
        street_address3 = request.form['street_address3']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        country = request.form['country']
        active = request.form['active']
        verified = request.form['verified']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        # store_manager_id = request.form['store_manager_id']

        new_pharmacy = Pharmacy(business_name=business_name, 
            street_address1=street_address1, 
            street_address2=street_address2,            
            street_address3=street_address3,
            city=city,
            state=state, 
            zip_code=zip_code, 
            country=country, 
            active=active, 
            verified=verified,
            start_date=start_date,
            end_date=end_date,
            )
        db.session.add(new_pharmacy)
        db.session.commit()
        #render template pharmacy view with added verification message

        return 'PHARMACY VIEW'

@app.route('/delivery/map', methods=["GET"])
def map():
    return 'DELIVERY MAP VIEW'

@app.route('/delivery/deliver', methods=["GET"])
def deliver():
    return 'DELIVERY CONFIRMATION VIEW'

@app.route('/message-response', methods=["GET"])
def message_response():
    patient = Patient.query.filter_by(id=1).first()
    # new_delivery = Delivery(
    #     id=1, 
    #     driver_id=street_address1, 
    #     patient_id=street_address2,            
    #     package=street_address3,
    #     status=city,
    #     notes=state, 
    #     patient_comments=zip_code, 
    #     location=country
    # )
    return "Name: "+str(patient.name)

@app.route("/risk", methods=['GET', 'POST'])
@app.route("/risk/<int:patientid>/<curr_assessment>")
def set_risk(patientid=None, curr_assessment=None):
    risk_error = ""
    session['patientid'] = 1
    if "patientid" in session:
        patientid = session['patientid']
    else:
        flash("Patient not specified")
        return redirect(url_for("error"))

    patient = Patient.query.filter_by(id=patientid).first()

    if patientid and curr_assessment:
        if patient.id == patientid and curr_assessment in risk_levels:
            db.session.query(Patient).filter(Patient.id == patientid).update({'risk_assessment': curr_assessment})
            db.session.commit()


    if not patient:
        flash("Patient not found")
        return redirect(url_for("error"))

    if request.method == 'POST':        
        curr_assessment = request.form['risk']

        if not curr_assessment or curr_assessment.strip() == "":
            risk_error = "Please select a risk level"
        else:
            db.session.query(Patient).filter(Patient.id == patientid).update({'risk_assessment': curr_assessment})
            db.session.commit()

    return render_template("curr_assessment.html", patient=patient, risk_levels=risk_levels, risk_error=risk_error)



@app.route("/error")
def error():
    return render_template("base_for_risk.html")

if __name__ == '__main__':
    app.run()