from peewee import *
import datetime


class Personnel(Model):
    personnel_ID = CharField(max_length=16, unique=True)
    name = TextField()
    sector = TextField()
    user_id = CharField(max_length=10, unique=True)
    user_pass = CharField(max_length=16)


class Patient(Model):
    patient_ID = CharField(max_length=16, unique=True)
    name = TextField()
    date_of_birth = DateTimeField()
    phone_number = TextField()


class Medicine(Model):
    medicine_ID =CharField()
    medicine_name = TextField()
    amount = IntegerField()


class Prescription(Model):
    prescription_ID = CharField(max_length=20, unique=True)
    medicine_ID = ForeignKeyField(Medicine)
    personnel_ID = ForeignKeyField(Personnel)
    dosage = TextField()
    

class Appointment(Model):
    appointment_ID = CharField(max_length=16, unique=True)
    data = DateTimeField(default=datetime.datetime.now)
    patient_ID = ForeignKeyField(Patient, related_name='appointed')
    personnel_ID = ForeignKeyField(Personnel, related_name='supervise')    
    prescription_ID = ForeignKeyField(Prescription)    
    service_charge = FloatField(default=0)


class Medicine(Model):
    medicine_ID =CharField()
    medicine_name = TextField()
    amount = IntegerField()



    
    
    
    
