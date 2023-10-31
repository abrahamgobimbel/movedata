import mysql.connector
import datetime
import db_go 
import db_kbm 
import db_materi 
import db_materi_teaser 
import db_produk 
import db_produk_teaser  
import db_ptn 
import db_report_siswa_empati_mandiri 
import db_report_siswa_empati_wajib
import db_report_siswa_goa 
import db_report_siswa_irt 
import db_report_siswa_kuis 
import db_report_siswa_lateks  
import db_report_siswa_paket_intensif 
import db_report_siswa_pendalaman_materi 
import db_report_siswa_peringkat  
import db_report_siswa_presensi 
import db_report_siswa_racing 
import db_report_siswa_soref 
import db_report_siswa_tobk  
import db_report_siswa_vak 
import db_report_siswa_koding 
import db_report_tamu 
import db_sekolah 
import db_user 
import db_user_lembaga 
import db_user_tamu 

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

        if nama_database == 'db_kbm':
            query = db_kbm.query_select(sumber)
        elif nama_database == 'db_go' :
            query = db_go.query_select(sumber)
        elif nama_database == 'db_materi':
            query = db_materi.query_select(sumber)
        elif nama_database == 'db_report_siswa_goa' :
            query = db_report_siswa_goa.query_select(sumber)

        
        cursor.execute(query)
        results = cursor.fetchall()
        formatted_rows = []
        data_sql = []
        for row in results:
            formatted_row = [format_datetime(value) if isinstance(value, datetime.datetime) else value for value in row]
            formatted_rows.append(formatted_row)
        for row in formatted_rows:
            formatted = [value.replace("'", "-") if isinstance(value, str) else value for value in row]
            data_sql.append(formatted)
        return data_sql

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()