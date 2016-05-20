import Models
import Schedule
import datetime

class Personnel:
    def __init__(self, username):
        self.user_id = username

    def get_name(self):
        row = Models.Personnel.select().where(Models.Personnel.user_id == self.user_id).get()
        return row.name

    def get_sector(self):
        row = Models.Personnel.select().where(Models.Personnel.user_id == self.user_id).get()
        return row.sector

    def get_personnel_ID(self):
        row = Models.Personnel.select().where(Models.Personnel.user_id == self.user_id).get()
        return row.personnel_ID

    def get_user_pass(self):
        row = Models.Personnel.select().where(Models.Personnel.user_id == self.user_id).get()
        return row.user_pass

    def val_user_id(self):
        try:
            user = Models.Personnel.get(Models.Personnel.user_id == self.username)
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
    
    @classmethod
    def create(cls, personnel_ID, name, sector, user_id, user_pass):
        Models.Personnel.add(personnel_ID, name, sector, user_id, user_pass)

    @classmethod
    def delete(cls, username):
        row = Models.Personnel.select().where(Models.Personnel.user_id == username).get()
        Models.Personnel.delete(row)


class Doctor(Personnel):
    def __init__(self, username):
        super.__init__(username)
        self.schedule = Schedule(username)
        
    def add_sch(self, appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge):
        self.schedule.add_sch(appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge)

    def del_sch(self, appointment_ID):
        self.schedule.del_from_sch(appointment_ID)

    def get_lab_result(self, appointment_ID):
        row = Models.Appointment.select().where(appointment_ID == appointment_ID).get()
        return row.lab_result

    def prescribe(self, appointment_ID, medicine_ID, date = datetime.datetime.now):
        Models.Prescribe.add(appointment_ID, medicine_ID, date)

    def get_appt_lst(self):
        return [appt_lst for appt_lst in Models.Appointment.select().where(Models.Appointment.personnel_ID_fk == get_personnel_ID())]

class Reception(Personnel):
    def set_fee(self, fee, appointment_ID):        
        medicine_tmp = Models.Appointment.update(service_charge=fee).where(Models.Appointment.appointment_ID == appointment_ID)
        medicine_tmp.execute()

    def view_req_detail(self):
        return [req_detail for req_detail in Models.Reqdetail.select().where(Models.Reqdetail.is_completed == False)]

    def complete_req_detail(self, patient_ID):
        tmp = Models.Reqdetail.update(is_completed=True).where(Models.Reqdetail.patient_ID_fk == patient_ID)
        tmp.execute()

    def view_medreq(self):
        return [medreq for medreq in Models.Medpercase.select().where(Models.Medpercase.is_completed == False)]

    def complete_medreq(self, appointment_ID):
        tmp = Models.Medpercase.update(is_completed = True).where(Models.Medpercase.appointment_ID_fk == appointment_ID)
        tmp.execute()


class Pharmacist(Personnel):
    def view_presc(self):
        return [presc for presc in Models.Prescribe.select().where(Models.Prescribe.is_completed == False)]
    
    def complete_presc(self, appointment_ID):
        tmp = Models.Prescribe.update(is_completed = True).where(Models.Prescribe.appointment_ID_fk == appointment_ID)
        tmp.execute()

    def req_med_percase(self, appointment_ID, medicine_ID):
        Models.Medpercase.add(appointment_ID, medicine_ID, dosage, datetime.datetime.now, False)
        
        
class Lab(Personnel):
    def __init__(self,personnel_ID, appointment_ID):
        super.__init__(personnel_ID)
        self.appointment_ID = appointment_ID
        

    def send_lab_result(self, result):
        tmp = Models.Appointment.update(lab_result=result).where(Models.Appointment == self.appointment_ID)
        tmp.execute()
        
    def use_room(self, room_num_fk, personnel_ID, use_time, leave_time):
        Models.Roomuse.add(room_num_fk, personnel_ID, use_time, leave_time);
        

        
        
