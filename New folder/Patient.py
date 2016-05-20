import Models
import datetime

class Patient:
    def __init__(self, username):
        self.username = username

    def get_patient_ID(self):
        row = Models.Patient.select().where(Models.Patient.user_id == self.username).get()
        return row.patient_ID

    def get_name(self):
        row = Models.Patient.select().where(Models.Patient.user_id == self.patient_ID).get()
        return row.name

    def get_dob(self):
        row = Models.Patient.select().where(Models.Patient.user_id == self.patient_ID).get()
        return row.date_of_birth.strftime('%A %B %d')

    def get_phone_number(self):
        row = Models.Patient.select().where(Models.Patient.user_id == self.patient_ID).get()
        return row.phone_number

    def get_age(self):
        row = Models.Patient.select().where(Models.Patient.user_id == self.patient_ID).get()
        return row.age

    def get_user_id(self, patient_ID):
        row = Models.Patient.select().where(Models.Patient.patient_ID == patient_ID).get()
        return row.user_id

    def get_user_pass(self):
        row = Models.Patient.select().where(Models.Patient.user_id == self.username).get()
        return row.user_pass

    def val_user_id(self):
        try:
            user = Models.Patient.get(Models.Patient.user_id == self.username)
        except Models.DoesNotExist:
            return False
        else:
            return True

    def val_user_pass(self, password):
        pw = get_user_pass()
        if str(pw) == password:
            return True
        else:
            return False

    def send_req_detail(self, detail):
        Models.Reqdetail.add(self.patient_ID, datetime.datetime.now, detail, department)

    @classmethod
    def create(cls, patient_ID, name, date_of_birth, phone_number, age, user_id, user_pass):
        Models.Patient.add(patient_ID, name, date_of_birth, phone_number, age, user_pass, user_pass)

    @classmethod
    def delete(cls, patient_ID):
        row = Models.Patient.select().where(patient_ID == patient_ID).get()
        Models.Patient.delete(row)        



       
