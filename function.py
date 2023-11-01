import datetime
import function_database
import function_table


def nama_database() :
    pilihan = False
    while not pilihan : 
        nama_database = function_database.nama_database()
        print(f"List database : ")
        for i, table in enumerate(nama_database):
            if i < 9 :
                print(f"{i+1}.  db_{nama_database[i]}")
            else : 
                print(f"{i+1}. db_{nama_database[i]}")
        
        nomor = int(input(f"\nPilih nomor database yang diinginkan (1-{len(nama_database)}) : "))
        while nomor < 1 or nomor > len(nama_database) : 
            if nomor < 1 or nomor > len(nama_database):
                print(f"Nomor yang diinput harus antara 1 hingga {len(nama_database)}\n")
                nomor = int(input(f"Pilih nomor database yang diinginkan (1-{len(nama_database)}) : "))
        nama_database = f"db_{nama_database[nomor-1]}"
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama database : {nama_database} | Apakah nama database postgre sudah sesuai (y|n) : ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' : 
            pilihan = True
        elif pilihan.lower()  == 'n' :
            pilihan = False
    return nama_database

def nama_table_postgre(nama_database):
    pilihan = False 
    while not pilihan : 
        nama_table = function_table.nama_table(nama_database)
        print(f"List table {nama_database} : ")
        for i, table in enumerate(nama_table):
            if i < 9 :
                print(f"{i+1}.  {nama_database} - {table}")
            else : 
                print(f"{i+1}. {nama_database} - {table}")
        nomor = int(input(f"Pilih nomor database yang diinginkan (1-{len(nama_table)}) : "))
        while nomor < 1 or nomor > len(nama_table) : 
            if nomor < 1 or nomor > len(nama_table):
                print(f"\nNomor yang diinput harus antara 1 hingga {len(nama_table)}\n")
                nomor = int(input(f"Pilih nomor database yang diinginkan (1-{len(nama_table)}) : "))
        nama_table = f"{nama_table[nomor-1]}"
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama tabel : {nama_table} | Apakah nama database postgre sudah sesuai (y|n) : ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' : 
            pilihan = True
        elif pilihan.lower()  == 'n' :
            pilihan = False
    return nama_table

def format_datetime(val):
    if val is None:
        return 'NULL'
    elif isinstance(val, datetime.datetime):
        return val.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(val, datetime.date) :
        return val.strftime('%Y-%m-%d')
    else:
        return val