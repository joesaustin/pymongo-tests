from pymongo import MongoClient
import basic_functions, unittest, re

class SortData(unittest.TestCase):
    def setUp(self):
        self.mongo_functions = basic_functions.MongoFuctions()
        self.client = self.mongo_functions.client
        self.db = self.client.testdb #if the db does not already exist, it will be created

    def test_inserts_from_file(self):
        '''If you haven already, make sure to run the load_test_data_from_file.py script so you have data to play with in this collection!'''
        
        documents = self.db.test_accounts
        
        print "Return only 3 documents in the collection"
        print "============================================="
        for doc in documents.find().limit(3):print doc
        
        print "\nReturn the first 3 records in alphabetic ascending order"
        print "=========================================================="
        for doc in documents.find().limit(3).sort("last_name", 1):print doc
        
        print "\nReturn the first 3 records in alphabetic descending order"
        print "==========================================================="
        for doc in documents.find().limit(3).sort("last_name", -1):print doc
        
        print "\nSearch for documents where last name starts with Ho"
        print "====================================================="
        regex = re.compile('Ho*')
        for doc in documents.find({"last_name": regex}):print doc
        
        print "\nReturn only the email fields that end with .com and don't show the ObjectId"
        print "================================================="
        regex = re.compile('\.com$')
        for doc in documents.find({"email":regex}, {"email":1, '_id':0}):print doc
        
    def tearDown(self):
        print "Test Done."    

if __name__ == "__main__":
    unittest.main()