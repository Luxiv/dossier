from flask import render_template, request, abort, redirect, url_for
from datetime import datetime

from models import *


@app.route('/dossier/', methods=['GET'])  # оприділяємо url по якій буде відкриватися додаток
def patient_dossier():
    if request.args.get(
            'patient_id'):  # в юрл передається аргумент patient_id що визначає на сторінку якого пацієнта ти попадаєш
        patient_id = request.args.get('patient_id')  # тут ми хапаємо patient_id з урли виглядає так: patient_id=1
        patient_id = int(patient_id)  # переводимо його у потрібний тип данних
        patient_general_info = PatientDossier.query.filter(
            PatientDossier.id == patient_id).one()  # витягуємо з БД всі дані об"єкта PatientDossier фільтруючи всіх пацієнтів по його айді

        if request.args.get('info') == 'anamnesis':  # аргумент info=anamnesis в урлі перекидає на вкладку анамнез
            patient_anamnesis_info = PatientAnamnesis.query.filter(
                PatientAnamnesis.id == patient_id).one()  # аналогічним чином фільтруємо пацієнтів по айдішці і витягуємо всі данні обєкта анамнез для цього пацієнта
            #  complaints - скарги
            complaints = PostComplaints.query.filter(
                PostComplaints.patient_id == patient_id)  # оскільки в об"єкта пацієнт, може бути багато скарг фільтруємо скарги по стовпцю patient_id
            return render_template('anamnez.html',
                                   # повертаємо рендер anamnez.html де дані пацієнта вже передані в потрібні поля
                                   patient=patient_general_info,
                                   # ці три строчки передають в anamnez.html динамічні дані з БД
                                   anamnesis=patient_anamnesis_info,
                                   complaints=complaints)

        elif request.args.get('info') == 'general':  # аргумент info=general в урлі перекидає на вкладку Общеее
            imt = (
                              patient_general_info.weight / patient_general_info.height ** 2) * 10 ** 4 if patient_general_info.weight is not None or patient_general_info.height is not None else None
            # тут рахуємо імт (поки розрахунок не бере до уваги стать, поправимо це коли будемо відшліфовути додаток )
            return render_template('index.html',  # повертаємо рендер index.html з даними  з БД
                                   patient=patient_general_info,
                                   imt=f"{imt:.2f}")
    else:  # якщо в лінку не переданий жодний аргумент то повертається список пацієнтів з бд
        patients = PatientDossier.query.all()  # витягуємо всіх пацієнтів з бд
        return render_template('patientslist.html',  # тут всьо і так понятно)
                               patients=patients)


@app.route('/add_patient/', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        try:
            pat = PatientDossier(
                name_surname=request.form['name'],
                price=request.form['price'],
                birth_day=datetime.strptime(request.form['birth date'], "%Y-%m-%d"),
                weight=request.form['weight'],
                height=request.form['height'],
                phone_number=request.form['phone'],
                address=request.form['address'],
                job=request.form['job'],
                interests=request.form['interests'],
                loads_chair=True if request.form.get('radio-p-a-chair') == 'on' else False,
                loads_walk=True if request.form.get('radio-p-a-walk') == 'on' else False,
                loads_barbell=True if request.form.get('radio-p-a-barbell') == 'on' else False,
                visits=0,
                course=0,
                non_appearance=0,
                cancellations=0,
                desired_frequency=0

            )
            db.session.add(pat)
            db.session.flush()

            anamnesis = PatientAnamnesis(
                id=pat.id,
                procedure_features=request.form['procedure_features'],
                diagnosis=request.form['diagnosis'],
                comorbidities=request.form['comorbidities'],
                pre_complaints=request.form['pre_complaints']
            )
            db.session.add(anamnesis)
            db.session.commit()
            patient_id = pat.id
            return redirect(url_for('patient_dossier', info='general', patient_id=patient_id))
        except KeyError as e:
            db.session.rollback()
            error_msg = f"KeyError: {str(e)}"
            return abort(400, description=f"Bad Request, \n {error_msg}")
        except Exception as e:
            db.session.rollback()
            error_msg = f"Error: {str(e)}"
            raise Exception(f'Patient registration error \n {error_msg}')


    return render_template('add_edit.html')


if __name__ == '__main__':  # якщо ми запустимо поточний файл через IDE або через термінал, наступним чином:
    #  1) перейти в дерикторію з поточним файлом  2) запустити команду: python app.py
    # запуститься локальний сервер де можна поцикати додаток, щоб це зробити треба перейти по урлі знизу
    app.run(debug=True)

# http://127.0.0.1:5000/dossier/?info=general&patient_id=1
