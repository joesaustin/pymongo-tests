from pymongo import MongoClient
import basic_functions, unittest

class InsertBulkDocuments(unittest.TestCase):
    def setUp(self):
        self.mongo_functions = basic_functions.MongoFuctions()
        self.client = self.mongo_functions.client
        self.db = self.client.testdb #if the db does not already exist, it will be created

    def test_bulk_inserts(self):
        #create x number of documents and place them into a list
        existing_docs = self.db.bulk_users.count()
        new_docs = 25        
        user_data = []
        ids = []
        
        for i in range(0,new_docs):
            user_data.append(self.mongo_functions.generate_user_data())
        
        #bulk insert all documents in user_data to the bulk_users db
        post = self.mongo_functions.post_to_collection(self.db.bulk_users, user_data) #db.users points to the collection users in the database. if it does not exits it will be created

        #verify the records now exist in the collection
        for i in range(0,len(user_data)):
            try:
                result = post.find_one({'email':user_data[i]['email']})
                ids.append(result['_id']) # collect the ObjectId of each document inserted
                self.assertEqual(user_data[i]['email'], result['email'])
            except:
                print "Failed! Cannot find document in collection where email = %s" %(user_data[i]['email'])
                
        #lets make sure the count of documents in the database is correct
        try:
            self.assertEqual(self.db.bulk_users.count(), (new_docs + existing_docs))
        except:
            print "number of documents is incorrect in the database"
            
        #delete only the documents that where inserted by this test.
        try:
            self.db.bulk_users.remove({ "_id": { "$in" : ids}})
            self.assertEqual(existing_docs, self.db.bulk_users.count())
        except:
            print "Failed verifying final count after data clean up. Check data in error file and verify it is not in the db"
            self.mongo_functions.write_data_to_file(self.__class__.__name__,user_data)
        
        
    def tearDown(self):
        print "Test Done."    

if __name__ == "__main__":
    unittest.main()