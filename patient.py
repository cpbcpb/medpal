from flask import Flask, request, session, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from app import app, db

class Patient:
    def __init__(self, id, name, risk):
        self.id = id
        self.name = name
        self.risk = risk

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "MedPal"

risk_levels = ["None", "Low", "Medium", "High"]

patient = Patient(1234, "Jane Doe", "Low")

@app.route("/risk", methods=['GET', 'POST'])
@app.route("/risk/<int:patientid>/<curr_risk>")
def set_risk(patientid=None, curr_risk=None):
    risk_error = ""

    # if "patientid" in session:
    #     patientid = session['patientid']
    # else:
    #     flash("Patient not specified")
    #     return redirect(url_for("error"))

    #patient = Patient.query.filter_by(patientid=patientid).first()

    if patientid and curr_risk:
        if patient.id == patientid and curr_risk in risk_levels:
            patient.risk = curr_risk


    if not patient:
        flash("Patient not found")
        return redirect(url_for("error"))

    if request.method == 'POST':        
        risk = request.form['risk']

        if not risk or risk.strip() == "":
            risk_error = "Please select a risk level"
        else:
            #session.query(Patient).filter(Patient.id == patientid).update({'risk_assessment': risk})
            patient.risk = risk

    return render_template("curr_risk.html", patient=patient, risk_levels=risk_levels, risk_error=risk_error)



@app.route("/error")
def error():
    return "Error"

app.run()