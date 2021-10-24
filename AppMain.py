from PyQt5 import QtCore, QtGui, QtWidgets
import sys,sqlite3
from PyQt5.QtWidgets import QMessageBox,QComboBox,QGridLayout,QDialog, QPushButton,QLabel,QLineEdit
from PyQt5.QtCore import  Qt, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QIcon

class AppMain(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(AppMain, self).__init__(*args, **kwargs)
        self.setupUi()
        
        # Set window background image
        oImage = QImage(r".\image\bg_2.jpg")
        sImage = oImage.scaled(QSize(800,600))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage)) 
        palette.setColor(self.foregroundRole(), Qt.white)                                           
        self.setPalette(palette)
        self.show()
       
        
    def setupUi(self):
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        
        self.setObjectName("main")
        self.setFixedSize(800, 600)
        self.setWindowIcon(QtGui.QIcon(r'.\resources\face.png'))
        self.setIconSize(QtCore.QSize(24, 24))
        self.setWindowTitle("User Registration System")
        
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")

        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.setObjectName("toolbar")
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.addToolBar(self.toolbar)
        self.setStyleSheet("QToolBar { background-color: lightblue; }")

        self.menuSystem = QtWidgets.QMenu("&System",self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        self.menuSystem.triggered.connect(self.userLogin)


        self.actionLogin = QtWidgets.QAction(QtGui.QIcon(r".\icons\login.png"), "Login", self.menuSystem )
        self.actionLogin.setObjectName("Login")
        self.actionLogin.triggered.connect(self.userLogin)
        
    
               
        self.actionLogin = QtWidgets.QAction(QtGui.QIcon(r".\icons\login.png"),"Login",self.menuSystem)
        self.actionLogin.setObjectName("actionLogin")        
             
        
        self.menuSystem.addAction(self.actionLogin)
        self.toolbar.addAction(self.actionLogin)
       
          
    def closeEvent(self,event):
        result = QtWidgets.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure?",
                      QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)

        event.ignore()

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
            sys.exit(0)
            
    def userLogin(self):
        self.login = Login() 
        self.login.show()
        
            
