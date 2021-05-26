

def check_wifi_connection():
    return True


def run():
    while True:
        is_fall = accerlation.get_is_fall()
        is_wifi_connect = check_wifi_connection()
        if is_wifi_connect:
            return True
            # TODO : call module to update our database
        else:
            return True


def test():
    print("alert")
