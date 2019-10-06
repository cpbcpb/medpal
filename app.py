from flask import Flask, request, render_template, session, flash, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from models import Pharmacy, Patient

from flask import Flask
import nexmo

client = nexmo.Client(key='7d3b3494', secret='vMF3mb7GNxMMDt9s')

app = Flask(__name__)
# db = SQLAlchemy(app)

# app.secret_key = "MedPal"

# risk_levels = ["None", "Low", "Medium", "High"]


@app.route('/', methods=["GET"])
def index():
    client.send_message({
        'from': '15859357147',
        'to': '18134849281',
        'text': 'Hello from Nexmo',
    })
    return 'HOMEPAGE AND LOGIN (Doesnt need to be extravagant'

@app.route('/', methods=["GET"])
def index():
    return render_template('map2.html')

@app.route('/signup', methods=["GET"])
def signup():
    return 'SIGNUP VIEW (This is not necessary)'

# @app.route('/patient/signup', methods=["POST"])
# def patient_signup():

#     if request.method == "POST":

#         name = request.form['name']
#         last_name = request.form['last_name']
#         phone = request.form['phone']
#         email = request.form['email']
#         address = request.form['address']
#         meds = request.form['meds']
#         risk_assessment = request.form['risk_assessment']
#         created_date = request.form['created_date']
#         pharmacy = request.form['pharmacy']
#         last_filled = request.form['last_filled']
#         last_filled_amount = request.form['last_filled_amount']
#         dob = request.form["dob"]
#         insurance = request.form['insurance']
#         group_no = request.form['group_no']
#         ss_no = request.form['ss_no']
#         Rx_no = request.form['Rx_no']
#         chronic_conditions = request.form['chronic_conditions']
#         allergies = request.form['allergies']
#         cell_phone = request.form['cell_phone']
#         gender = request.form['gender']

#         new_patient = Patient(name=name,
#             last_name=last_name,
#             phone=phone,
#             email=email,
#             address=address,
#             meds=meds,
#             risk_assessment=risk_assessment,
#             created_date=created_date,
#             pharmacy=pharmacy,
#             last_filled=last_filled,
#             last_filled_amount=last_filled_amount,
#             dob=dob,
#             insurance=insurance,
#             group_no=group_no,
#             ss_no=ss_no,
#             Rx_no=Rx_no,
#             chronic_conditions=chronic_conditions,
#             allergies=allergies,
#             cell_phone=cell_phone,
#             gender=gender)

#         db.session.add(new_patient)
#         db.session.commit()
#     return 'SIGNUP VIEW (This is not necessary)'

# @app.route('/pharmacy', methods=["GET"])
# def pharmacy():

#     return 'PHARMACY VIEW'

# @app.route('/pharmacy/signup', methods=["POST" ])
# def pharmacy_signup():

#     if request.method == "POST":

#         business_name = request.form["name"]
#         street_address1 = request.form['street_address1']
#         street_address2 = request.form['street_address2']
#         street_address3 = request.form['street_address3']
#         city = request.form['city']
#         state = request.form['state']
#         zip_code = request.form['zip_code']
#         country = request.form['country']
#         active = request.form['active']
#         verified = request.form['verified']
#         start_date = request.form['start_date']
#         end_date = request.form['end_date']
#         # store_manager_id = request.form['store_manager_id']

#         new_pharmacy = Pharmacy(business_name=business_name, 
#             street_address1=street_address1, 
#             street_address2=street_address2,            
#             street_address3=street_address3,
#             city=city,
#             state=state, 
#             zip_code=zip_code, 
#             country=country, 
#             active=active, 
#             verified=verified,
#             start_date=start_date,
#             end_date=end_date,
#             )
#         db.session.add(new_pharmacy)
#         db.session.commit()
#         #render template pharmacy view with added verification message

#         return 'PHARMACY VIEW'

# @app.route('/delivery/map', methods=["GET"])
# def map():
#     return 'DELIVERY MAP VIEW'

# @app.route('/delivery/deliver', methods=["GET"])
# def deliver():
#     return 'DELIVERY CONFIRMATION VIEW'


# @app.route("/risk", methods=['GET', 'POST'])
# @app.route("/risk/<int:patientid>/<curr_assessment>")
# def set_risk(patientid=None, curr_assessment=None):
#     risk_error = ""

#     if "patientid" in session:
#         patientid = session['patientid']
#     else:
#         flash("Patient not specified")
#         return redirect(url_for("error"))

#     patient = Patient.query.filter_by(id=patientid).first()

#     if patientid and curr_assessment:
#         if patient.id == patientid and curr_assessment in risk_levels:
#             db.session.query(Patient).filter(Patient.id == patientid).update({'risk_assessment': curr_assessment})
#             db.session.commit()


#     if not patient:
#         flash("Patient not found")
#         return redirect(url_for("error"))

#     if request.method == 'POST':        
#         curr_assessment = request.form['risk']

#         if not curr_assessment or curr_assessment.strip() == "":
#             risk_error = "Please select a risk level"
#         else:
#             db.session.query(Patient).filter(Patient.id == patientid).update({'risk_assessment': curr_assessment})
#             db.session.commit()

#     return render_template("curr_assessment.html", patient=patient, risk_levels=risk_levels, risk_error=risk_error)



@app.route("/error")
def error():
    return "Error"

if __name__ == "__main__":
    app.run(debug=True)