import basic_functions
from faker import Factory
from pymongo import MongoClient
import unittest

class InsertRandomDocument(unittest.TestCase):
    def setUp(self):
        self.mongo_functions = basic_functions.MongoFuctions()
        self.client = self.mongo_functions.client

    def test_inserts(self):
        user_data = self.mongo_functions.generate_user_data()
        db = self.client.testdb #if the db does not already exist, it will be created
        post = self.mongo_functions.post_to_collection(db.users, user_data) #db.users points to the collection users in the database. if it does not exits it will be created
        
        #verify the record now exist in the collection
        try:
            result = post.find_one({'email':user_data['email']})
            self.assertEqual(user_data['email'], result['email'], "cannot find record in collection where last_name = % s" %(user_data['email']))
        except:
            print "Failed! Cannot find record in collection where email = % s" %(user_data['email'])
        
    def tearDown(self):
        print "Test Done."    

if __name__ == "__main__":
    unittest.main()
    
