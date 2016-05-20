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
    user_id = CharField(unique=True)
    user_pass = CharField(max_length=100)

    class Meta:
        database  = DATABASE
        order_by = ('-patient_ID',)  


    @classmethod
    def add(cls, patient_ID, name, date_of_birth, phone_number, age, user_id, user_pass):
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
            patient_tmp.user_id = user_id
            patient_tmp.user_pass = user_pass
            patient_tmp.save()

    @classmethod
    def delete(cls, user):
        user.delete_instance()


class Medicine(Model):
    medicine_ID =CharField(unique=True)
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
   

class Appointment(Model):
    appointment_ID = CharField(unique=True)
    date = DateTimeField(default=datetime.datetime.now)
    patient_ID_fk = ForeignKeyField(Patient, related_name='appointed')
    personnel_ID_fk = ForeignKeyField(Personnel, related_name='supervise')    
    service_charge = FloatField(default=0)

    class Meta:
        database = DATABASE
        order_by = ('-date',)
        
    @classmethod
    def add(cls, appointment_ID, date, patient_ID, personnel_ID, service_charge):
        try:            
            cls.create(
                    appointment_ID=appointment_ID,
                    date=date,
                    patient_ID_fk=patient_ID_fk,
                    personnel_ID_fk=personnel_ID_fk,
                    prescription_ID_fk=prescription_ID_fk,
                    service_charge=service_charge,
                    lab_result=lab_result)            
        except IntegrityError:
            app_tmp = Appointment.get(appointment_ID = appointment_ID)
            app_tmp.date = date
            app_tmp.patient_ID_fk = patient_ID_fk
            app_tmp.personnel_ID_fk = personnel_ID_fk
            app_tmp.prescription_ID_fk = prescription_ID_fk
            app_tmp.service_charge = service_charge
            app_tmp.save()
            

    @classmethod
    def delete(cls, appointment):
        appointment.delete_instance()


class Room(Model):
    room_num = CharField(unique=True)
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


class Reqdetail(Model):
    patient_ID_fk = ForeignKeyField(Patient, related_name='requests')
    date = DateTimeField(default=datetime.datetime.now)
    detail = TextField()
    department = CharField()
    is_completed = BooleanField(default = False) 

    class Meta:
        database = DATABASE
        order_by = ('-date',)

    @classmethod
    def add(cls, patient_ID_fk, date, detail, department, is_completed = False):
        try:            
            cls.create(
                    patient_ID_fk=patient_ID_fk,
                    date=date,
                    detail=detail,
                    department=department,
                    is_completed=is_completed)
            
        except IntegrityError:
            reqdetail = Reqdetail.get(patient_ID_fk = patient_ID_fk)
            reqdetail.date = date
            reqdetail.detail = detail
            reqdetail.department = department
            reqdetail.is_completed = is_completed
            reqdetail.save()
            
    @classmethod
    def delete(cls, reqdetail):
        reqdetail.delete_instance()


class Prescribe(Model):
    appointment_ID_fk = ForeignKeyField(Appointment, related_name='requests')
    medicine_ID_fk = ForeignKeyField(Medicine, related_name='is requested by')
    date = DateTimeField(default=datetime.datetime.now)
    is_completed = BooleanField(default = False) 

    class Meta:
        database = DATABASE
        order_by = ('-date',)

    @classmethod
    def add(cls, appointment_ID_fk, medicine_ID_fk, date, is_completed):
        try:            
            cls.create(
                    appointment_ID_fk=appointment_ID_fk,
                    medicine_ID_fk=medicine_ID_fk,                    
                    date=date,
                    is_completed=is_completed)
            
        except IntegrityError:
            reqmedicine = Reqmedicine.get(appointment_ID_fk = appointment_ID_fk)
            reqmedicine.medicine_ID_fk = medicine_ID_fk
            reqmedicine.date = date
            reqmedicine.is_completed = is_completed
            reqmedicine.save()
            
    @classmethod
    def delete(cls, reqmedicine):
        reqmedicine.delete_instance()


class Medpercase(Model):
    appointment_ID_fk = ForeignKeyField(Appointment, related_name='requests')
    medicine_ID_fk = ForeignKeyField(Medicine, related_name='is requested by')
    dosage = FloatField()
    date = DateTimeField(default=datetime.datetime.now)
    is_completed = BooleanField(default = False)

    class Meta:
        database = DATABASE
        order_by = ('-date',)

    @classmethod
    def add(cls, appointment_ID_fk, medicine_ID_fk, dosage, date, is_completed):
        try:            
            cls.create(
                    appointment_ID_fk=appointment_ID_fk,
                    medicine_ID_fk=medicine_ID_fk,
                    dosage=dosage,
                    date=date,
                    is_completed=is_completed)
            
        except IntegrityError:
            medpercase = Reqmedicine.get(appointment_ID_fk = appointment_ID_fk)
            medpercase.medicine_ID_fk = medicine_ID_fk
            medpercase.dosage = dosage
            medpercase.date = date
            medpercase.is_completed = is_completed
            medpercase.save()
            
    @classmethod
    def delete(cls, reqmedicine):
        reqmedicine.delete_instance()


class PatUseMed(Model):
    appointment_ID_fk = ForeignKeyField(Appointment)
    patient_ID_fk = ForeignKeyField(Patient, related_name='uses')
    medicine_ID_fk = ForeignKeyField(Medicine, related_name='is used by')
    timeuse = TextField()
    days = DateTimeField()
    delta_days = DateTimeField()

    class Meta:
        database = DATABASE
        order_by = ('-patient_ID_fk',)


    @classmethod
    def add(cls, appointment_ID_fk, patient_ID_fk, medicine_ID_fk, timeuse, days, delta_days):
        try:            
            cls.create(
                    appointment_ID_fk=appointment_ID_fk,
                    patient_ID_fk=patient_ID_fk,
                    medicine_ID_fk=medicine_ID_fk,
                    timeuse=timeuse,
                    days=days,
                    delta_days=delta_days)
            
        except IntegrityError:
            usemed = PatUseMed.get(appointment_ID_fk = appointment_ID_fk)
            usemed.patient_ID_fk = patient_ID_fk
            usemed.medicine_ID_fk = medicine_ID_fk
            usemed.timeuse = timeuse
            usemed.days = days
            usemed.delta_days = delta_days
            usemed.save()
            
    @classmethod
    def delete(cls, usemed):
        usemed.delete_instance()

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Personnel, Patient, Medicine, Appointment, Room, Roomuse, Reqdetail, Prescribe, Medpercase, PatUseMed], safe=True)
    DATABASE.close()
    
    
    
    
