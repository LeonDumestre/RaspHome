from customtkinter import *
from ui.color import *
from utils.date_utils import *
import time


class Window:
    app = CTk()
    time_label = None
    temp_label = None
    humidity_label = None

    def __init__(self):
        set_appearance_mode("dark")

        # App frame
        self.app.geometry("640x480")
        self.app.title("RaspHome")
        self.app.configure(fg_color=background_color)

        # App elements
        self.time_label = CTkLabel(self.app, text=format_current_time(), font=("Chandas", 200))
        self.time_label.pack(pady=30)

        bottom_frame = CTkFrame(self.app, fg_color=background_color)

        self.temp_label = CTkLabel(bottom_frame, text="20°C", font=("Chandas", 60))
        self.humidity_label = CTkLabel(bottom_frame, text="10%", font=("Chandas", 60))

        self.temp_label.pack(side="left", expand=True, padx=10)
        self.humidity_label.pack(side="left", expand=True, padx=10)
        bottom_frame.pack(side="bottom", fill="both", pady=10)

    def run(self):
        self.update_time()
        self.app.mainloop()

    def update_time(self):
        self.time_label.configure(text=format_current_time())
        self.time_label.after(100, lambda: self.update_time())

    def update_ui(self):
        while True:
            temp, humidity = "20°C", "10%"
            self.temp_label.configure(text=temp)
            self.humidity_label.configure(text=humidity)

            # Lire la température à partir du capteur et la mettre à jour dans l'interface graphique
            # temperature = read_temperature()
            # temp_sensor_label.configure(text=temperature)

            time.sleep(3)
