from pymongo import MongoClient
import basic_functions, unittest

class InsertFromFile(unittest.TestCase):
    def setUp(self):
        self.mongo_functions = basic_functions.MongoFuctions()
        self.client = self.mongo_functions.client
        self.db = self.client.testdb #if the db does not already exist, it will be created

    def test_inserts_from_file(self):
        data = self.mongo_functions.import_data_from_file('test_data.txt')
        self.mongo_functions.post_to_collection(self.db.test_accounts, data)
        
    def tearDown(self):
        #self.db.test_accounts.remove({}) #lets empty the db of any records
        print "Test Done."    

if __name__ == "__main__":
    unittest.main()