import datetime

from peewee import *

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

    class Meta:
        database  = DATABASE
        order_by = ('-patient_ID',)  


    @classmethod
    def add(cls, patient_ID, name, date_of_birth, phone_number, age):
        try:            
            cls.create(
                    patient_ID=patient_ID,
                    name=name,
                    date_of_birth=date_of_birth,
                    phone_number=phone_number,
                    age = age)
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
    medicine_ID =CharField()
    medicine_name = TextField()
    amount = IntegerField()

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
                    medicine_ID=medicine_ID,
                    personnel_ID=personnel_ID,
                    dosage=dosage)            
        except IntegrityError:
            pres_tmp = Prescription.get(prescription_ID = prescription_ID)
            pres_tmp.medicine_ID = medicine_ID
            pres_tmp.personnel_ID = personnel_ID
            pres_tmp.dosage = dosage
            pres_tmp.save()
            

    @classmethod
    def delete(cls, prescription):
        prescription.delete_instance()
    

class Appointment(Model):
    appointment_ID = CharField(unique=True)
    date = DateTimeField(default=datetime.datetime.now)
    patient_ID_fk = ForeignKeyField(Patient, related_name='appointed')
    personnel_ID_fk = ForeignKeyField(Personnel, related_name='supervise')    
    prescription_ID_fk = ForeignKeyField(Prescription)    
    service_charge = FloatField(default=0)

    class Meta:
        database = DATABASE
        order_by = ('-date',)
        
    @classmethod
    def add(cls, appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge):
        try:            
            cls.create(
                    appointment_ID=appointment_ID,
                    date=date,
                    patient_ID=patient_ID,
                    personnel_ID=personnel_ID,
                    prescription_ID=prescription_ID,
                    service_charge=service_charge)            
        except IntegrityError:
            app_tmp = Appointment.get(appointment_ID = appointment_ID)
            app_tmp.date = date
            app_tmp.patient_ID = patient_ID
            app_tmp.personnel_ID = personnel_ID
            app_tmp.prescription_ID = prescription_ID
            app_tmp.service_charge = service_charge
            app_tmp.save()
            

    @classmethod
    def delete(cls, appointment):
        appointment.delete_instance()


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
        order_by = ('-room_num',)
        
    @classmethod
    def create_add_update_roomuse(cls, room_num, personnel_ID, use_time, leave_time):
        try:            
            cls.create(
                    room_num=room_num,
                    personnel_ID=personnel_ID,
                    use_time=use_time,
                    leave_time=leave_time)
            
        except IntegrityError:
            roomuse_tmp = Roomuse.get(room_num = room_num)
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


    
    
    
    
