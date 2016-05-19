import sys

from PySide.QtCore import*
from PySide.QtGui import*
from PySide.QtUiTools import*

class userclientgui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)
        self.imagelogo = QPixmap("medio login.png");
        self.loader = QUiLoader();
        form = self.loader.load("C:/Users/por_n/Documents/SEP project UI/loginregistered.ui",self);
        self.setCentralWidget(form);
        self.background = form.findChild(QLabel,"label") ;
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        self.background.show();       
        button1 = form.findChild(QPushButton,"pushButton");
        button1.setIcon(QIcon("medio login.png"));
        button1.clicked.connect(self.tologinscreen);
    
    def tologinscreen(self):
        form2 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/log in mock up ui.ui",self);
        self.setCentralWidget(form2);
        self.background = form2.findChild(QLabel,"background");
        acclevel = form2.findChild(QComboBox,"acclevel");
        cslevel = form2.findChild(QLabel,"cslevel");
        self.keeplog = form2.findChild(QCheckBox,"keeplog");
        keeplogl = form2.findChild(QLabel,"keeplogl");
        logo = form2.findChild(QLabel,"logo");
        notres = form2.findChild(QLabel,"notres");
        self.passfield = form2.findChild(QLineEdit,"passfield");
        password = form2.findChild(QLabel,"password");
        self.remuser = form2.findChild(QCheckBox,"remuser");
        remuserl = form2.findChild(QLabel,"remuserl");
        self.userfield = form2.findChild(QLineEdit,"userfield");
        username = form2.findChild(QLabel,"username");
        loginb = form2.findChild(QPushButton,"login") 
        cancel = form2.findChild(QPushButton,"cancel");
        registerhere = form2.findChild(QPushButton,"registerhere");
                
        self.background.setPixmap(self.image);
        self.background.show();       
        logo.setPixmap(self.imagelogo);
        logo.show();
        cancel.clicked.connect(self.backtofront);
        loginb.clicked.connect(self.login);
    def backtofront(self):
        form = self.loader.load("C:/Users/por_n/Documents/SEP project UI/loginregistered.ui",self);
        self.setCentralWidget(form);
        self.background = form.findChild(QLabel,"label") ;
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        self.background.show();       
        button1 = form.findChild(QPushButton,"pushButton");
        button1.setIcon(QIcon("medio login.png"));
        button1.clicked.connect(self.tologinscreen);    
    
    def login(self):
        inputusername = self.userfield.text();
        inputpassword = self.passfield.text();
        self.remuser.isChecked();
        print(self.remuser.isChecked())
        print(self.keeplog.isChecked())
        print(inputusername);
        print(inputpassword);
        testuserkey = ""
        testpasskey = ""
        if(inputusername == testuserkey and inputpassword == testpasskey):
            form3 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/mainmenu.ui",self);
            self.setCentralWidget(form3);
            self.background = form3.findChild(QLabel,"background") ;
            self.image = QPixmap("Mainmenubg.png");
            self.background.setPixmap(self.image);
            button1 = form3.findChild(QPushButton,"appointment");
            button1.setIcon(QIcon("main button.png"));
            button1.clicked.connect(self.toappointment1); 
            button2 = form3.findChild(QPushButton,"medsche");
            button2.setIcon(QIcon("medicineschedulebutton.png"));
            button3 = form3.findChild(QPushButton,"transac");
            button3.setIcon(QIcon("Historybutton.png"));
            button4 = form3.findChild(QPushButton,"settings");
            button4.setIcon(QIcon("settingsbutton.png"));
            button5 = form3.findChild(QPushButton,"contact");
            button5.setIcon(QIcon("contactandclicktocallbutton.png")); 
        else:
            print("wrong username or password");
        
    def toappointment1(self):
        form3 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/appointmentscreen.ui",self);
        self.setCentralWidget(form3);
        self.background = form3.findChild(QLabel,"background");
        orth = form3.findChild(QPushButton,"Ortho");
        gastro = form3.findChild(QPushButton,"GI");  
        emer = form3.findChild(QPushButton,"ER");
        dermato = form3.findChild(QPushButton,"Derma");
        pedia = form3.findChild(QPushButton,"Ped");
        outpat = form3.findChild(QPushButton,"OPD");
        cardi = form3.findChild(QPushButton,"Cardio");
        neurology = form3.findChild(QPushButton,"Neuro");
        rad = form3.findChild(QPushButton,"Radio");
        back = form3.findChild(QPushButton,"backtomain");
        self.clocknow = form3.findChild(QLCDNumber,"clock");
        diviv = form3.findChild(QLine,"dividerverti");
        divih = form3.findChild(QLine,"dividerhori");
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        orth.setIcon(QIcon("orthopedicbutton.png"));
        gastro.setIcon(QIcon("GIbutton.png"));
        emer.setIcon(QIcon("ERbutton.png"));
        dermato.setIcon(QIcon("dermatologybutton.png"));
        pedia.setIcon(QIcon("pedibutton.png"));
        outpat.setIcon(QIcon("opdbutton.png"));
        cardi.setIcon(QIcon("cardiologybutton.png"));
        neurology.setIcon(QIcon("neurologybutton.png"));
        rad.setIcon(QIcon("radiologybutton.png"));
        back.setIcon(QIcon("returnbutton.png"));
            
        self.clocknow.setSegmentStyle(QLCDNumber.Filled);

        self.timer = QTimer();
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000);
    def showtime(self):
        self.time = QTime.currentTime();
        self.text = self.time.toString("hh:mm");
        self.clocknow.display(self.text);

    

        
class GUIobserver:
    def __init__(self, **kwargs):             
        self.guiuser = userclientgui()
        self.guiuser.show()
    def getuserfield(self):
        inputusername = self.guiuser.userfield.text();
        return inputusername
    def getpassfield(self):
        inputpassword = self.guiuser.passfield.text();
        return inputpassword
    def getkeepusernamestatus(self):
        return self.guiuser.remuser.isChecked()
    def getkeeploggedinstatus(self):
        return self.guiuser.keeplog.isChecked()

def main():
    
    app = QApplication(sys.argv)
    observer1 = GUIobserver()

    return app.exec_()
if __name__=="__main__":
    sys.exit(main())