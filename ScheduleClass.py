import ApptClass as Appt
class Schedule:
    def __init__(self):
        self.ApptList = []
    def addNewAppt(self,appt):
        self.ApptList.append(appt)
    def deleteAppt(self,Id):
        for appt in self.ApptList:
            if (appt.getId == Id):
                self.ApptList.remove(appt)
                break
    def getSch(self):
        return self.ApptList