import mysql.connector
import json


class Mysql:

    def __init__(self, host:str, username:str, password:str, database:str):
        self.db = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

        self.mycursor = self.db.cursor()


    def query(self, query:str) -> None:
        """
            run any query to the db. Not reccomended unless you know what you're doing

        Keyword arguments:
            query -- sql query to run
        """

        try:
            # execute any query
            self.mycursor.execute(query)
        except Exception as e:
            print(f'Exception: {str(e)}')
            return str(e)


    def insert(self, table_name:str, col_table=None, placeholder="%s", col_val_insert=None, data=None) -> any:
        """insert specific to the db ONLY

        Keyword arguments:
            table_name -- the table name to insert data to
            col_table -- the row on the table to be modified. TUPLE expected
            placeholder -- prevents sql injection
            col_val_insert -- the values to replace on the row specified by col_table. TUPLE expected
            data -- data being inserted. TUPLE expected
            Return: json with information, or an exception
        """

        try:

            if col_table is None and col_val_insert is None and data is None:
                col_table       = ()
                col_val_insert  = ()
                data            = ()

            query = f'INSERT INTO {table_name} ({col_table}) VALUES ({placeholder})'

            da = (col_val_insert,)

            # execute to the db
            self.mycursor.execute(query, da)

            # committing so there's changes made in the database
            db_commit = self.mydb.commit()

            if db_commit:
                return json.dumps(
                    {
                        "DB commit": True
                    }
                )
            else:
                return json.dumps(
                    {
                        "DB commit": False
                    }
                )

        except Exception as e:
            print(f'Exception: {str(e)}')
            return str(e)


    def select(self, table_name:str, fetch="all", rows='*'):
        """Select from the specific table in the database. row is * (all by default)

        Keyword arguments:
            table_name -- the table name to be selected from
            row -- defaulted to * (all), can be changed. Expected str
            fetch -- which to fetch. Default to all
            return: data from selected table
        """

        try:
            sql = f"SELECT {rows} FROM {table_name}"

            self.mycursor.execute(sql)

            result = self.mycursor.fetchall()

            if fetch:
                for data in result:
                    return data
            elif fetch == 'one':
                return self.mycursor.fetchone()

        except Exception as e:
            print(f'Exception: {str(e)}')
            return str(e)


    def select_keyW(self, table_name:str, placeholder='%s', row=None, data=None, fetch="all", rows='*'):
        """Select from the specific table in the database. row is * (all by default). and where is to be especific

        Keyword arguments:
            table_name -- the table name to be selected from
            rows -- rows to be selected from. tuples expected
            data -- data being selected specifically from the rows.
            row -- defaulted to * (all), can be changed. Expected str
            fetch -- which to fetch from the query. Default to all
            return: data from selected table
        """
        try:
            if row is None and data is None:
                row  = ()
                data = ()

            sql = f"SELECT {rows} FROM {table_name} WHERE {row} LIKE {placeholder}"
            adr = (data, )

            self.mycursor.execute(sql, adr)

            result = self.mycursor.fetchall()

            if fetch:
                for data in result:
                    return data
            elif fetch == 'one':
                return self.mycursor.fetchone()

        except Exception as e:
            print(f'Exception: {str(e)}')
            return str(e)


    def select_order(self, table_name:str, ordered_by:str, ordered:str, rows="*"):
        """Select from the specific table in the database. row is * (all by default)

        Keyword arguments:
            table_name -- the table name to be selected from
            ordered_by -- data to order the information being selected by
            ordered -- descending or ascending
            row -- defaulted to * (all), can be changed. Expected str
            return: data from selected table
        """

        try:
            sql = f"SELECT {rows} FROM {table_name} ORDER BY {ordered_by} {ordered}"

            self.mycursor.execute(sql)

            result = self.mycursor.fetchall()

            for data in result:
                return data

        except Exception as e:
            print(f'Exception: {str(e)}')
            return str(e)


    def delete(self, table_name:str, to_delete:str, data:str, placeholder="%s"):
        """delete specific information from the db

        Keyword arguments:
            table_name -- table to choose from to delete from
            to_delete -- information to delete
            data -- data being deleted. At least it should
            placeholder -- to prevent sql injection
        """
        try:
            sql = f"DELETE FROM {table_name} WHERE {to_delete} = {placeholder}"
            info = (data,)

            self.mycursor.execute(sql, info)
            self.mydb.commit()

        except Exception as e:
            print(f"exception: {str(e)}")
            return str(e)


    def update(self, table_name:str, data_to_Change:str, old_data_to_Change:str, new_data_to_Change:str, placeholder="%s"):
        """"sumary_line

        Keyword arguments:
            table_name -- table selected
            data_to_change -- selecting the data to change on the db 
            old_data_to_change -- old data on the db to better select it
            new_data_to_Change -- new data being updated
            placeholder -- prevents sql injection
        """
        try:
            sql = f"UPDATE {table_name} SET {data_to_Change} = {placeholder} WHERE {data_to_Change} = {placeholder}"
            val = (old_data_to_Change, new_data_to_Change)

            self.mycursor.execute(sql, val)

            self.mydb.commit()

        except Exception as e:
            print(f'exception: {str(e)}')
            return str(e)


    def select_limit(self, table_name:str, limit:int, offset=None, fetch="all", rows='*'):
        """Select from the specific table in the database. row is * (all by default)

        Keyword arguments:
            table_name -- the table name to be selected from
            rows -- defaulted to * (all), can be changed. Expected str
            limit -- how many to fetch
            offset -- starting with a specific section
            fetch -- which to fetch. Default to all
            return: data from selected table
        """

        try:
            if offset != None:
                sql = f"SELECT {rows} FROM {table_name} LIMIT {limit} OFFSET {offset}"

                self.mycursor.execute(sql)
                result = self.mycursor.fetchall()

                if fetch:
                    for data in result:
                        return data
                elif fetch == 'one':
                    return self.mycursor.fetchone()

            else:
                sql = f"SELECT {rows} FROM {table_name} LIMIT {limit}"

                self.mycursor.execute(sql)
                result = self.mycursor.fetchall()

                if fetch:
                    for data in result:
                        return data
                elif fetch == 'one':
                    return self.mycursor.fetchone()

        except Exception as e:
            print(f'Exception: {str(e)}')
            return str(e)


    def drop_table(self, table_name:str):
        # drops all the information on the table
        try:
            sql = f"DROP TABLE IF EXISTS {table_name}"

            self.mycursor.execute(sql)
        except Exception as e:
            print(f"Exception: {str(e)}")
            return str(e)
