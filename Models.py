from peewee import *
import datatime

class Personnel(Model):
    personnel_ID = CharField(max_length=16, unique=True)
    name = TextField(max_length=25)
    sector = TextField()
    user_id = CharField(max_length=10, unique=True)
    user_pass = CharField(max_length=16)
    
    class Meta:
        database = 'Personnel'


class Patient(Model):
    patient_ID = CharField(max_length=16, unique=True)
    name = TextField(max_length=15)
    date_of_birth = DateTimeField()
    phone_number = TextField()

    class Meta:
        database = 'Patient'


class Appointment(Model):
    appointment_ID = CharField(max_length=16, unique=True)
    data = DateTimeField(default=datetime.datetime.now)
    patient_ID = ForeignKeyField(Patient, related_name='appointed')
    personnel_ID = ForeignKeyField(Personnel, related_name='supervise')    
    prescription_ID = ForeignField(Prescription)    
    service_charge = IntegerField(default=0)

    class Meta:
        database = 'Appointment'


class Medicine(Model):
    medicine_ID =CharField()
    medicine_name = TextField()
    amount = IntegerField()

    class Meta:
        database = 'Medicine'


class Prescription(Model):
    prescription_ID = CharField(max_length=20, unique=True)
    medicine_ID = ForeignKeyField(Medicine)
    personnel_ID = ForeignKeyField(Personnel)
    dosage = TextField()

    
    
    
    
