import datetime

def nama_database() :
    pilihan = False 
    while not pilihan : 
        nama_database = input("Masukkan nama database postgre, ex : db_materi : ") 
        nama_database = nama_database.lower()
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama database : {nama_database} | Apakah nama database postgre sudah sesuai (y|n) : ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' : 
            pilihan = True
        elif pilihan.lower()  == 'n' :
            pilihan = False
    return nama_database


def nama_table_postgre() :
    pilihan = False
    while not pilihan : 
        nama_table = input("Masukkan nama table postgre, ex : t_isi_produk_mix : ")
        nama_table = nama_table.lower()
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama table postgre : {nama_table} | Apakah nama tabel postgre sudah sesuai (y|n) : ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' :
            pilihan = True
        elif pilihan.lower() == 'n' :
            pilihan = False
    return nama_table
    
    
def nama_table_sumber() :
    pilihan = False
    while not pilihan : 
        sumber = input("Masukkan nama table sumber mysql, ex : t_isiprodukmix : ")
        sumber = sumber.lower()
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama table mysql : {sumber} | Apakah nama tabel mysql sudah sesuai (y|n) : ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' :
            pilihan = True
        elif pilihan.lower() == 'n' :
            pilihan = False
    return sumber
    
    
def read_sql(sumber) :
    sql_file = f"{sumber}.sql"
    values = []
    with open(sql_file, 'r') as file:
        for line in file:
            values.append(line.strip())   
    for i in range(len(values)):
        values[i] = values[i].replace('\\', '-')
    return values


def jenis_table(nama_table) : 
    jenis_tabel = ''
    pilihan = False
    while not pilihan : 
        while jenis_tabel != 'm' and jenis_tabel != 'p' :
            jenis_tabel = input("Input jenis tabel (master = m, penghubung = p) : ")
            jenis_tabel = jenis_tabel.lower()
            if (jenis_tabel != 'm' and jenis_tabel != 'p') :
                print("input harus m atau p")
        if jenis_tabel == 'm' :
            jenis_tabel = 'master'
        else : 
            jenis_tabel = 'penghubung'
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Apakah {nama_table} adalah tabel {jenis_tabel} (y|n) : ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' :
            pilihan = True
        elif pilihan.lower() == 'n' :
            pilihan = False
    return jenis_tabel

def primary_key(nama_table) :
    pilihan = False
    while not pilihan : 
        primary_key = input("\nInput kolom primary key, ex : c_id : ")
        primary_key = primary_key.lower()
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Primary key table {nama_table} : {primary_key} | Apakah nama kolom primary_key sudah sesuai (y|n): ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' :
            pilihan = True
        elif pilihan.lower() == 'n' :
            pilihan = False
    return primary_key

def kolom_table(nama_table) :
    final = False
    while not final : 
        kolom_table = []
        pilihan = False
        while not pilihan :
            choice = False
            while not choice:
                kolom = input("Input kolom table selain primary key (kecuali master), ex: c_id_produk_mix: ")
                while choice != 'y' and choice != 'n' :
                    choice = input(f"Kolom : {kolom} | Apakah nama kolom sudah benar (y|n) : ")
                    if (choice != 'y' and choice != 'n') :
                        print("input harus y (yes) or n (no)")
                if choice.lower() == 'y':
                    kolom_table.append(kolom)
                    choice = True
                elif choice.lower() == 'n':
                    choice = False
            while pilihan != 'y' and pilihan != 'n' :
                pilihan = input("Apakah masih ada kolom lain (y|n): ")
                if (pilihan != 'y' and pilihan != 'n') :
                    print("input harus y (yes) or n (no)")
            if pilihan.lower() == 'y':
                pilihan = False
            elif pilihan.lower() == 'n':
                pilihan = True
        while final != 'y' and final != 'n' :
            final = input(f"Kolom dari {nama_table} : {kolom_table} | Apakah kolom dari table {nama_table} sudah benar (y|n) : ")
            if (pilihan != 'y' and pilihan != 'n') :
                print("input harus y (yes) or n (no)")
        if final.lower() == 'y' : 
            final = True
        elif final.lower() == 'n': 
            final = False
    return kolom_table

