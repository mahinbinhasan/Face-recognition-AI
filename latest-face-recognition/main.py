#This Script is fully created by Mahin Bin Hasan
#
#
#It's a part of NDITC's AI project. 
#Overall project credits are given in our official Github repo.
#
#

import os
os.system("cls")
print("""

    _______    ____  _____      ___    ____
   / ____/ |  / /\ \/ /   |    /   |  /  _/
  / __/  | | / /  \  / /| |   / /| |  / /  
 / /___  | |/ /   / / ___ |_ / ___ |_/ /   
/_____/  |___/   /_/_/  |_(_)_/  |_/___/   
                                           
   
[+]Welcome to NDITC's AI powered Face recognition programme..                                 
 """) 
print("[+]Collecting resources")
    
def interneterr(module):
    if module!='face-recognition':
        print("\n\n[-] "+module+" Installation Failed")
        print("[!!]Check your Internet Connection!")
    else:
        print("\n\n[-] "+module+" Installation Failed")
        print("[/]Install Visual C++ \nOr")
        print("[!!]Check your Internet Connection!")
    exit()
    
    
def importmodule(module):
    print("[+]Installing  "+module+" from Pypi.org")
    os.system("pip install "+module)
    
from tkinter import*                              #for developer window

#-----------------PyQt5
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    importmodule('PyQt5')
    try:
        from PyQt5 import QtCore, QtGui, QtWidgets
    except:
        interneterr('PyQt5')
        
#----------------Pillow        

try:
    from PIL import ImageTk, Image,ImageDraw,ImageFont                        
except:
    importmodule('Pillow')
    try:
        from PIL import ImageTk, Image,ImageDraw,ImageFont
    except:
        interneterr('Pillow')

#---------------Launchscreen
try:
    from launchscreen import *                        # This Module is published on Pypi which is specially made by Mahin Bin Hasan for this AI project
except:
    importmodule('launchscreen')
    try:
        from launchscreen import *
    except:
        interneterr('launchscreen')

        
Yourscreen=screen('assets/lscrn.png',5000) 

from PIL import ImageGrab
import webbrowser
import threading

#-------------OpenCV

try:
    import cv2
except:
    importmodule('opencv-python')
    try:
        import cv2
    except:
        interneterr('opencv-python')
        
        
#----------face-recognition

try:
    import face_recognition
except:
    importmodule('face-recognition')
    try:
        import face_recognition
    except:
        interneterr('face-recognition')

#-------------Numpy

try:
    import numpy as np
except:
    importmodule('numpy')
    try:
        import numpy as np
    except:
        interneterr('numpy')
        
#-------------Pyttsx3                                   #Voice Engine 
try:
    import pyttsx3 
except:
    importmodule('pyttsx3')
    try:
        import pyttsx3 
    except:
        interneterr('pyttsx3')
Yourscreen.run()

print("[+]Initializing Sound Engine")
engine = pyttsx3.init()
engine.setProperty('rate', 100) 
video_capture = cv2.VideoCapture(0)
#-----------------------------------------Faces--------------------------------
print("[+]Loading Faces")
mahin_image = face_recognition.load_image_file("faces/mahin.jpg")
mahin_face_encoding = face_recognition.face_encodings(mahin_image)[0]
saikat1_image = face_recognition.load_image_file("faces/saikat1.jpg")
saikat1_face_encoding = face_recognition.face_encodings(saikat1_image)[0]
saikat2_image = face_recognition.load_image_file("faces/saikat2.jpg")
saikat2_face_encoding = face_recognition.face_encodings(saikat2_image)[0]
tonmoy_image = face_recognition.load_image_file("faces/tonmoy.jpg")
tonmoy_face_encoding = face_recognition.face_encodings(tonmoy_image)[0]
tonmoy2_image = face_recognition.load_image_file("faces/tonmoy2.jpg")
tonmoy2_face_encoding = face_recognition.face_encodings(tonmoy2_image)[0]
hemanto1_image = face_recognition.load_image_file("faces/hemanto1.jpg")
hemanto1_face_encoding = face_recognition.face_encodings(hemanto1_image)[0]
hemanto2_image = face_recognition.load_image_file("faces/hemanto2.jpg")
hemanto2_face_encoding = face_recognition.face_encodings(hemanto2_image)[0]

