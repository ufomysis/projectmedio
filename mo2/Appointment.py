import datetime
import Models

class Appointment:
    def __init__(self, appointment_ID):
        self.patient_ID = ''
        self.personnel_ID = ''
        self.prescription_ID = ''
        self.service_charge = 0
        self.date = datetime.datetime.now        
        
    def get_date(self):
        row = Models.Appointment.select().where(Models.Appointment.appointment_ID == self.appointment_ID).get()
        return row.date.strftime('%A %B %d, %Y %I:%M%p')

    def get_patient(self):
        row = Models.Appointment.select(Appointment, Patient).join(Patient).where(Models.Appointment.appointment_ID == self.appointment_ID).get()
        return row.patient_ID_fk.name

    def get_personnel(self):
        row = Models.Appointment.select(Appointment, Personnel).join(Personnel).where(Models.Appointment.appointment_ID == self.appointment_ID).get()
        return row.personnel_ID_fk.name

    def get_service_charge(self):
        row = Models.Appointment.select().where(Models.Appointment.appointment_ID == self.appointment_ID).get()
        return row.service_charge

    def get_lab_result(self):
        row = Models.Appointment.select().where(Models.Appointment.appointment_ID == self.appointment_ID).get()
        return row.lab_result


    @classmethod
    def create(cls, appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge):
        Models.Appointment.add(appointment_ID, date, patient_ID, personnel_ID, prescription_ID, service_charge)

    @classmethod
    def delete(cls, appointment_ID):
        row = Models.Appointment.select().where(appointment_ID == appointment_ID).get()
        Models.Appointment.delete(row)        

    
