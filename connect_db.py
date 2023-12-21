import pymongo


class ConnectDatabase:
    def __init__(self):
        self._host = "localhost"
        self._port = 27017
        self._database = "student_db"
        self._connection = None
        self._collection = None
        print("1111")

    def connect_db(self, collection):
        self._connection = pymongo.MongoClient(self._host,self._port)
        database = self._connection[self._database]
        self._collection = database[collection]
        print("baglandi")

    def login(self,data):
        print(data)
        self.connect_db("login")
        user = self._collection.find_one(data)
        print("geldiiii")
        print(user)
        return user

