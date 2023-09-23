import cv2
import tkinter as tk
from tkinter import ttk
import threading

class ScreenRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Recorder")
        self.root.geometry("400x200")

        self.recording = False
        self.video_writer = None

        self.start_button = ttk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.stop_button = ttk.Button(self.root, text="Stop Recording", command=self.stop_recording)
        self.start_button.pack(pady=10)
        self.stop_button.pack()
        
    def start_recording(self):
        self.recording = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter('output.avi', fourcc, 10, (1920, 1080))

        threading.Thread(target=self.record_screen).start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.video_writer.release()

    def record_screen(self):
        while self.recording:
            screenshot = self.capture_screen()
            self.video_writer.write(screenshot)

        self.video_writer.release()

    def capture_screen(self):
        screen = cv2.cvtColor(cv2.screenshot(), cv2.COLOR_BGR2RGB)
        return screen

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenRecorder()
    app.run()
