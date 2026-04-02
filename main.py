import os
import pymysql
from dotenv import load_dotenv

load_dotenv() # Loading .env file with program configuration

# Checking if all required variables are set in the .env file
required = ['DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'DB_TABLE', 'DB_DATE_COLUMN', 'DB_INTERVAL']
missing = [var for var in required if not os.getenv(var)]
if missing:
    print(f"Missing variables in the .env file: {', '.join(missing)}")
    raise

table = os.getenv('DB_TABLE') # Load table name from .env file
date = os.getenv('DB_DATE_COLUMN') # Load date column name from .env file
interval = os.getenv('DB_INTERVAL') # Load deletion interval from .env file

# Preparing connection to the database
connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

# Attempting to connect to the database
try:
    with connection.cursor() as cursor:
        # Preparing the SQL query for the database
        sql = f"DELETE FROM {table} WHERE {date} < DATE_SUB(CURDATE(), INTERVAL {interval})"
        deleted = cursor.execute(sql) # Executing the query
        connection.commit() # Committing changes to the database
        print(f"Number of deleted records: {deleted} Older than: {interval}") # Echoing the number of deleted records
except pymysql.Error as e:
    connection.rollback() # Rolling back changes if an error occurred
    print(f"An error occurred: {e}")
    raise
finally:
    connection.close() # Closing the connection to the database after completing the operation