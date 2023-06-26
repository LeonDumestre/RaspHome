import datetime


def format_current_time():
    return datetime.datetime.now().strftime("%H:%M")


def format_current_date():
    return datetime.datetime.now().strftime("%d/%m/%Y")


def update_time(label):
    label.configure(text=format_current_time())
    label.after(1000, lambda: update_time(label))