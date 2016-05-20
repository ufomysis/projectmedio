import Models
import Appointment

class Schedule:
    def __init__(self, personnel_ID):
        self.personnel_ID = personnel_ID
        self.appts = []

    def get_sch(self):
        table = Models.Appointment.select(Appointment, Personnel).join(Personnel).where(personnel_ID_fk == self.personnel_ID)
        for appt in table:
            self.appts.append(appt)        
        return self.appts

    def add_sch(self,appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge):
        Appointment.create(appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge)

    def del_from_sch(self, appointment_ID):
        Appointment.delete(appointment_ID)
        
    
        
