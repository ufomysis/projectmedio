from datetime import date
class AppointMent:
    def __init__(self):
        self.date = date(0,0,0)
        self.ApptId = 0
        self.MedList = []
        self.fee = 0
    def addNewMed(self,med):
        self.MedList.append(med)
    def setDate(self,dates):
        self.date.replace(year = dates.year)
        self.date.replace(month = dates.month)
        self.date.replace(day = dates.day)
    def setApptId(self,id):
        self.ApptId = id
    def getMedList(self):
        return self.MedList
    def getDate(self):
        return self.date
    def getApptId(self):
        return self.ApptId
    def setFee(self,fee):
        self.fee = fee
    def getFee(self):
        return self.fee
