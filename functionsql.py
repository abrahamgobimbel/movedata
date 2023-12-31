import mysql.connector
import datetime
import db_go 
import db_kbm 
import db_materi 
import db_materi_teaser 
import db_produk 
import db_produk_teaser  
import db_pt
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

def data_sql(nama_database, nama_table):
    try:
        connection = mysql.connector.connect(
            host="192.168.169.193",
            user="goexpert",
            password="!6iri&Lu5i?",
            database = "db_banksoalV2",
            port = 3306
        )
        cursor = connection.cursor()

        
        if nama_database == 'db_go' :
            query = db_go.query_select(nama_table)
        elif nama_database == 'db_kbm':
            query = db_kbm.query_select(nama_table)
        elif nama_database == 'db_materi':
            query = db_materi.query_select(nama_table)
        elif nama_database == 'db_produk' :
            query = db_produk.query_select(nama_table)
        elif nama_database == 'db_pt' :
            query = db_pt.query_select(nama_table)   
        elif nama_database == 'db_report_siswa_empati_mandiri' : 
            query = db_report_siswa_empati_mandiri.query_select(nama_table)
        elif nama_database == 'db_report_siswa_empati_wajib' :
            query = db_report_siswa_empati_wajib.query_select(nama_table)
        elif nama_database == 'db_report_siswa_goa' :
            query = db_report_siswa_goa.query_select(nama_table)
        elif nama_database == 'db_report_siswa_irt' :
            query = db_report_siswa_irt.query_select(nama_table)
        elif nama_database == 'db_report_siswa_koding' :
            query = db_report_siswa_koding.query_select(nama_table)
        elif nama_database == 'db_report_siswa_peringkat' : 
            query = db_report_siswa_peringkat.query_select(nama_table)
        elif nama_database == 'db_sekolah' :
            query = db_sekolah.query_select(nama_table)
        elif nama_database == 'db_user' :
            query = db_user.query_select(nama_table)
        
        print (query)
        
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