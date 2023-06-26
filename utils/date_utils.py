import datetime


def get_current_time():
    return datetime.datetime.now()


def format_current_time():
    return get_current_time().strftime("%H:%M")


def format_current_date():
    return get_current_time().strftime("%d/%m/%Y")


def update_time(label):
    label.configure(text=format_current_time())
    label.after(1000, lambda: update_time(label))