import logging
import sqlite3

class Contacts:
    def __init__(self, db_path='base.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        sqlite_create_table_query = """
            CREATE TABLE
            if not exists

            people (
                id INTEGER PRIMARY KEY,
                name TEXT ,
                father_name TEXT ,
                last_name TEXT ,
                phone TEXT ,
                comment TEXT 
            );
        """

        conn.execute(
            sqlite_create_table_query
        )
        conn.close()

    def query(self, query, data):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
        conn.close()

    def insert_person(self, data):
        insert_query = 'INSERT INTO people (name ,father_name ,last_name, phone, comment ) VALUES(?,?,?,?,?)'
        self.query(insert_query, data)
        logging.info(f'Добавление записи: {data}')

    def insert_persons(self, data):
        insert_query = 'INSERT INTO people (name ,father_name ,last_name, phone, comment ) VALUES(?,?,?,?,?)'
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.executemany(insert_query, data)
        conn.commit()
        conn.close()
        logging.info(f'Добавление записей: {data}')

    def update_person(self, data, id):
        log_data = self.get_record('people', id)
        update_query = 'UPDATE people set name=? ,father_name=? ,last_name=?, phone=?, comment=?  WHERE id=?'
        update_tuple = list(data)
        update_tuple.append(id)
        data_and_id = tuple(update_tuple)
        self.query(update_query, data_and_id)
        logging.info(f'Обновление записи №{id} было {log_data} стало {data}')

    def get(self, table):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        get_query = f'SELECT * FROM {table}'
        data = cur.execute(get_query)
        data_tuple = [tuple(i) for i in data]
        conn.close()

        return data_tuple

    def get_record(self, table, id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        get_query = f'SELECT * FROM {table} WHERE id={id}'
        data = cur.execute(get_query).fetchone()
        conn.close()
        return data
    
    def delete(self,table,id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor() 
        log_data = self.get_record(table,id)
        delete_query = f'DELETE FROM {table} WHERE id={id}'
        cur.execute(delete_query)
        conn.commit()
        conn.close()
        logging.info(f'Удаление записи №{id} данные:{log_data}')
