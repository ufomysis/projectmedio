import Models


class Medicine:
    def __init__(self, medicine_ID):
        self.medicine_ID = medicine_ID
        self.medicine_name = ''
        self.amount = 0

    def get_medicine_name(self):
        row = Models.Medicine.select().where(medicine_ID == self.medicine_ID).get()
        return row.medicine_name

    def get_amount(self):
        row = Models.Medicine.select().where(medicine_ID == self.medicine_ID).get()
        return row.amount

    def get_price(self):
        row = Models.Medicine.select().where(medicine_ID == self.medicine_ID).get()
        return row.price
    
    @classmethod
    def create(cls, medicine_ID, medicine_name, amount):
        Models.Medicine.add(medicine_ID, medicine_name, amount)

    @classmethod
    def delete(cls, medicine_ID):
        row = Models.Medicine.select().where(medicine_ID == medicine_ID).get()
        Models.Medicine.delete(row)        

