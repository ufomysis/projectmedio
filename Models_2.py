import datetime
import Appointment as appt
import Medicine as medic
from peewee import *
import Personnel as person
import Patient as pat
DATABASE = SqliteDatabase('hospital.db')

class Personnel(Model):
    personnel_ID = CharField(max_length=16, unique=True)
    name = TextField()
    sector = TextField()
    user_id = CharField(unique=True)
    user_pass = CharField(max_length=100)

    class Meta:
        database  = DATABASE
        order_by = ('-personnel_ID',)        

        
    @classmethod
    def add(cls, personnel_ID, name, sector, user_id, user_pass):
        try:            
            cls.create(
                    personnel_ID=personnel_ID,
                    name=name,
                    sector=sector,
                    user_id=user_id,
                    user_pass=user_pass)
        except IntegrityError:
            personnel_tmp = Personnel.get(personnel_ID=personnel_ID)                     
            personnel_tmp.name = name
            personnel_tmp.sector = sector
            personnel_tmp.user_id = user_id
            personnel_tmp.user_pass = user_pass
            personnel_tmp.save()

    @classmethod
    def delete(cls, user):
        user.delete_instance()


class Patient(Model):
    patient_ID = CharField(max_length=16, unique=True)
    name = TextField()
    date_of_birth = DateTimeField()
    phone_number = TextField()
    age = IntegerField()
    user_id = CharField()
    user_pass = CharField()
    class Meta:
        database  = DATABASE
        order_by = ('-patient_ID',)  


    @classmethod
    def add(cls, patient_ID, name, date_of_birth, phone_number, age,user_id,user_pass):
        try:            
            cls.create(
                    patient_ID=patient_ID,
                    name=name,
                    date_of_birth=date_of_birth,
                    phone_number=phone_number,
                    age = age,
                    user_id = user_id,
                    user_pass = user_pass)
        except IntegrityError:            
            patient_tmp = Patient.get(patient_ID=patient_ID)
            patient_tmp.name = name
            patient_tmp.date_of_birth = date_of_birth
            patient_tmp.phone_number = phone_number
            patient_tmp.age = age
            patient_tmp.save()

    @classmethod
    def delete(cls, user):
        user.delete_instance()


class Medicine(Model):
    medicine_ID = CharField(unique=True)
    medicine_name = TextField()
    amount = IntegerField()
    price = FloatField()

    class Meta:
        database = DATABASE
        order_by = ('-medicine_name',)
        

    @classmethod
    def add(cls, medicine_ID, medicine_name, amount):
        try:            
            cls.create(
                    medicine_ID=medicine_ID,
                    medicine_name=medicine_name,
                    amount=amount)            
        except IntegrityError:
            medicine_tmp = Medicine.get(medicine_ID = medicine_ID)
            medicine_tmp.medicine_name = medicine_name
            medicine_tmp.amount = amount
            medicine_tmp.save()

    @classmethod
    def delete(cls, medicine):
        medicine.delete_instance()
        

class Prescription(Model):
    prescription_ID = CharField(unique=True)
    medicine_ID_fk = ForeignKeyField(Medicine)
    personnel_ID_fk = ForeignKeyField(Personnel)    
    dosage = TextField()


    class Meta:
        database = DATABASE
        order_by = ('-prescription_ID',)
        
    @classmethod
    def add(cls, prescription_ID, medicine_ID, personnel_ID, dosage):
        try:            
            cls.create(
                    prescription_ID=prescription_ID,
                    medicine_ID_fk=medicine_ID_fk,
                    personnel_ID=personnel_ID,
                    dosage=dosage)            
        except IntegrityError:
            pres_tmp = Prescription.get(prescription_ID = prescription_ID)
            pres_tmp.medicine_ID_fk = medicine_ID_fk
            pres_tmp.personnel_ID_fk = personnel_ID_fk
            pres_tmp.dosage = dosage
            pres_tmp.save()
            

    @classmethod
    def delete(cls, prescription):
        prescription.delete_instance()
    

