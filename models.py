from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask import Flask


#  Нижче ініціалізуємо додаток і оприділяємо конфігурацію БД (зараз ми використовуємо бд sqlite, тут може бути конфіг для постгрес і такого іншого)
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dossier.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class PatientDossier(db.Model):  # творюємо обєкт PatientDossier з даними що ми бачимо в вкладці Общее
    __tablename__      = 'patient_general'  # внутрішня назва таблиці в бд
    # оприділяємо всі стовпці з даними по обєкту PatientDossier(тіпа всі дані зі сторінки Общее)
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

    def __init__(self, name, phone_number):  #  це теж внутрішнє тобі не треба. Коли в коді викликається обєкт PatientDossier без визначення конкретних полів то повертається ім"я і телефон пацієнта по якому був запит
        self.name = name
        self.phone_number = phone_number


class PatientAnamnesis(db.Model):  # класс анамнез де описуються данні анамнезу
    __tablename__        = 'patient_anamnesis'
    # напряму зв"яуємо айдішнік классу PatientAnamnesis і PatientDossier
    id                   = db.Column(db.Integer, ForeignKey('patient_general.id'), primary_key=True)
    procedure_features   = db.Column(db.String(300))  #  Особенности проведения процедуры
    diagnosis            = db.Column(db.String(300))  #  Диагноз
    comorbidities        = db.Column(db.String(300))  #  Сопутствующие заболевания
    pre_complaints       = db.Column(db.String(300))  #  Жалобы до першого сеансу


class PostComplaints(db.Model):  # Скарги що виникли протягом терапії назвемо їх постскарги/постжалобы
    __tablename__        = 'complaints'
    id                   = db.Column(db.Integer, primary_key=True)  # у кожної постскарги буде унікальний айді
    #  оскільки в пацієнта може бути багато постскарг (а може і не бути зовсім) прив"язуємо кожну з них до конкретного пацієнта полем patient_id
    patient_id           = db.Column(db.Integer, db.ForeignKey('patient_general.id'), nullable=False)
    post_complaints      = db.Column(db.String(300))  #  текст постскарги
    post_complaint_date  = db.Column(db.DateTime)  #  дата постскарги


if __name__ == '__main__':  # Наступні 3 строчки потрібні щоб згенерувати базуданих по правилах що передані вище!
    with app.app_context():
        db.create_all()
