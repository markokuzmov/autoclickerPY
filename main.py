import tkinter as tk
from autoclicker import AutoClicker
from hotkey_selector import HotkeySelector
import threading

def start_clicking():
    root.focus()
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
    
    cps_input = tk.Spinbox(cps_frame, from_=1, to=1000, width=5)
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