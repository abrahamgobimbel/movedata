import mysql.connector
import datetime
import db_materi

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def data_sql(nama_database, sumber, primary_key):
    
    connection = mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password = "gobimbel",
        database = nama_database  
    )
    cursor = connection.cursor()

    if nama_database == 'db_materi' :
        query = db_materi.query_select(sumber, primary_key)
    elif nama_database == 'db_kbm' :
        query = db_kbm.query_select(sumber, primary_key)
        
    cursor.execute(query)
    results = cursor.fetchall()
    
    data_sql = []
    for row in results:
        for index, value in enumerate(row):
            if isinstance(value, datetime.datetime):
                row = list(row)  
                row[index] = format_datetime(value)
                data_sql.append(row)
    
    cursor.close()
    connection.close()
    return data_sql