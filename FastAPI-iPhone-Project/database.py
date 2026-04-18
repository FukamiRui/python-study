import sqlite3

def get_connection():

    connect = sqlite3.connect("iphone.db")
    connect.row_factory = sqlite3.Row 
    return connect

def init_database():
    connect = get_connection()
    cursor = connect.cursor()

    cursor.execute('''
               CREATE TABLE IF NOT EXISTS iphones(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  version REAL,
                  serialNumber INTEGER,
                  userID INTEGER,
                  userName TEXT
                  phoneNumber INTEGER
                  birthDay INTEGER
                 )
               ''')
    cursor.execute('''
                 CREATE TABLE IF NOT EXISTS deleted_iphones(
                   id INTEGER PRIMARY KEY AUTOINCREMENT
                   userID INTEGER
                   userName TEXT)
                 ''')
    
    cursor.execute('''
                  CREATE TABLE IF NOT EXISTS workers(
                   id INTEGER PRIMARY KEY AYTOINCREMENT,
                   workerID: INTERGER
                   country: TEXT
                   age: INTEGER
                   salary: str)
                  ''')
    
    connect.commit()
    connect.close()
    
