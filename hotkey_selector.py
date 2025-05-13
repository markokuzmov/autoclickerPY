import tkinter as tk

class HotkeySelector():
    def __init__(self, root, row, column, padx, pady):
        self.root = root
        self.hotkey = "Q"
        self.recording = False
        
        self.button = tk.Button(root, text=f"Hotkey: {self.hotkey}", command=self.start_recording)
        self.button.grid(row=row, column=column, padx=padx, pady=pady)

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.button.config(text="Press a key...")
            self.root.bind("<Key>", self.set_hotkey)
    
            
    def set_hotkey(self, event):
        self.hotkey = event.keysym.upper()
        self.button.config(text=f"Hotkey: {self.hotkey}")
        self.root.unbind("<Key>")
        self.recording = False