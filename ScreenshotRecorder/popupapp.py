from tkinter import *
import tkinter.messagebox
import pyscreenrec
recorder = pyscreenrec.ScreenRecorder()

rec_status='stopped'

root = tkinter.Tk()
recorder = pyscreenrec.ScreenRecorder()

# root window title and dimension
root.title("When you press a any button the message will pop up")
root.geometry('250x50')
root.attributes("-topmost", True)

# Create a messagebox showinfo

def Start():
	if rec_status=='stopped':
		tkinter.messagebox.showinfo("Recording Started")
		recorder.start_recording("recording.mp4", 30)
		rec_status='started'

def End():
	if rec_status=='stopped':
		tkinter.messagebox.showinfo("Recording Ended")
		recorder.stop_recording()
		rec_status='stopped'

# Create a Buttons

Button1 = Button(root, text="Start Recording", command=Start, pady=10)
Button2 = Button(root, text="End Recording", command=End, pady=10)

# Set the position of buttons
Button1.pack(side=LEFT)
Button2.pack(side=RIGHT)

root.mainloop()