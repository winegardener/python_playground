import tkinter as tk
from StateMachine import StateMachine
import threading
import time

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("State Machine GUI")
        
        self.state_machine = StateMachine(["Init", "Preparing", "Off", "Running", "Crash"])
        self.state_machine.print_debug(False)
        
        self.label_state = tk.Label(self, text="Current State: " + self.state_machine.state())
        self.label_state.pack()

        self.button_start = tk.Button(self, text="Start", command=self.start_button_click, state=tk.NORMAL if self.state_machine.is_state("Off") else tk.DISABLED)
        self.button_start.pack()

        self.button_stop = tk.Button(self, text="Stop", command=self.stop_button_click, state=tk.NORMAL if self.state_machine.is_state("Running") else tk.DISABLED)
        self.button_stop.pack()

        self.button_error = tk.Button(self, text="Fehler", command=self.error_button_click)
        self.button_error.pack()

        self.update_gui()

    def update_gui(self):
        self.label_state.config(text="Current State: " + self.state_machine.state())
        
        if self.state_machine.is_state("Off"):
            self.button_start.config(state=tk.NORMAL)
            self.button_stop.config(state=tk.DISABLED)
        elif self.state_machine.is_state("Running"):
            self.button_start.config(state=tk.DISABLED)
            self.button_stop.config(state=tk.NORMAL)

        self.after(100, self.update_gui)

    def start_button_click(self):
        if self.state_machine.is_state("Off"):
            self.state_machine.change_to("Preparing")

    def stop_button_click(self):
        if self.state_machine.is_state("Running"):
            print("Stop button clicked")
            self.state_machine.change_to("Off")

    def error_button_click(self):
        self.state_machine.force_to("Crash")

if __name__ == "__main__":
    app = GUI()

    while True:
        if app.state_machine.is_state("Init"):
            if app.state_machine.entry_state():
                pass
            pass      
            time.sleep(1)
            app.state_machine.change_to("Preparing")    
            if app.state_machine.exit_state():
                pass
        
        elif app.state_machine.is_state("Preparing"):
            if app.state_machine.entry_state():
                pass
            pass
            time.sleep(1)
            app.state_machine.change_to("Running")
            if app.state_machine.exit_state():
                pass
        
        elif app.state_machine.is_state("Off"):
            if app.state_machine.entry_state():
                pass
            pass
            if app.state_machine.exit_state():
                pass
        
        elif app.state_machine.is_state("Running"):
            if app.state_machine.entry_state():
                pass
            pass
            if app.state_machine.exit_state():
                pass
        
        elif app.state_machine.is_state("Crash"):
            if app.state_machine.entry_state():
                pass
                print("Notbremse aktiviert")
            pass
            time.sleep(1)
            app.state_machine.change_to("Off")
            if app.state_machine.exit_state():
                pass
        
        app.update_gui()
        app.update()
