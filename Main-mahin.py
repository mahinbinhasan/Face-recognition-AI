import os
os.system("cls")
print("""
#----------------Script header| please do not modify this head section without permission...

    ---------Program Info----------   
    Name: Face RECOGNITION AI         
    Language: Python                  
    Published by : Notre Dame IT Club 
    Patron: Abdul Basit Tonmoy        
    Team Member: Mahin,Shawki,Arko    
                ----       
    Copyright of Mahin Bin Hasan,2023            
    https://www.facebook.com/root.mahin                       
    https://www.youtube.com/AlMahin     
    https://github.com/mahinbinhasan                   
 
 
    -------Main Script Info------       
    Author: Md. Al Mahin Bin Hasan          
    Modules: all modules are public     
          available for public use         
                                   
 """)                                                                  
#-----------------------------------------------------------------Code starts from here..
print("Loading Resources..")
#<---------------Import Portion-------------------->
from tkinter import*
from PIL import ImageTk, Image,ImageDraw,ImageFont
from PIL import ImageGrab
import webbrowser
import threading
import cv2
import face_recognition
import numpy as np
import pyttsx3

#<------------------------------------------------>
print("Initializing...")
#<-------------------Initialize------------------->
engine = pyttsx3.init()
engine.setProperty('rate', 100) 
nsrc = " "
root = Tk()
root.title("FACE RECOGNITION AI")
root.geometry("880x675")
root.configure(bg="#202229")
icon=PhotoImage(height=16, width=16)
icon.blank()
root.wm_iconphoto('True', icon)
#root.resizable(False,False)
srcdimx = 550 # Resized Image length
srcvx = srcdimx/2
srcdimy = 388 #Resized Image Height
srcvy = srcdimy/2
srcvy = srcvy + 10
csrc = " "

#<---------------Header Functions--------------->
def newwin():
    win = Tk()
    win.title('Developer Info ')
    
    Lab = Label(win,text='AI based Face Recognition NDITC',font=('','12'))
    Lab.pack()
    
    bod = Label(win,text='This program is created by NDITC AI Team.\nPatron: Abdul Basit Tonmoy\n GUI,AI & Voice implementation: Md. Al Mahin Bin Hasan\n Post processing:Ahammed Shawki \nImage resources : Arko Chowdhury ')
    bod.pack()
    
    t = Button(win, bg="#777a80", fg="#bbbbbd", width=22, text='Find me on Facebook!!', command=lambda: brs())
    t.pack()
    
    win.mainloop
     
def brs():
    urb = 'https://www.facebook.com/root.mahin'
    webbrowser.open(urb)
#<--------------------------------------------->   
def imp():
    print("Working!!")


#<-----------------Threads-------------------->
global per
per=""
def wth():
    td = threading.Thread(target=welcome)
    td.start()
       
#<---------------------------------------------------------------->
video_capture = cv2.VideoCapture(0)
#-----------------------------------------Faces--------------------------------

mahin_image = face_recognition.load_image_file("mahin.jpg")
mahin_face_encoding = face_recognition.face_encodings(mahin_image)[0]
saikat1_image = face_recognition.load_image_file("saikat1.jpg")
saikat1_face_encoding = face_recognition.face_encodings(saikat1_image)[0]
saikat2_image = face_recognition.load_image_file("saikat2.jpg")
saikat2_face_encoding = face_recognition.face_encodings(saikat2_image)[0]
tonmoy_image = face_recognition.load_image_file("tonmoy.jpg")
tonmoy_face_encoding = face_recognition.face_encodings(tonmoy_image)[0]
tonmoy2_image = face_recognition.load_image_file("tonmoy2.jpg")
tonmoy2_face_encoding = face_recognition.face_encodings(tonmoy2_image)[0]
hemanto1_image = face_recognition.load_image_file("hemanto1.jpg")
hemanto1_face_encoding = face_recognition.face_encodings(hemanto1_image)[0]
hemanto2_image = face_recognition.load_image_file("hemanto2.jpg")
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
def ocs():
    stsbox.insert(END,'Video Capturing Started')
    oc()
fonames=[]
def welcome():
    if per !="Unknown":
        mes="Welcome "+per
        engine.say(mes)
        engine.runAndWait()
def oc():
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
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        if name not in fonames:
            stsbox.insert(END,'New Face detected-'+name)
            fonames.append(name)
            per= name
            wth()
            
    
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #opencv_image = cv2.flip(opencv_image,1)
    captured_image = Image.fromarray(opencv_image)
    photo_image = ImageTk.PhotoImage(image=captured_image)
    viewbox.photo_image = photo_image
    viewbox.configure(image=photo_image,width=srcdimx,height=srcdimy)
    
    viewbox.after(5,oc)
#<--------------------------Header-------------------------------->
header = Frame(root,bg="#3C3F41")
header.pack()

vrs = Label(header,bg="#3C3F41",width = 100,text = 'Version 1.1     |     Release Date : X,x,2023     ',fg="#bbbbbd")
vrs.grid(row = 0 ,column = 0)

cnbt = Button(header,bg="#777a80",fg="#bbbbbd",width = 12,text ='Developer Info',command = lambda: newwin())
cnbt.grid(row = 0,column = 1)

cn = Button(header,bg="#3C3F41",width = 12,text ='----------')
cn.grid(row = 0,column = 2)

lab = Label(root,text="NDITC'S AI POWERED FACE RECOGNITION APP",font=('Trebuchet MS Bold','28'),bg='#202229',fg='#56fc03').pack()
#lab = Label(root,text="FACE RECOGNITION APP",font=('Trebuchet MS Bold','28'),bg='#202229',fg='#56fc03').pack()

#<---------------------------------------------------------------->




panel = Frame(root,bg="#181a1f")
panel.pack()
com = Frame(panel,bg="#181a1f",borderwidth=20)
com.grid(row=0,column=1)

V = StringVar()


buts = Frame(com,bg="#181a1f")
buts.pack()


expbut = Button(buts,bg="#42e3f5",fg="#e705f7",font=('Impact Regular','12'),text="Open Camera",width=12,command=lambda: ocs())
expbut.grid(row=0,column=0)


viewbox = Label(panel,width=95,height=27,bd=0,highlightthickness=2,bg="#777a80")
viewbox.grid(row = 0,column=2)


stsbo = Frame(root,borderwidth="8",bg="#181a1f")
stsbo.pack()

hdes = Label(stsbo,text="Status Display",font=('','12'))
scrollbar = Scrollbar(stsbo,orient = VERTICAL)

stsbox = Listbox(stsbo,width=100,height= 10,bg="Black",font=('Terminal','11'),fg="#ffffff",borderwidth="8",yscrollcommand = scrollbar.set)
scrollbar.config(command=stsbox.yview)

scrollbar.pack(side=RIGHT,fill=Y)
stsbox.pack(side = LEFT)


#<-----------------Footer--------------->
footer = Frame(root)
footer.pack()

copy = Label(footer,width=200,borderwidth=2,bg="#3C3F41",text="This Software is created by Mahin Bin Hasan",font=('','12'),fg="#bbbbbd")
copy.pack()
#<-----------------Footer--------------->
root.mainloop()