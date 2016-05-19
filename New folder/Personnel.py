import Models
import Schedule

class Personnel:
    def __init__(self, personnel_ID):
        self.personnel_ID = personnel_ID
        self.name = ''
        self.sector = ''
        self.user_id = ''
        self.user_pass = ''

    def get_name(self):
        row = Models.Personnel.select().where(personnel_ID = self.personnel_ID).get()
        return row.name

    def get_sector(self):
        row = Models.Personnel.select().where(personnel_ID = self.personnel_ID).get()
        return row.sector

    def get_user_id(self):
        row = Models.Personnel.select().where(personnel_ID = self.personnel_ID).get()
        return row.user_id

    def get_user_pass(self):
        row = Models.Personnel.select().where(personnel_ID = self.personnel_ID).get()
        return row.user_pass

    
    @classmethod
    def create(cls, personnel_ID, name, sector, user_id, user_pass):
        Models.Personnel.add(personnel_ID, name, sector, user_id, user_pass)

    @classmethod
    def delete(cls):
        row = Models.Personnel.select().where(personnel_ID == self.personnel_ID).get()
        Models.personnel_ID.delete(row)


class Doctor(Personnel):
    def __init__(self, personnel_ID):
        super.__init__(personnel_ID)
        self.schedule = Schedule(personnel_ID)
        
    def add_sch(self, appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge):
        self.schedule.add_sch(appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge)

    def del_sch(self, appointment_ID):
        self.schedule.del_from_sch(appointment_ID)

    def get_lab_result(self, appointment_ID):
        row = Models.Appointment.select().where(appointment_ID == appointment_ID).get()
        return row.lab_result

class Reception(Personnel):
    def set_fee(self, fee, appointment_ID):        
        medicine_tmp = Models.Appointment.update(service_charge=fee).where(Models.Appointment.appointment_ID == appointment_ID)
        medicine_tmp.execute()


class Lab(Personnel):
    def __init__(self,personnel_ID, appointment_ID):
        super.__init__(personnel_ID)
        self.appointment_ID = appointment_ID
        

    def send_lab_result(self, result):
        tmp = Models.Appointment.update(lab_result=result).where(Models.Appointment == self.appointment_ID)
        tmp.execute()
        
    def use_room(self, room_num_fk, personnel_ID, use_time, leave_time):
        Models.Roomuse.add(room_num_fk, personnel_ID, use_time, leave_time);
        

        
        
