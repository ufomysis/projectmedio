import sys

from PySide.QtCore import*
from PySide.QtGui import*
from PySide.QtUiTools import*

class Phone_Window(QMainWindow):
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
        keeplog = form2.findChild(QCheckBox,"keeplog");
        keeplogl = form2.findChild(QLabel,"keeplogl");
        logo = form2.findChild(QLabel,"logo");
        notres = form2.findChild(QLabel,"notres");
        self.passfield = form2.findChild(QLineEdit,"passfield");
        password = form2.findChild(QLabel,"password");
        remuser = form2.findChild(QCheckBox,"remuserl");
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
        print(inputusername);
        print(inputpassword);
        testuserkey = "Satachan"
        testpasskey = "Yaoifanboy"
        if(inputusername == testuserkey and inputpassword == testpasskey):
            form3 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/mainmenu.ui",self);
            self.setCentralWidget(form3);
            self.background = form3.findChild(QLabel,"background") ;
            self.image = QPixmap("Mainmenubg.png");
            self.background.setPixmap(self.image);
            button1 = form3.findChild(QPushButton,"appointment");
            button1.setIcon(QIcon("main button.png"));
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

def main():
    
    app = QApplication(sys.argv)
    w = Phone_Window()
    w.show()
    return app.exec_()
if __name__=="__main__":
    sys.exit(main())