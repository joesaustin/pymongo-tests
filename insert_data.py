import basic_functions
from faker import Factory
from pymongo import MongoClient
import unittest

class InsertRandomDocument(unittest.TestCase):
    def setUp(self):
        self.mongo_functions = basic_functions.MongoFuctions()
        self.client = self.mongo_functions.client
        self.db = self.client.testdb #if the db does not already exist, it will be created

    def test_individual_inserts(self):
        documents = 10        
        for i in range(0,documents):
            user_data = self.mongo_functions.generate_user_data()
            post = self.mongo_functions.post_to_collection(self.db.individual_users, user_data) #db.users points to the collection users in the database. if it does not exits it will be created
        
            #verify the record now exist in the collection
            try:
                result = post.find_one({'email':user_data['email']})
                self.assertEqual(user_data['email'], result['email'], "cannot find record in collection where last_name = % s" %(user_data['email']))
            except:
                print "Failed! Cannot find record in collection where email = % s" %(user_data['email'])
                
        #lets make sure the count of documents in the database is correct
        try:
            self.assertEqual(self.db.individual_users.count(), documents, "number of documents is incorrect in the database")
        except Exception:
            print "Error, here are all the records in the collection"
            for doc in post.find(): print doc
        
    def tearDown(self):
        self.db.individual_users.remove({}) #remove all the records in the DB
        print "Test Done. Test data was removed"    

if __name__ == "__main__":
    unittest.main()
    
