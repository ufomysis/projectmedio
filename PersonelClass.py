import ScheduleClass as Sch
import ApptClass as appt
class Personnel:
    def __init__(self):
        self.name = ""
        self.numId = 0
        self.section = ""
    def setName(self,name):
        self.name = name
    def setNumId(self,id):
        self.NumId = id
    def setSection(self,section):
        self.section = section
    def getName(self):
        return self.name
    def getNumId(self):
        return self.NumId
    def getSection(self):
        return self.section

class Doctor(Personnel):
    def __init__(self):
        super().__init__()
        self.sch = Sch.Schedule()
    def addAppt(self,appt):
        self.sch.addNewAppt(appt)
    def deleteAppt(self,id):
        self.sch.deleteAppt(id)

class Reception(Personnel):
    def  calculateFee(self,appt):
         MedList = appt.getMedList
         fee = appt.getFee() + 500
         for med in MedList:
             fee += med.getFee()
         appt.setFee(fee)
    
class Lab(Personnel):
    def __init__(self):
        super().__init__()
        self.apptUse = appt() #appt which use room now
        self.roomNum = 0
    def sendLabresult(self,result): #must  send lab result to both Doctor and Appt class
        return result
    def setapptUse(self,appt):
        self.apptUse = appt
class Pharmacist(Personnel):
    def __init__(self):
        super().__init__()
