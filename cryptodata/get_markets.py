

def get_markets(api):
    """
    Prints the market pairs for all exchanges passed to the function
    :param exchanges object:
    :return: get_markets response
    """
    return api.get_markets()