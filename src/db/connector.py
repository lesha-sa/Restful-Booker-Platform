import os
import socket
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def is_resolvable(host: str) -> bool:
    try:
        socket.gethostbyname(host)
        return True
    except:
        return False

def get_db_connection():
    host = os.getenv("POSTGRES_HOST")
    if not is_resolvable(host):
        host = "localhost"

    conn = psycopg2.connect(
        host=host,
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn
