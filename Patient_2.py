import Models_2
import datetime

class Patient:
    def __init__(self, patient_ID):
        self.patient_ID = patient_ID
        self.name = 'lol'
        self.date_of_birth = datetime.datetime.now
        self.phone_number = ''
        self.age = 0

    def get_name(self):
        row = Models.Patient.select().where(patient_ID = self.patient_ID).get()
        return row.name

    def get_dob(self):
        row = Models.Patient.select().where(patient_ID == self.patient_ID).get()
        return row.date_of_birth.strftime('%A %B %d')

    def get_phone_number(self):
        row = Models.Patient.select().where(patient_ID = self.patient_ID).get()
        return row.phone_number

    def get_age(self):
        row = Models.Patient.select().where(patient_ID = self.patient_ID).get()
        return row.age

    @classmethod
    def create(cls, patient_ID, name, date_of_birth, phone_number, age):
        Models.Patient.add(patient_ID, name, date_of_birth, phone_number, age)

    @classmethod
    def delete(cls):
        row = Models.Patient.select().where(patient_ID == self.patient_ID).get()
        Models.Patient.delete(row)        



       
