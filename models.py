from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask import Flask

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dossier.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class PatientDossier(db.Model):
    __tablename__      = 'patient_general'
    id                 = db.Column(db.Integer(), primary_key=True)
    name_surname       = db.Column(db.String(100), unique=True)
    price              = db.Column(db.Integer())
    birth_day          = db.Column(db.DateTime)
    weight             = db.Column(db.Integer())
    height             = db.Column(db.Integer())
    phone_number       = db.Column(db.Integer())
    address            = db.Column(db.String(100))
    job                = db.Column(db.String(100))
    interests          = db.Column(db.String(200))
    visits             = db.Column(db.Integer())
    course             = db.Column(db.Integer())
    non_appearance     = db.Column(db.Integer())
    cancellations      = db.Column(db.Integer())
    desired_frequency  = db.Column(db.Integer())

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class PatientAnamnesis(db.Model):
    __tablename__        = 'patient_anamnesis'
    id                   = db.Column(db.Integer, ForeignKey('patient_general.id'), primary_key=True)
    procedure_features   = db.Column(db.String(300))
    diagnosis            = db.Column(db.String(300))
    comorbidities        = db.Column(db.String(300))
    pre_complaints       = db.Column(db.String(300))


class PostComplaints(db.Model):
    __tablename__        = 'complaints'
    id                   = db.Column(db.Integer, primary_key=True)
    patient_id           = db.Column(db.Integer, db.ForeignKey('patient_general.id'), nullable=False)
    post_complaints      = db.Column(db.String(300))
    post_complaint_date  = db.Column(db.DateTime)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
