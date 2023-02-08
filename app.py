from flask import render_template, request
from models import *


@app.route('/dossier/', methods=['GET'])
def patient_dossier():
    if request.args.get('patient_id'):
        patient_id = request.args.get('patient_id')
        patient_id = int(patient_id)
        patient_general_info = PatientDossier.query.filter(PatientDossier.id == patient_id).one()

        if request.args.get('info') == 'anamnesis':
            patient_anamnesis_info = PatientAnamnesis.query.filter(PatientAnamnesis.id == patient_id).one()
            complaints = PostComplaints.query.filter(PostComplaints.patient_id == patient_id)
            return render_template('anamnez.html',
                                   patient=patient_general_info,
                                   anamnesis=patient_anamnesis_info,
                                   complaints=complaints)

        elif request.args.get('info') == 'general':
            imt = (patient_general_info.weight / patient_general_info.height ** 2)*10**4 if patient_general_info.weight is not None or patient_general_info.height is not None else None
            return render_template('index.html',
                                   patient=patient_general_info,
                                   imt=f"{imt:.2f}")
    else:
        patients = PatientDossier.query.all()
        return render_template('patientslist.html',
                               patients=patients)


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/dossier/?info=general&patient_id=1