known_face_encodings = [
    mahin_face_encoding,
    saikat1_face_encoding,
    saikat2_face_encoding,
    tonmoy_face_encoding,
    tonmoy2_face_encoding,
    hemanto1_face_encoding,
    hemanto2_face_encoding,
]
known_face_names = [
    "Mahin",
    "Saikat Sir",
    "Saikat Sir",
    "Tonmoy",
    "Tonmoy",
    "Father Hemanto",
    "Father Hemanto",
]
#-----------------------------------------Face Section End---------------------------
face_locations = []
face_encodings = []
face_names = []
fonames=[]
global sts
sts=True


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 579)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color:rgb(104, 117, 116)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color:rgb(104, 117, 116)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"color:White;\n"
"background:rgb(0, 255, 127);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:rgba(255, 253, 254, 100);\n"
"text-align:center;\n"
"padding-left:100%;\n"
"font-size:50px;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 540, 801, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:rgb(197, 197, 197)\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 110, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:rgba(255, 255, 255, 120);\n"
"color:white;\n"
"padding-left:50%;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"color:White;\n"
"background:rgb(255, 51, 54);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 180, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"border-radius:10px;\n"
"border:2px solid rgb(168, 250, 248);\n"
"color:white;\n"
"padding-left:20%;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 220, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"border-radius:10px;\n"
"border:2px solid rgb(168, 250, 248);\n"
"color:white;\n"
"padding-left:20%;\n"
"}")
        self.label_5.setObjectName("label_5")
        
#Label 6 -----------------------------------> EVYA description
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 450, 741, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"border:2px solid rgb(0, 255, 127);\n"
"border-radius:10px;\n"
"padding-left:20%;\n"
"padding-right:20%;\n"
"color:white\n"
"}")
        self.label_6.setObjectName("label_6")
        
#Label 7 -----------------------------------> Video Display Border
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 471, 351))
        self.label_7.setStyleSheet("QLabel{\n"
"border-radius:6px;\n"
"border:4px solid rgb(0, 255, 127);\n"
"}")
        self.label_7.setText("")
        #self.label_7.setPixmap(QtGui.QPixmap("r.jpg"))
        self.label_7.setObjectName("label_7")
        
#Label 8 -----------------------------------> Video Display NDITC logo
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 91, 31))
        self.label_8.setStyleSheet("QLabel{\n"
"background-color:rgba(255, 253, 254, 0);\n"
"}")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("assets/slogo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 540, 81, 21))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color:rgb(197, 197, 197);\n"
"border:1px solid rgb(17, 17, 17);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def welcome(self):  #Voice Gen Bug Fixed
        if per !="Unknown":
            mes="Welcome "+per
            engine.say(mes)
            engine.runAndWait()
            engine.stop()
            
            
            
    def oc(self):
        global sts
        
        while sts==True:
            global per
            _, frame = video_capture.read()
            frame = cv2.flip(frame,1)
            
                
            rgb_small_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

                best_match_index = np.argmin(face_distances)
                
                fd=face_distances[best_match_index]            #Face Distance part control
                fd=float(fd)
                fd=1-fd
                fd=round(fd,2)
                fd=fd*100
                if fd>50:
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    face_names.append(name)
                    
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                _translate = QtCore.QCoreApplication.translate
                if name not in fonames:
                    self.label_4.setText(_translate("MainWindow", name))
                    print(name)
                    
                    self.label_5.setText(_translate("MainWindow", str(fd)+'%'))
                    print(str(fd)+'%')
                    fonames.append(name)
                    per= name
                    self.msg()
                    
            
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #opencv_image = cv2.flip(opencv_image,1)
            captured_image = Image.fromarray(opencv_image)
            h, w, ch = opencv_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QtGui.QImage(opencv_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(550, 388)
            self.label_7.setPixmap(QtGui.QPixmap(p))
            
    def msg(self):
        td = threading.Thread(target=self.welcome)
        td.start()   
        
    def wth(self):
        global sts
        sts=True
        td = threading.Thread(target=self.oc)
        td.start()
        
    def stp(self):
        global sts
        sts=False
        self.label_7.setText(" ")
        
    def newwin(self):
        
        win = Tk()
        win.title('Developer Info ')
        
        Lab = Label(win,text='AI based Face Recognition NDITC',font=('','12'))
        Lab.pack()
        
        bod = Label(win,text='This program is created by NDITC AI Team.\nProduct Manager: Abdul Basit Tonmoy\n Full Appliaction: Md. Al Mahin Bin Hasan\n Post processing:Ahammed Shawki \nImage resources : Arko Chowdhury ')
        bod.pack()
        
        t = Button(win, bg="#777a80", fg="#bbbbbd", width=22, text='Find me on Facebook!!', command=lambda: self.brs())
        t.pack()
        
        win.mainloop()
        
    def brs(self):
        urb = 'https://www.facebook.com/root.mahin'
        webbrowser.open(urb)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition-EVYA.AI"))
        self.pushButton.setText(_translate("MainWindow", "RUN AI"))
        self.pushButton.clicked.connect(self.wth)
        self.label.setText(_translate("MainWindow", "Face Recognition-EVYA.AI"))
        self.label_2.setText(_translate("MainWindow", "                                                                                                                                 NDITC"))
        self.label_3.setText(_translate("MainWindow", "Details"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.pushButton_2.clicked.connect(self.stp)
        self.label_6.setText(_translate("MainWindow", "EVYA.AI is Notre Dame Information Technology Club\'s Official Artificial Intelligence\n"
"           application that performs  face recognition as the back-end head\n"
"                                             of the Tinker bot"))
        self.pushButton_3.setText(_translate("MainWindow", "Developer Info"))
        self.pushButton_3.clicked.connect(self.newwin)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
