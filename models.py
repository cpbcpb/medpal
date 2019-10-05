from app import app, db


class Medicine(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    product_ndc = db.Column(db.String(50))              #National drug code FDA
    proprietary_name = db.Column(db.String(200))
    nonproprietary_name = db.Column(db.string(1000))

    def __init__(self, medicine_id, product_ndc, proprietary_name, nonproprietary_name):

        self.id = medicine_id
        self.nonproprietary_name = nonproprietary_name
        self.product_ndc = product_ndc
        self.proprietary_name = proprietary_name

class Delivery(db.model):

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.integer, db.ForeignKey("driver.id"))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    package = db.Column(db.Integer(2000), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(2000))
    patient_comments = db.Column(db.String(2000))
    location = db.Column(db.String(120), nullable=False)


    def __init__(self, delivery_id, driver_id, patient_id, package, status, notes, patient_comments, location):

        self.id = delivery_id
        self.driver_id = driver_id
        self.patient_id = patient_id
        self.package = package
        self.status = status
        self.notes = notes
        self.patient_comments = patient_comments
        self.location = location