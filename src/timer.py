import tkinter as tk

def start_countdown(seconds):
    def countdown(seconds_remaining):  
        if seconds_remaining > 0:
            # Properly divide and convert
            minutes, sec = divmod(seconds_remaining, 60)
            minutes = int(minutes)
            sec = int(sec)
            time_format = '{:02d}:{:02d}'.format(minutes, sec)
            label.config(text=time_format)
            # Schedule the countdown function to run again in 1 second
            root.after(1000, countdown, seconds_remaining - 1)
        else:
            label.config(text="mob's down!")

    root = tk.Tk()
    label = tk.Label(root, font=('Helvetica', 48), text="")
    label.pack()
    countdown(seconds)  
    root.mainloop()