def foreign_key(nama_table, kolom_table) :
    if_foreign_key = ''
    while if_foreign_key != 'y' and if_foreign_key != 'n' :
        if_foreign_key = input("Apakah ada foreign key (y,n) : ") 
        if_foreign_key = if_foreign_key.lower()
        if (if_foreign_key != 'y' and if_foreign_key != 'n') :
            print("input harus y atau n")

    foreign_column = [] 
    foreign_table =[]
    if if_foreign_key.lower() == 'y' :
        pilihan = False
        while not pilihan : 
            choice = False
            while not choice : 
                kolom = ''
                while True :
                    kolom = input(f"Input kolom foreign_key {nama_table}, ex: c_id_produk_mix: ").lower()
                    if (kolom in kolom_table) :
                        break
                    else : print(f"Kolom tidak ada di tabel {nama_table}")
                table = input(f"Input nama table {kolom} : ").lower()
                while choice != 'y' and choice != 'n' :
                    choice = input(f"foreign key {nama_table} : {kolom} from {table} | Apakah nama kolom foreign_key sudah sesuai (y|n): ")
                    if (choice != 'y' and choice != 'n') :
                        print("input harus y (yes) or n (no)")
                if choice.lower() == 'y' :
                    foreign_column.append(kolom)
                    foreign_table.append(table)
                    choice = True
                elif choice.lower() == 'n' :
                    choice = False
            while pilihan != 'y' and pilihan != 'n' :
                pilihan = input("Apakah masih ada foreign_key lain (y|n): ")
                if (pilihan != 'y' and pilihan != 'n') :
                    print("input harus y (yes) or n (no)")
            if pilihan.lower() == 'y':
                pilihan = False
            elif pilihan.lower() == 'n':
                pilihan = True
    return foreign_column, foreign_table

def unique_key(nama_table, kolom_table) :
    if_unique_key = ''
    while if_unique_key != 'y' and if_unique_key != 'n' :
        if_unique_key = input("Apakah ada unique key (y,n) : ") 
        if_unique_key = if_unique_key.lower()
        if (if_unique_key != 'y' and if_unique_key != 'n') :
            print("input harus y atau n")

    unique_key = []
    if if_unique_key.lower() == 'y' :
        pilihan = False
        while not pilihan : 
            choice = False
            while not choice : 
                unique_column = []
                kolom = input("Input kolom table unique, ex: c_id_produk_mix: ").lower()
                if kolom not in kolom_table :  
                    print("kolom tersebut tidak ada di list kolom table")
                    choice = False
                    break
                else : 
                    unique_column.append(kolom)
                choice = input(f"Apakah ada kolom unique terkait dengan {kolom} (y/n) : ")
                if choice.lower() == 'y' :
                    nc = False
                    while not nc :
                        kolom = input(f"Input kolom table unique terkait dengan {unique_column}, ex: c_id_produk_mix: ").lower()
                        unique_column.append(kolom)
                        nc = input(f"Apakah ada kolom lain terkait dengan {unique_column} (y,n) : ")
                        if nc == 'y' :
                            nc = False
                        elif nc == 'n' :
                            nc = True
                            unique_key.append(unique_column)
                        else : 
                            print("input harus y dan n")
                            nc = True
                    choice = True
                elif choice.lower() == 'n' :
                    unique_key.append(unique_column)
                    choice = False
                else : 
                    print("input harus y atau n")
                    choice = False
            while pilihan != 'y' and pilihan != 'n' :
                pilihan = input("Apakah masih ada unique_key lain (y|n): ")
                if (pilihan != 'y' and pilihan != 'n') :
                    print("input harus y (yes) or n (no)")
            if pilihan.lower() == 'y':
                pilihan = False
            elif pilihan.lower() == 'n':
                pilihan = True
    return unique_key

def format_datetime(val):
    if val is None:
        return 'NULL'
    elif isinstance(val, datetime.datetime):
        return val.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(val, datetime.date) :
        return val.strftime('%Y-%m-%d')
    else:
        return val