from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
import os
from datetime import datetime
from pathlib import Path


class FirebaseDatabase:

    def __init__(self, collection, user_document, db_attribute):
        sdk = Path(__file__).parent.parent / "data/adminSDK.json"
        cred = credentials.Certificate(sdk)
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://myovest.firebaseio.com'
        })
        self.db = firestore.client()
        self.collection = collection
        self.user_document = user_document
        self.db_attribute = db_attribute
        # self.initialize_db()

    def initialize_db(self):
        coll_ref = self.db.collection(u"{}".format(self.collection))
        doc_ref = coll_ref.document(u"{}".format(self.user_document))
        doc_ref.set(self.db_attribute, merge=True)

    def update_child(self, key, value):
        coll_ref = self.db.collection(u"{}".format(self.collection))
        doc_ref = coll_ref.document(u"{}".format(self.user_document))
        doc_ref.set({
            key: value
        }, merge=True)

    def update_some_child(self, dic):
        for key in dic:
            self.update_child(key, dic[key])


# x = {"name": "John", "age": 30, "city": "New York"}
# y = {"name": "omar", "age": 141}
# datab = FirebaseDatabase("myovest", "test12", x)
# datab.update_some_child(y)
