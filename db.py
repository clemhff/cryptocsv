import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(verbose=True)


HOST = os.getenv('PHOST')
USER = os.getenv('PUSER')
PASSWORD = os.getenv('PPASSWORD')
DATABASE = os.getenv('PDATABASE')

def query(sql):
    # Open connection
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

    #Open a cursor to send SQL commands
    cur = conn.cursor()


    # Execute a SQL INSERT command
    cur.execute(sql)
    result = cur.fetchall()
    
    # Close connection
    conn.close()

    return result
