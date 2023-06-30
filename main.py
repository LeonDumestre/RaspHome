from ui.window import Window
from api.weather import run_weather_stack_api_loop
from threading import Thread

window = Window()

api_thread = Thread(target=run_weather_stack_api_loop)
ui_thread = Thread(target=window.update_ui)

api_thread.start()
ui_thread.start()

window.run()
