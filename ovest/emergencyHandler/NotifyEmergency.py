import http.client as httplib


class NotifyEmergency:
    def __init__(self):
        pass

    def check_internet_connection(self):
        connection = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            # only header requested for fast operation
            connection.request("HEAD", "/")
            connection.close()  # connection closed
            print("Internet On")
            return True
        except Exception as exep:
            print(exep)
            return False
