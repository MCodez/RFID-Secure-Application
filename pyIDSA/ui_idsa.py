# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:00:50 2017

@author: LALIT ARORA
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import serial
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import cred
import datetime
import threading


class Ui_ISDA(object):
    def setupUi(self, ISDA):
        ISDA.setObjectName("ISDA")
        ISDA.resize(638, 322)
        ISDA.setMaximumSize(QtCore.QSize(638, 322))
        self.label2 = QtWidgets.QLabel(ISDA)
        self.label2.setGeometry(QtCore.QRect(40, 70, 171, 181))
        self.label2.setObjectName("image")
        #img=QtGui.QImage("test1.jpg")
        #self.displayimage("test1.jpg")
        #p = QtGui.QPalette()
        #gradient = QtGui.QLinearGradient(0, 0, 0, 400)
        #gradient.setColorAt(0.0, QtGui.QColor(30, 144, 255))
        #gradient.setColorAt(1.0, QtGui.QColor(30, 144, 255))
        #p.setBrush(QtGui.QPalette.Window,QtGui.QBrush(gradient))
        #ISDA.setPalette(p)
        
        self.label = QtWidgets.QLabel(ISDA)
        self.label.setGeometry(QtCore.QRect(230, 20, 161, 16))
        self.pushbutton=QtWidgets.QPushButton(ISDA)
        self.pushbutton.setGeometry(QtCore.QRect(450,290,75,20))
        self.pushbutton.setObjectName("start")
        self.pushbutton.clicked.connect(self.start)
        self.label3=QtWidgets.QLabel(ISDA)
        self.label3.setGeometry(QtCore.QRect(528,290,38,20))
        self.label3.setObjectName("status")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.touch = QtWidgets.QLabel(ISDA)
        self.touch.setGeometry(QtCore.QRect(40, 290, 161, 16))
        self.touch.setObjectName("touch")
        self.info = QtWidgets.QLabel(ISDA)
        self.info.setGeometry(QtCore.QRect(330, 70, 181, 171))
        self.info.setObjectName("info")
        self.retranslateUi(ISDA)
        self.displayimage("blank.png")
        QtCore.QMetaObject.connectSlotsByName(ISDA)
        
    
    def displayimage(self,filename):
        leftPixelMap = QtGui.QPixmap(filename)
        self.label2.setPixmap(leftPixelMap)
        self.label2.show()
        
        
    def retranslateUi(self, ISDA):
        _translate = QtCore.QCoreApplication.translate
        ISDA.setWindowTitle(_translate("ISDA", "IDSA Secure Login"))
        self.label.setText(_translate("ISDA", "WELCOME TO IDSA"))
        self.touch.setText(_translate("ISDA", "TOUCH YOUR SECURE ID CARD"))
        self.pushbutton.setText(_translate("ISDA","START"))
        self.info.setText(_translate("ISDA", " "))
    
    def sqleject(self,key):
        conn=sqlite3.connect('controlroom.sqlite')
        c=conn.cursor()
        conn.commit()
        tempe=[]
        for val in c.execute('SELECT * from Members WHERE RFID=?',(key,)):
            tempe.append(val)
        conn.commit()
        if len(tempe)==0:
            self.wrongperson()
            return 0
        else:
            t=self.check(tempe[0])
            return t
    def printit(self):
        threading.Timer(5.0, self.printit).start()
        

    def mail(self,to):
        fromaddr="<Sender email ID>"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = to
        msg['Subject'] = "ILLEGAL ENTRY TRIAL"
        body = "Someone with Invalid Secure ID had tried to make an entry in IDSA!"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        passw=cred.credent()
        server.login(fromaddr,passw)
        text = msg.as_string()
        server.sendmail(fromaddr,to, text)
        server.quit()
        
    def wrongperson(self):
        self.displayimage("access.png")
        self.info.setText("INVALID SECURE ID.")
        self.mail("<Recepient email ID>")
        self.touch.setText("INVALID SECURE ID..")
        #write something
        
    def check(self,a):
        desig=a[1]
        if desig=="MARSHAL" or desig=="HEAD":
            return "ACCESS PROVIDED.."
        else:
            return "ACCESS DENIED.."

   
    
    def arduinoconnect(self,com,baudrate):
        ser=serial.Serial(com,baudrate)
        while ser.inWaiting()==0:
            pass
        data=str(ser.readline())
        print(data)
        return(data[2:14])
    
    def displayinfo(self,a,b,d,e,f):
        string="NAME: "+a+"\n"+"DESIGNATION: "+b+"\n"
        string=string+"TIME: "+d+"\n"+"DATE: "+e+"\n"
        self.info.setText(string)
        self.info.show()
        self.displayimage(f)
        
        print(string)
        #m=self.delay(1)
        
        
    def stat(self,key,status):
        if status=="ACCESS DENIED..":
            self.displayimage("access.png")
            self.touch.setText("ACCESS DENIED..")
            return self.start
        now = datetime.datetime.now()
        curtime=str(now.hour)+":"+str(now.minute)+":"+str(now.second)
        curdate=str(now.day)+":"+str(now.month)+":"+str(now.year)
        conn=sqlite3.connect('controlroom.sqlite')
        c=conn.cursor()
        conn.commit()
        tempe=[]
        for val in c.execute('SELECT * from Members WHERE RFID=?',(key,)):
            tempe.append(val)
        conn.commit()
        n=tempe[0][0]
        e=tempe[0][1]
        m=tempe[0][2]
        d=curtime
        f=curdate
        g=tempe[0][3]
        self.displayinfo(n,e,d,f,g)
        print("HERE-------------------------")
        c.execute('INSERT INTO Stats (NAME,DESIGNATION,RFID,TIME,DATE,PHOTO) VALUES (?,?,?,?,?,?)',(n,e,m,d,f,g))
        conn.commit()
        conn.close()
        
    def start_timer(self):
        # Initialize timer
        self.timer = QtCore.QTimer()
        self.now = 0
        # Update display and start timer
        self.update_timer()
        self.timer.timeout.connect(self.tick_timer)
        self.timer.start(40000) # Duration of one second = 1000 msec
    
    def update_timer(self):
        self.runtime = "%d:%02d" % (self.now/60,self.now % 60)
        self.lcdNumber.display(self.runtime)

    def tick_timer(self):
        self.now += 1
        self.update_timer()

    def stop_timer(self):
        self.timer.stop
        
    def start(self):
        print("Starting------------------------")
        self.label3.setText("WORK")
        self.info.setText(" ")
        self.touch.setText(" ")
        self.work()
        self.start
    
    def work(self):
        while True:
            rfidcheck=self.arduinoconnect("COM5",9600)
            print(rfidcheck)
            if rfidcheck[0:3]!="340":
                pass
            else:
                print("HERE")
                status=self.sqleject(rfidcheck)
                break
        self.touch.setText(status)
        self.stat(rfidcheck,status)
        self.start_timer
        
        
        
                                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ISDA()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())