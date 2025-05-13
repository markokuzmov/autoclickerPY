import pynput
import keyboard
import time
import threading
import tkinter as tk

class AutoClicker():
    def __init__(self, cps, hotkey):
        self.cps = cps
        self.hotkey = hotkey
        self.clicking = True
        self.listening = False
        self.thread = None
        self.mouse = pynput.mouse.Controller()
        self.hotkey_handle = None
    
    def toggle(self):
        if self.clicking:
            self.clicking = False
        else:
            self.clicking = True
            self.thread = threading.Thread(target=self.click_loop).start()
    
    def stop(self):
        self.clicking = False
        if self.hotkey_handle:
            keyboard.remove_hotkey(self.hotkey_handle)
            self.hotkey_handle = None

        
    def click_loop(self):
        delay = 1 / (self.cps)
        while self.clicking:
            self.mouse.click(pynput.mouse.Button.left, 1)
            time.sleep(delay)
            
    def start_listening(self):
        if self.hotkey_handle:
            keyboard.remove_hotkey(self.hotkey_handle)
        self.hotkey_handle = keyboard.add_hotkey(self.hotkey, self.toggle)


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


def start_clicking():
    clicker.cps = int(cps_input.get())
    clicker.hotkey=hotkey_input.hotkey
    threading.Thread(target=clicker.start_listening, daemon=True).start()
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Autoclick")
    
    #Choose cps
    cps_frame = tk.Frame(root)
    cps_frame.grid(row=0, column=0, padx=100, pady=5)
    
    cps_label = tk.Label(cps_frame, text="CPS: ")
    cps_label.pack(side="left")
    
    cps_input = tk.Spinbox(cps_frame, from_=1, to=100, width=3)
    cps_input.insert(1, "0")
    cps_input.pack(side="left")
    
    #Hotkey
    hotkey_input = HotkeySelector(root, row=1, column=0, padx=10, pady=5)
    
    #Start Button
    clicker = AutoClicker(cps=10, hotkey="Q")
    start_button = tk.Button(root, text="Start", command=start_clicking)
    start_button.grid(row=2, column=0, padx=20, pady=5)
    
    #Stop Button
    stop_button = tk.Button(root, text="Stop", command=clicker.stop)
    stop_button.grid(row=3, column=0, padx=20, pady=5)
    
    root.mainloop()

    