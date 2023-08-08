import os

import mysql.connector
from dotenv import load_dotenv

from utils.s3_write import s3_write

load_dotenv()


def mysql_connection(database: str, table: str) -> list:
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
    data = mysql_connection('lake_solution', 'sales')
    s3_write(data, 'sales')
