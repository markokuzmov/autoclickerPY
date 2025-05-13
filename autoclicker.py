import pynput
import keyboard
import threading
import time

class AutoClicker():
    def __init__(self, cps, hotkey):
        self.cps = cps
        self.hotkey = hotkey
        self.clicking = False
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
