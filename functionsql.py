import mysql.connector
import datetime
import db_materi  # Ensure db_materi contains the necessary query_select function
import db_kbm  # Ensure db_kbm contains the necessary query_select function

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def data_sql(nama_database, sumber):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gobimbel",
            database=nama_database
        )
        cursor = connection.cursor()

        if nama_database == 'db_materi':
            query = db_materi.query_select(sumber)
        elif nama_database == 'db_kbm':
            query = db_kbm.query_select(sumber)

        cursor.execute(query)
        results = cursor.fetchall()
        data_sql = []
        for row in results:
            formatted_row = [format_datetime(value) if isinstance(value, datetime.datetime) else value for value in row]
            data_sql.append(formatted_row)
        return data_sql

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()