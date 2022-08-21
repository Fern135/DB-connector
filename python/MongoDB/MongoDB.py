import pymongo
import json


class MongoDB:

    def __init__(self, db_host:str, db_port:str, db_name:str, col_name:str):
        self.myclient = pymongo.MongoClient(f"mongodb://{db_host}:{db_port}/")

        # checking if the db exists
        dblist = self.myclient.list_database_names()

        if db_name in dblist:
            return json.dumps(
                {
                    "Server": "The database exists."
                }
            )
        else:
            # making the db
            self.mydb = self.myclient[db_name]

            # checking if the table / collection exists
            collist = self.mydb.list_collection_names()

            if col_name in collist:
                return json.dumps(
                    {
                        "Server": "The Collection exists."
                    }
                )
            else:
                self.main_col = self.mydb[col_name]


    def insert(self, data=None):
        """Inserting 1 dictionary or aka json

        Keyword arguments:
            data -- data being inserted. Dictionary expected. aka json
        """
        try:
            if data is None:
                data={}

            self.mycol.insert_one(data)
        except Exception as e:
            print(f"Exception: {str(e)}")


    def insert_many(self, data=None):
        """Inserting many dicts (json) in an array (list [python])

        Keyword arguments:
            data -- data being inserted. Inserting many dicts (json) in an array (list [python])
        """
        try:
            if data is None:
                data=[{}]

            self.mycol.insert_many(data)
        except Exception as e:
            print(f'Exception: {str(e)}')


    def find_one(self):
        """Finding just one from the collection

        Keyword arguments:
            Return: the one file collection. AKA the data
        """
        try:
            return self.mycol.find_one()
        except Exception as e:
            print(f'Exception: {str(e)}')


    def find_all(self):
        """Finding all from the collection

        Keyword arguments:
            Return: the all from collection. AKA the data
        """
        try:
            for x in self.mycol.find():
                return x
        except Exception as e:
            print(f'Exception: {str(e)}')


    def find_all(self, sort_by:str, sort=None):
        """Finding all from the collection

        Keyword arguments:
            sort -- sor by ascending (1: Default is 1),  descending (-1) 
            Return: the all from collection sorted ascending. Descending if sort is set to -1. AKA the data
        """
        try:
            if sort == -1:
                for x in self.mycol.find().sort(sort_by, -1):
                    return x
            else:
                for x in self.mycol.find().sort(sort_by):
                    return x

        except Exception as e:
            print(f'Exception: {str(e)}')


    def find_all(self, limit=None):
        """Finding all from the collection

        Keyword arguments:
            Return: the all from collection sorted ascending. Descending if sort is set to -1. AKA the data
        """
        try:
            if limit >= 1:
                myresult = self.mycol.find().limit(limit)

                # print the result:
                for x in myresult:
                    return x

            else:
                myresult = self.mycol.find().limit(limit)

                # print the result:
                for x in myresult:
                    return x

        except Exception as e:
            print(f'Exception: {str(e)}')



    def find_spc(self, data=None):
        """Finding specific from the collection

        Keyword arguments:
            data -- json object or python dict
            Return: the specific from collection. AKA the data
        """
        try:
            if data is None:
                data={}

            for x in self.mycol.find({}, data):
                dataFound = x

            return dataFound
        except Exception as e:
            print(f'Exception: {str(e)}')


    def query(self, data=None):
        """querying specific from the db

        Keyword arguments:
            data -- quering for the colelction 
            Return: the data from collection
        """
        try:
            if data is None:
                data={}

            mydoc = self.mycol.find(data)

            for x in mydoc:
                dataFound = x

            return dataFound
        except Exception as e:
            print(f'Exception: {str(e)}')


    def del_one(self, data=None):
        """Delete specific sections of the collection

        Keyword arguments:
            data -- data being deleted
        """
        try:
            if data is None:
                data = {}

            self.mycol.delete_one(data)
        except Exception as e:
            print(f'Exception: {str(e)}')


    def update(self, data_old=None, data_new=None, many=False, Modified_count=False):
        try:
            if data_old is None and data_new is None:
                data_old={}
                data_new={}

            if many:
                myquery = data_old
                newvalues = {"$set": data_new}

                self.mycol.update_one(myquery, newvalues)

            elif many == True:
                # setting alot of updates of the collection
                myquery = {data_old: {"$regex": "^S"}}
                newvalues = {"$set": data_new}

                x = self.mycol.update_many(myquery, newvalues)

                if Modified_count:
                    pass
                else:
                    return int(x.modified_count)
        except Exception as e:
            print(f"Exception: {str(e)}")


    def del_all(self):
        # deletes all records.
        try:
            self.mycol.delete_many({})
        except Exception as e:
            print(f'Exception: {str(e)}')


    def drop(self):
        # You can delete a table, or collection as it is called in MongoDB
        try:
            self.mycol.drop()
        except Exception as e:
            print(f'Exception: {str(e)}')
