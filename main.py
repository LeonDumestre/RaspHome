import customtkinter as ctk

from api.weather.weather_stack import run_weather_stack_api_loop
from utils.date_utils import *
from themes.color import *

run_weather_stack_api_loop()

# System settings
ctk.set_appearance_mode("dark")

# App frame
app = ctk.CTk()
app.geometry("640x480")
app.title("RaspHome")
app.configure(fg_color=background_color)

# App elements
time = ctk.CTkLabel(app, font=("Chandas", 200))
update_time(time)
time.pack(pady=30)

bottom_frame = ctk.CTkFrame(app, fg_color=background_color)

temp = ctk.CTkLabel(bottom_frame, text="20°C", font=("Chandas", 60))
humidity = ctk.CTkLabel(bottom_frame, text="10%", font=("Chandas", 60))

temp.pack(side="left", expand=True, padx=10)
humidity.pack(side="left", expand=True, padx=10)
bottom_frame.pack(side="bottom", fill="both", pady=10)

# Run app
app.mainloop()
