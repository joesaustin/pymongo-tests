from faker import Factory
from bson import ObjectId
from pymongo import MongoClient
import json, time

class MongoFuctions():
    def __init__(self):
        self.client = MongoClient('localhost',27017)# connect to your local running instance of mongo
        self.fake = Factory.create()
    
    def post_to_collection(self, collection, collection_data):
        post = collection #if the collection does not already exist it will be created.
        post.insert(collection_data)
        return post
    
    def generate_user_data(self):
        fname = self.fake.first_name()
        lname = self.fake.last_name()
        street = self.fake.street_address()
        city = self.fake.city()
        state = self.fake.state()
        zip = self.fake.zipcode()
        email = self.fake.email()
        
        user_data = {'first_name' : fname,
                     'last_name' : lname,
                     'address':{'street': street,
                                'city': city,
                                'state': state,
                                'zip' : zip},
                     'email' : email}
        return user_data
        
    def write_data_to_file(self, class_name, data):
        encoder = JSONEncoder()
        data = encoder.encode(data) 
        filename = class_name+"_"+time.strftime("%Y-%m-%d_%H-%M-%S")+".txt"
        with open(filename, 'wb') as fo:
            json.dump(data, fo)
            fo.close
    
    def import_data_from_file(self, file_name):
        file_data = open(file_name)
        data = json.load(file_data)
        file_data.close()
        return data
    
    
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


        
    