from contextlib import contextmanager
import psycopg2
from env import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


@contextmanager
def connection():
    """
    Connection to database
    """
    cursor = None
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            port = DB_PORT,
            password=DB_PASSWORD)
        
        cursor = conn.cursor()
        yield cursor, conn

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