class DBHelper():
    def __init__(self):
        self.conn=sqlite3.connect("user_registration.db")
        self.c=self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS user_name(name TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS user_mobile(country TEXT,mobile TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS user_password(password TEXT)")

        
    def addUserName(self,name):
        try:
        
            self.c.execute("INSERT INTO user_name(name) VALUES (?)",(name,))

            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Registration Success.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add user to the database.')
        
            
    def addUserMobile(self,country,mobile):
        try:  
            self.c.execute("INSERT INTO user_mobile(country,mobile) VALUES (?,?)",(country,mobile,))

            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Registration Success.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add user to the database.')
            
    def addUserPassword(self,password):
        try:
        
            self.c.execute("INSERT INTO user_password(password) VALUES (?)",(password,))

            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Registration Success.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add user to the database.')
            

class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        
        self.name=""
        self.mobile=""
        self.password=""

        
        self.userNameLabel=QLabel("Username")
        self.userNameLabel.setStyleSheet("color: #ffffff;")
        self.userNameLabel.setFont(font)
        
      
        self.userMobileLabel=QLabel("Mobile Number")
        self.userMobileLabel.setStyleSheet("color: #ffffff;")
        self.userMobileLabel.setFont(font)
        

        self.userPassLabel=QLabel("Password")
        self.userPassLabel.setStyleSheet("color: #ffffff;")
        self.userPassLabel.setFont(font)

        self.textName = QLineEdit(self)
        self.textMobile = QLineEdit(self)
        self.textPass = QLineEdit(self)
        self.textPass.setEchoMode(QLineEdit.Password)
              
        
        self.buttonReset = QPushButton('Reset', self)
        self.buttonReset.setStyleSheet("background-color: #21C4CB; color: #ffffff;")
        self.buttonReset.setFont(font)
        
        self.buttonRegister1 = QPushButton('Register', self)
        self.buttonRegister1.setStyleSheet("background-color: #21C4CB; color: #ffffff;")
        self.buttonRegister1.setFont(font)
        
        self.buttonRegister2 = QPushButton('Register', self)
        self.buttonRegister2.setStyleSheet("background-color: #21C4CB; color: #ffffff;")
        self.buttonRegister2.setFont(font)
        
        self.buttonRegister3 = QPushButton('Register', self)
        self.buttonRegister3.setStyleSheet("background-color: #21C4CB; color: #ffffff;")
        self.buttonRegister3.setFont(font)
        

        self.combobox = QComboBox()
        self.combobox.setFixedSize(60,20)
        myanmar = QIcon(r".\icons\myanmar.png")
        singapore = QIcon(r".\icons\singapore.png")
        japan = QIcon(r".\icons\japan.png")
        china = QIcon(r".\icons\china.png")
        self.combobox.addItem(myanmar, '+95')
        self.combobox.addItem(singapore, '+65')
        self.combobox.addItem(japan, '+81')
        self.combobox.addItem(china, '+86')  
        self.combobox.setStyleSheet("color: #000000;")
        self.combobox.setFont(font)
        
             
        self.buttonRegister1.clicked.connect(self.nameCheck)
        self.buttonRegister2.clicked.connect(self.mobileCheck)
        self.buttonRegister3.clicked.connect(self.passwordCheck)
        self.buttonReset.clicked.connect(self.reset)

        
        layout = QGridLayout(self)
        layout.addWidget(self.userNameLabel, 1, 1)
        layout.addWidget(self.userMobileLabel, 2, 1)

        layout.addWidget(self.userPassLabel, 3, 1)
        layout.addWidget(self.textName,1,2)
        layout.addWidget(self.combobox,2,2, alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(self.textMobile,2,2, alignment=QtCore.Qt.AlignRight)
        layout.addWidget(self.textPass,3,2)
        
        layout.addWidget(self.buttonRegister1,1,3)
        layout.addWidget(self.buttonRegister2,2,3)
        layout.addWidget(self.buttonRegister3,3,3)
        
        layout.addWidget(self.buttonReset,4,2, alignment=QtCore.Qt.AlignCenter)

        self.setWindowTitle("User Registration")
        self.resize(400,150)
        
          # Set window background image
        oImage = QImage(r".\image\bg_1.jpg")
#        sImage = oImage.scaled(QSize(800,600))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))  
        palette.setColor(self.foregroundRole(), Qt.white)                                          
        self.setPalette(palette)
        
    # Checking User Name:        
    def nameCheck(self):
        self.name=self.textName.text()
        self.dbhelper=DBHelper()
            
        if len(self.name) < 30:
            if not(self.name.isdigit()):
                if True:
                    if self.name.isalpha():
                        if True:
                            self.dbhelper.addUserName(self.name)
                            
                        
                    else:
                        QMessageBox.warning(QMessageBox(), 'Error',
                                                'Cannot have any symbol:')
                       
                        return None 
                        
        
            else:
                QMessageBox.warning(QMessageBox(), 'Error',
                            'Cannot have all number:')
                return None
            
        else:
              QMessageBox.warning(QMessageBox(), 'Error',
                            'Not more than 30 alphabet:')
              return None 
   
    # Checking User Name:        
    def mobileCheck(self):
        
        self.country=self.combobox.currentText()
        self.mobile=self.textMobile.text()
        
        self.dbhelper=DBHelper()
            
        if len(self.mobile) < 15:
            if self.mobile.isdigit():
                if True:
                    if not(self.mobile.isalpha()):
                        if True:
                            self.dbhelper.addUserMobile(self.country,self.mobile)
                        
                    else:
                        QMessageBox.warning(QMessageBox(), 'Error',
                                            'Cannot have all other symbol:')
                        return None 
        
            else:
                QMessageBox.warning(QMessageBox(), 'Error',
                            'Cannot have any other alphabet:')
                return None
            
        else:
              QMessageBox.warning(QMessageBox(), 'Error',
                            'Not more than 15 number:')
              return None 
          
            
    # Checking Password:        
    def passwordCheck(self):

        self.password=self.textPass.text()
        self.dbhelper=DBHelper()
            
        
        if len(self.password) >= 8 and len(self.password) <= 15:
            if len(self.password.upper()) > 1 and not(self.password.isdigit()): 
                if not(self.password.isalpha()):
                    if self.password.isspace():
                        QMessageBox.warning(QMessageBox(), 'Error',
                                            'Cannot have all spacing:')
                        return None 
                                    
                    else:                                                                          
                        self.dbhelper.addUserPassword(self.password)
                        
                else:
                    QMessageBox.warning(QMessageBox(), 'Error',
                                        'Allow symbols, but not compulsory:')
                    return None 
        
            else:
                QMessageBox.warning(QMessageBox(), 'Error',
                            'Must have at least 1 Capital Letter and 1 number:')
                return None
            
        else:
              QMessageBox.warning(QMessageBox(), 'Error',
                            'Min 8 character, but not more than 15 character:')
              return None 
        
    def reset(self):
        
        self.textName.setText("")
        self.textMobile.setText("")
        self.textPass.setText("")
        
       

        
#############################End of AppMain class###########################

if __name__ == "__main__":

    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
        app.aboutToQuit.connect(app.deleteLater)
    appMain = AppMain()
    appMain.show()
    
    sys.exit(app.exec_())
    app.exec_()