from faker import Factory
from pymongo import MongoClient

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
        email = self.fake.email()
        
        user_data = {'first_name' : fname,
                     'last_name' : lname,
                     'email' : email}
        return user_data
        

        
        
    