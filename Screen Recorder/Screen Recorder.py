from tkinter import *
import pyscreenrec
from PIL import Image, ImageTk
import cv2 

root=Tk()
root.geometry("400x600")
root.title("screen recorder")
root.config(bg="#fff")
root.resizable(False,False)
drawing = False
global x1, y1, x2,y2,num,h,w,windowRegion
x1,y1,x2,y2,h,w = 0,0,0,0,0,0
windowRegion=0
num = 0
def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)
def pause_rec():
    rec.pause_recording()
def resume_rec():
    rec.resume_recording()
def stop_rec():
    rec.stop_recording()
def draw_rect(event, x, y, flags, param):
		global x1, y1, drawing,  num, img, img2,x2,y2
		if event == cv2.EVENT_LBUTTONDOWN:
			drawing = True
			x1, y1 = x, y
		elif event == cv2.EVENT_MOUSEMOVE:
			if drawing == True:
				a, b = x, y
				if a != x & b != y:
					img = img2.copy()
				   
					cv2.rectangle(img, (x1,y1),(x,y), (0, 255, 0), 2)
		elif event == cv2.EVENT_LBUTTONUP:
			drawing = False
			num += 1
			font = cv2.FONT_HERSHEY_SIMPLEX
			x2 = x
			y2= y   
rec=pyscreenrec.ScreenRecorder()
#icon
image_icon=PhotoImage(file=r"D:\Python\Python Files\screen recorder\icon.png")
root.iconphoto(False,image_icon)

#heading
lb1=Label(root,text="Secreen Recorder",bg='#fff',font="arial 15 bold")
lb1.pack(pady=20)

image1=PhotoImage(file="yellow.png")
Label(root,image=image1,bg="#fff").place(x=-2,y=40)

image2=PhotoImage(file="blue.png")
Label(root,image=image2,bg="#fff").place(x=223,y=200)

image3=PhotoImage(file="recording.png")
Label(root,image=image3,bd=0).pack(pady=30)

#entry

Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=18,font="arial 15")
entry.place(x=100,y=350)
Filename.set("recording25")
#buttons
	

start=Button(root,text='Start',font="arial 22",bd=0,command=start_rec)
start.place(x=140,y=250)

image4=PhotoImage(file='pause.png')
pause=Button(root,image=image4,bd=0,bg='#fff',command=pause_rec)
pause.place(x=50,y=450)

image5=PhotoImage(file='resume.png')
resume=Button(root,image=image5,bd=0,bg='#fff',command=resume_rec)
resume.place(x=150,y=450)

image6=PhotoImage(file='stop.png')
stop=Button(root,image=image6,bd=0,bg='#fff',command=stop_rec)
stop.place(x=250,y=450)

image7=PhotoImage(file='capture.png')
stop=Button(root,image=image7,bd=0,bg='#fff',command=draw_rect)
stop.place(x=350,y=450)




















root.mainloop()
