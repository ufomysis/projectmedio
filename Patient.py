import ApptClass as appt 
import time
from datetime import date
class Patient:
    def __init__(self):
        self.name = ""
        self.age = 0.00
        self.DoB  = date()
        self.appt = []
        self.Id = 0
    def setName(self,name):
        self.name = name
    def setAge(self):
        if (self.DoB.month < time.strftime("%m")):
            self.age = time.strftime("%y") - self.DoB.year
            month = time.strftime("&m") - self.DoB.month
            month = month/12 * 10
            month /= 100
            self.age += month
        else:
            self.age = self.age = time.strftime("%y") - self.DoB.year - 1
            month = 12 - (time.strftime("%y") - self.DoB.year)
            month = month/12 * 10
            month /= 100
            self.age += month
    def setDoB(self,nday,nmonth,nyear):
        self.DoB.replace(year = nyear)
        self.DoB.replace(month = nmonth)
        self.DoB.replace(day = nday)
        self.setAge()
    def setId(self,id):
        self.Id = id
    def addNewAppt(self,appt):
        self.appt.append(appt)
    def deleteAppt(self,Id):
        for appt in self.ApptList:
            if (appt.getId == Id):
                self.ApptList.remove(appt)
                break
    def getName(self):
        return self.name
    def getId(self):
        return self.Id
    def getDoB(self):
        return self.DoB
    def getAge(self):
        self.setAge()
        return self.age
    def getApptList(self):
        return self.appt

