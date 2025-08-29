import psycopg2
from psycopg2.extras import RealDictCursor

def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="Ayobami@090499",
            cursor_factory = RealDictCursor   
        )
        cursor = conn.cursor()
        print("Database connection was successful")
    except Exception as error:
        print("Database connection failed")
        print("Error:", error)