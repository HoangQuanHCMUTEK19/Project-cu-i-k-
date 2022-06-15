from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from turtle import update 
import cv2 
import PIL.Image, PIL.ImageTk
from keras.models import  load_model
import cv2 
import numpy as np 
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing import  image

window = Tk()
window.title("So sanh khuon mat")
url = "http://192.168.137.172:4747/video"
label = ['Hong Diem','Manh Truong','Quoc Truong','Tran Thanh','Truong Giang','Viet Anh']
#,'Huong Giang'
video = cv2.VideoCapture(url)
canvas_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
canvas_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)*1.05

model = load_model("Projectk.h5")
k = 0 
predict = 0

canvas  = Canvas(window, width = canvas_width, height= canvas_height , bg="white" )
canvas.pack()
text = ""

def handleCompare():
    global text, predict
    ret, frame = video.read() #ret la ket qua doc anh , frame la anh doc ve 
    #Neu doc thanh cong thi hien thi
    if ret == True:
        # Resize
        img = frame.copy()
        img = img[60:370, 200:420]
        img = cv2.resize(img,(150,150))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img_to_array(img)
        img = img.reshape(1,150,150,1) 
        img = img.astype('float32') 
        img = img/255 
        predict = model.predict(img)
        k = str(np.max(predict)*100)
        text =  ('Ti le giong voi dien vien '+ label[np.argmax(predict)] + 'la' +  k  + '%')
        if np.argmax(predict) == 0:
            img1 = cv2.imread('E:/Nam3ki2/Tri tue nhan tao/Project cuoi ki/New folder/1.png')
            img1 = cv2.resize(img1,(300,300))
            cv2.imshow('Dien Vien',img1)
        if np.argmax(predict) == 1:
            img1 = cv2.imread('E:/Nam3ki2/Tri tue nhan tao/Project cuoi ki/New folder/k.png')
            img1 = cv2.resize(img1,(300,300))
            cv2.imshow('Dien Vien',img1)
        if np.argmax(predict) == 2:
            img1 = cv2.imread('E:/Nam3ki2/Tri tue nhan tao/Project cuoi ki/New folder/2.jpg')
            img1 = cv2.resize(img1,(300,300))
            cv2.imshow('Dien Vien',img1)
        if np.argmax(predict) == 3:
            img1 = cv2.imread('E:/Nam3ki2/Tri tue nhan tao/Project cuoi ki/New folder/19.png')
            img1 = cv2.resize(img1,(300,300))
            cv2.imshow('Dien Vien',img1)
        if np.argmax(predict) == 4:
            img1 = cv2.imread('E:/Nam3ki2/Tri tue nhan tao/Project cuoi ki/New folder/56.jpg')
            img1 = cv2.resize(img1,(300,300))
            cv2.imshow('Dien Vien',img1)
        if np.argmax(predict) == 5:
            img1 = cv2.imread('E:/Nam3ki2/Tri tue nhan tao/Project cuoi ki/New folder/38.png')
            img1 = cv2.resize(img1,(300,300))
            cv2.imshow('Dien Vien',img1)


button = Button(window, text = "So sanh",command = handleCompare)
button.place(x=450,y=480)

def handleCam():
    global k
    k = 1 - k 
button1 = Button(window, text = "Mo/Tat Cam",command = handleCam)
button1.place(x=150,y=480)


photo = None 

def update_frame():
    global canvas, photo
    ret, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     # Predict
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1.5
    color = (0, 255, 0)
    thickness = 2
    cv2.putText(frame, text ,org, font,fontScale/3, color, thickness, cv2.LINE_AA)
    cv2.rectangle(frame,(200,60),(400,350),(0,255,0),2)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    if k == 1:
        canvas.create_image(0,0,image=photo,anchor = tkinter.NW)
    else:
        cv2.destroyAllWindows()


    window.after(15,update_frame)

update_frame()
window.mainloop()