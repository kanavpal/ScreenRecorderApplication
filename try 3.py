import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import datetime

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")

        self.recording = False
        self.video_writer = None
        self.recording_history = []

        self.start_button = ttk.Button(root, text="Start Recording", command=self.start_recording)
        self.stop_button = ttk.Button(root, text="Stop Recording", command=self.stop_recording)
        self.history_button = ttk.Button(root, text="Show History", command=self.show_history)
        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.history_button.pack(pady=10)

    def start_recording(self):
        self.recording = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"

        self.video_writer = cv2.VideoWriter(
            f"recording_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.avi",
            cv2.VideoWriter_fourcc(*'XVID'),
            25,  # Frames per second
            (1920, 1080)  # Screen resolution (adjust as needed)
        )

        while self.recording:
            screenshot = self.capture_screen()
            self.video_writer.write(screenshot)

        self.video_writer.release()
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"
        self.recording_history.append(f"recording_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.avi")

    def stop_recording(self):
        self.recording = False

    def capture_screen(self):
        screen = ImageGrab.grab()
        return cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Recording History")

        history_listbox = tk.Listbox(history_window)
        for item in self.recording_history:
            history_listbox.insert(tk.END, item)
        history_listbox.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorder(root)
    root.mainloop()
