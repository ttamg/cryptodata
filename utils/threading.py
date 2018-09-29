import threading

def run_threaded(job_func, kwargs_dict):
    """
    Function to wrap a function in a threaded wrapper
    :param job_func: The function to be called
    :param kwargs_dict: A dictionary of kwargs to be passed to the function
    :return: None
    """
    job_thread = threading.Thread(target=job_func, kwargs=kwargs_dict)
    job_thread.start()
    return None
