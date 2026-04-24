# import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2
from psycopg2.extras import RealDictCursor

SQLALCHEMY_DATABASE_URL = "postgresql://rui:password123@localhost:5432/iphone_management"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_connection():
    return psycopg2.connect(host = "localhost",
                            database = "iphone_management",
                            user = "rui",
                            password = "password123",
                            port = 5432,
                            cursor_factory = RealDictCursor)


# def init_database():
#     connect = get_connection()
#     cursor = connect.cursor()

#     cursor.execute('''
#                CREATE TABLE IF NOT EXISTS iphones(
#                   id SERIAL PRIMARY KEY,
#                   version TEXT,
#                   serialNumber TEXT,
#                   userID INTEGER UNIQUE,
#                   userName TEXT,
#                   phoneNumber TEXT,
#                   birthDay TEXT,
#                  );
#                ''')
#     cursor.execute('''
#                  CREATE TABLE IF NOT EXISTS deleted_iphones(
#                    id SERIAL PRIMARY KEY,
#                    userID INTEGER UNIQUE,
#                    userName TEXT
#                    );
#                  ''')
    
#     cursor.execute('''
#                   CREATE TABLE IF NOT EXISTS workers(
#                    id SERIAL PRIMARY KEY,
#                    workerID: TEXT
#                    country: TEXT
#                    age: TEXT
#                    salary: TEXT
#                    );
#                   ''')
#     print("Successfully the postgreSQL is added for the database")
#     connect.commit()
#     connect.close()
#     connect.close()
#     connect.close()
    

