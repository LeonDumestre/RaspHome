import datetime

FOUR_HOURS_IN_SEC = 4 * 60 * 60


def get_current_time():
    return datetime.datetime.now()


def format_current_time():
    return get_current_time().strftime("%H:%M")


def format_current_date():
    return get_current_time().strftime("%d/%m/%Y")
