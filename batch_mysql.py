import os

import mysql.connector
from dotenv import load_dotenv

from utils.write_s3 import write_s3

load_dotenv()

def mysql_connection(database, table) -> list:
  cnx = mysql.connector.connect(
      host=os.getenv('MYSQL_CONN_HOST'),
      user=os.getenv('MYSQL_CONN_USER'),
      password=os.getenv('MYSQL_CONN_PASSWORD'),
      database=database
  )

  cursor = cnx.cursor()

  query = f'select * from {table};'

  cursor.execute(query)
  data = cursor.fetchall()

  return data


if __name__ == '__main__':
  data = mysql_connection('hotmart', 'sales')
  write_s3(data, 'sales')