class Appointment(Model):
    appointment_ID = CharField(unique=True)
    date = DateTimeField(default=datetime.datetime.now)
    patient_ID_fk = ForeignKeyField(Patient)
    personnel_ID_fk = ForeignKeyField(Personnel)    
    prescription_ID_fk = ForeignKeyField(Prescription)    
    service_charge = FloatField(default=0)
    lab_result = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-date',)
        
    @classmethod
    def add(cls, appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge, lab_result):
        try:            
            cls.create(
                    appointment_ID=appointment_ID,
                    date=date,
                    patient_ID_fk=patient_ID,
                    personnel_ID_fk=personnel_ID,
                    prescription_ID_fk=prescription_ID,
                    service_charge=service_charge,
                    lab_result=lab_result)           
        except IntegrityError:
            app_tmp = Appointment.get(appointment_ID = appointment_ID)
            app_tmp.date = date
            app_tmp.patient_ID_fk = patient_ID
            app_tmp.personnel_ID_fk = personnel_ID
            app_tmp.prescription_ID_fk = prescription_ID
            app_tmp.service_charge = service_charge
            app_tmp.save()
            

    @classmethod
    def delete(cls, appointment):
        appointment.delete_instance()

    def get_date(self):
        row = Appointment.select().where(Appointment.appointment_ID == self.appointment_ID).get()
        return row.date.strftime('%A %B %d, %Y %I:%M%p')

    def get_patient(self):
        row = Appointment.select(Appointment, Patient).join(Patient).where(Appointment.appointment_ID == self.appointment_ID).get()
        return row.patient_ID_fk.name

    def get_personnel(self):
        row = Appointment.select(Appointment, Personnel).join(Personnel).where(Appointment.appointment_ID == self.appointment_ID).get()
        return row.personnel_ID_fk.name

    def get_service_charge(self):
        row = Appointment.select().where(Appointment.appointment_ID == self.appointment_ID).get()
        return row.service_charge

    def get_lab_result(self):
        row = Appointment.select().where(Appointment.appointment_ID == self.appointment_ID).get()
        return row.lab_result
class Room(Model):
    room_num = CharField()
    room_type = CharField()

    class Meta:
        database = DATABASE
        order_by = ('-room_num',)
        
    @classmethod
    def add(cls, room_num, room_type):
        try:            
            cls.create(
                    room_num=room_num,
                    room_type=room_type)
            
        except IntegrityError:
            room_tmp = Room.get(room_num = room_num)
            room_tmp.room_type = room_type           
            room_type.save()
            
    @classmethod
    def delete(cls, room):
        room.delete_instance()

class Roomuse(Model):
    room_num_fk = ForeignKeyField(Room, related_name='used')
    personnel_ID_fk = ForeignKeyField(Personnel, related_name='uses')
    use_time = DateTimeField()
    leave_time = DateTimeField()

    class Meta:
        database = DATABASE
        order_by = ('-room_num_fk',)
        
    @classmethod
    def add(cls, room_num_fk, personnel_ID, use_time, leave_time):
        try:            
            cls.create(
                    room_num_fk=room_num_fk,
                    personnel_ID=personnel_ID,
                    use_time=use_time,
                    leave_time=leave_time)
            
        except IntegrityError:
            roomuse_tmp = Roomuse.get(room_num_fk = room_num_fk)
            roomuse_tmp.personnel_ID = personnel_ID
            roomuse_tmp.use_time = use_time
            roomuse_tmp.leave_time = leave_time   
            roomuse_tmp.save()
            
    @classmethod
    def delete(cls, roomuse):
        roomuse.delete_instance()

'''tweets = Tweet.select(Tweet, User).join(User).order_by(Tweet.create_date.desc())
for tweet in tweets:
    print(tweet.user.username, tweet.message)'''

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Personnel,Patient,Medicine,Prescription,Appointment,Room, Roomuse], safe=True)
    DATABASE.close()
    app = appt.Appointment("ap0001")
    pats = pat.Patient("AS")
    date = datetime.datetime(2016,1,12,4,50,30,100,None)
    app.create("1234",date,1,1,1,"1000","DIE")
    pats.create(1,"Por",date,"0818188216",10,"AS","AS")
    pers = person.Personnel(1)
    pers.create(1,"PO","a","b","c")
    #med.create("1234","lol",10000)
    #Appointment.create("5678",date,"pat0002","doc0001","pre0002","1000","SAVIOR")

    
