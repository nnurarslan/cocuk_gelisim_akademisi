import pymongo


class ConnectDatabase:
    def __init__(self):
        self._host = "localhost"
        self._port = 27017
        self._database = "student_db"
        self._connection = None
        self._collection = None

    def connect_db(self, collection):
        self._connection = pymongo.MongoClient(self._host, self._port)
        database = self._connection[self._database]
        self._collection = database[collection]

    def login(self, data):
        self.connect_db("login")
        user = self._collection.find_one(data)
        return user

    def get_single_data(self, student_id):
        self.connect_db("info")
        data = self._collection.find_one({'student_id': student_id})
        return data

    def add_info(self, student_data):
        self.connect_db("info")
        document = self._collection.insert_one(student_data)
        return document.inserted_id

    def search_info(self, data):
        # Connect to the database
        self.connect_db("info")
        query = {}

        if data["student_id"]:
            query["student_id"] = {"$regex": f".*{data['student_id']}.*", "$options": "i"}
        if data["first_name"]:
            query["first_name"] = {"$regex": f".*{data['first_name']}.*", "$options": "i"}
        if data['last_name']:
            query["last_name"] = {"$regex": f".*{data['last_name']}.*", "$options": "i"}
        if data['email']:
            query["email"] = {"$regex": f".*{data['email']}.*", "$options": "i"}

        print(query)
        if query:
            # Koşullarla bilgi aramak için bir MongoDB sorgusu oluştur
            results = self._collection.find(query)
            return list(results)
        else:
            # Tüm bilgiyi aramak için bir MongoDB sorgusu oluştur
            results = self._collection.find()
            return list(results)

    def delete_info(self, student_id):
        self.connect_db("info")
        try:
            document = self._collection.delete_one({'student_id': student_id})
            print(document)
            return document.acknowledged
        except Exception as E:
            self._connection.rollback()
            return E
        finally:
            self._connection.close()

    def update_info(self, data):
        self.connect_db("info")
        print(data)
        try:
            document = self._collection.update_one({'student_id': data['student_id']},
                                                   {"$set": data}, upsert=True)
            return document.acknowledged
        except Exception as E:
            self._connection.rollback()
            return E
        finally:
            self._connection.close()
