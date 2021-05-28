import pyrebase


class FirebaseDatabase

   firebaseConfig = {
        "apiKey": "AIzaSyB2NljfGaOMR_EQY0-sy8BU",
        "authDomain": "my-weathirebaseapp.com",
          "databaseURL": "https://my-weather-de081.firebaseio.com",
          "projectId": "my-w",
          "storageBucket": "my-.appspot.com",
          "messagingSenderId": "57"
          "appId": "1:57066dbeca2840f5d9e0b148"
        }

       def __init__(self):
            self.db = pyrebase.initialize_app(firebaseConfig)

        def update_child(child, data):
            print('update', child, ':', data)
            db.child(child).update(data)
    