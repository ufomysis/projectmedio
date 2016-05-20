import datetime
import Models

class Prescription:
    def __init__(self, prescription_ID):
        self.prescription_ID = prescription_ID
        self.medicine_ID = ''
        self.personnel_ID = ''
        self.dosage = ''

    def get_personnel(self):
        row = Models.Prescription.select(Prescription, Personnel).join(Personnel).where(prescription_ID == self.prescription_ID).get()
        return row.personnel_ID_fk.name
    
    def get_medicine(self):        
        row = Models.Perscription.select(Prescription, Medicine).join(Medicine).where(prescription_ID == self.prescription_ID).get()
        return row.medicine_ID_fk.medicine_name

    def get_dosage(self):
        row = Models.Prescription.select().where(prescription_ID == self.prescription_ID).get()
        return row.dosage


    @classmethod
    def create_prescription(cls, prescription_ID, medicine_ID, personnel_ID, dosage):
        Models.Prescription.add(prescription_ID, medicine_ID, personel_ID, dosage)
