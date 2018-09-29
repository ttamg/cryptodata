import datetime


def unixtime_period(seconds):
    """
    Function to provide a signal that a new period has started following a number of seconds
    :param seconds:
    :return: period number (integer)
    """
    return int(datetime.datetime.now().timestamp() / seconds)

