import tkinter
import customtkinter
from date_utils import *

# System settings
customtkinter.set_appearance_mode("dark")

# App frame
app = customtkinter.CTk()
app.geometry("640x480")
app.title("RaspHome")

# App elements
time = customtkinter.CTkLabel(app, font=("Chandas", 100))
update_time(time)
time.pack()

# Run app
app.mainloop()
