import function
import os
import functionsql
import function_table
import datetime


def clear_terminal():
    os.system("cls")
    
maxlen = 0
data_front = []
def print_data(data_front) :
    data = [value for value in data_front]
    return data

clear_terminal()

#NAMA TABLE SUMBER
sumber = function.nama_table_sumber()
o_sumber = f"Nama table sql : {sumber}" 
data_front.append(o_sumber)
if len(o_sumber) > maxlen : 
    maxlen = len(o_sumber)

clear_terminal()

#DATABASE AMBIL DATA
print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")
nama_database = function.nama_database()
o_nama_database = f"Nama database postgre : {nama_database}"
data_front.append(o_nama_database)
if len(o_nama_database) > maxlen : 
    maxlen = len(o_nama_database)

clear_terminal()

#NAMA TABLE TUJUAN
print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")
nama_table = function.nama_table_postgre(nama_database)
o_nama_table = f"Nama table postgre : {nama_table}"
data_front.append(o_nama_table)
if len(o_nama_table) > maxlen : 
    maxlen = len(o_nama_table)

clear_terminal()

#JENIS TABLE
print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")
jenis_table = function_table.jenis_table(nama_database,nama_table)
o_jenis_table = f"Jenis tabel {nama_table} : {jenis_table}"
data_front.append(o_jenis_table)
if len(o_jenis_table) > maxlen : 
    maxlen = len(o_jenis_table)
clear_terminal()

#PRIMARY KEY TABLE
print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")
primary_key = function_table.primary_key(nama_table)
o_primary_key = f"Primary key table {nama_table} : {primary_key}"
data_front.append(o_primary_key)
if len(o_primary_key) > maxlen : 
    maxlen = len(o_primary_key)
clear_terminal()

#KOLOM TABLE
print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")
kolom_table = function_table.kolom_table(nama_table)
o_kolom_table = f"Kolom dari {nama_table} : {kolom_table}"
data_front.append(o_kolom_table)
if len(o_kolom_table) > maxlen : 
    maxlen = len(o_kolom_table)
clear_terminal()

#FOREIGN KEY
print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")
result = function_table.foreign_key(nama_table)
foreign_column = result[0]
foreign_table = result[1]
o_foreign_column = f"foreign_column dari {nama_table} : {foreign_column}"
o_foreign_table = f"foreign_table dari {nama_table} : {foreign_table}"
data_front.append(o_foreign_column)
data_front.append(o_foreign_table)
if len(o_foreign_column) > maxlen : 
    maxlen = len(o_foreign_column)
if len(o_foreign_table) > maxlen : 
    maxlen = len(o_foreign_table)
clear_terminal()

#UNIQUE KEY
print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")
unique_key = function_table.unique_key(nama_table)
o_unique_key = f"unique_key dari {nama_table} : {unique_key}"
data_front.append(o_unique_key)
if len(o_unique_key) > maxlen : 
    maxlen = len(o_unique_key)
clear_terminal()

print("="*maxlen)
data = print_data(data_front)
print('\n'.join(data))
print("="*maxlen+"\n")


sql_statements = []
nama_table_baru = f"{nama_table}_baru"   

data_sql = functionsql.data_sql(nama_database, sumber)

values = []
for array in data_sql:
    new_tuple = tuple(function.format_datetime(val) for val in array)
    values.append(new_tuple)
if len(values) >1000 :
    batch_size = round(len(values)/1000)
elif len(values) >100 :
    batch_size = round(len(values)/100)
elif len(values) > 10 :
    batch_size = round(len(values)/10)
else : 
    batch_size = 1



  
if jenis_table == 'penghubung' :
    best_unique = []
    long_unique = 0
    for i in range(len(unique_key)) :
        unique_long = []
        for value in unique_key[i] :
            unique = f"{value}"
            unique_long.append(unique) 
        if len(unique_long) > long_unique : 
            long_unique = len(unique_long)
            best_unique.append(unique_long)
    unique_last = best_unique[-1]
    first = nama_table.split("_")
    first_word =  ''
    for value in first : 
        first_word += first[0]
    
    unique_selection = []
    for value in kolom_table :
        unique = f"c.{value}"
        unique_selection.append(unique)
        
    
    unique_select = f"select {', '.join(unique_selection)} from (select * from {nama_table} {first_word} join (SELECT MAX({primary_key}) AS max_{primary_key} FROM {nama_table} GROUP BY {', '.join(unique_last)}) sub on sub.max_{primary_key} = {first_word}.{primary_key}) c ;"

    sql_statements.append(f"DROP TABLE IF EXISTS {nama_table_baru};")
    sql_statements.append(f"CREATE TABLE {nama_table_baru} AS SELECT * FROM {nama_table} WHERE false;")
    sql_statements.append(f"ALTER TABLE {nama_table_baru} DROP COLUMN {primary_key};")
    sql_statements.append(f"alter table {nama_table_baru} ADD {primary_key} serial;")
    if nama_table != 't_isi_bundel_soal' :
        sql_statements.append(f"insert into {nama_table_baru} {unique_select};")
    if nama_table == 't_isi_bundel_soal' :
        sql_statements.append(f"ALTER TABLE {nama_table_baru} ADD CONSTRAINT unique_{nama_table_baru} UNIQUE (c_id_bundel, c_id_soal);")
    else : 
        sql_statements.append(f"ALTER TABLE {nama_table_baru} ADD CONSTRAINT unique_{nama_table_baru} UNIQUE ({', '.join(unique_last)});")
    sql_statements.append(f"ALTER TABLE {nama_table_baru} ADD CONSTRAINT {nama_table_baru}_pk PRIMARY KEY ({primary_key});")
    
    for i in range(0, len(values), batch_size):
        batch_values = values[i:i + batch_size]
        batch_sql_query = []
        for value in batch_values:
            batch_sql_query.append(f"{value}")

        batch_sql_query = ', '.join(batch_sql_query)
        if nama_table != 't_isi_bundel_soal':
            sql_query_ = f"INSERT INTO {nama_table_baru} ({', '.join(kolom_table)}) VALUES {batch_sql_query} ON CONFLICT ({', '.join(unique_last)}) DO NOTHING;"
        else : 
            sql_query_ = f"INSERT INTO {nama_table_baru} ({', '.join(kolom_table)}) VALUES {batch_sql_query} ON CONFLICT (c_id_bundel, c_id_soal) DO NOTHING;"
        sql_statements.append(sql_query_)

    sql_statements.append(f"DROP TABLE IF EXISTS {nama_table};")
    sql_statements.append(f"ALTER TABLE {nama_table_baru} RENAME TO {nama_table};")
    sql_statements.append(f"ALTER TABLE {nama_table} RENAME CONSTRAINT {nama_table_baru}_pk TO {nama_table}_pk;")
    sql_statements.append(f"ALTER TABLE {nama_table} RENAME CONSTRAINT unique_{nama_table_baru} TO unique_{nama_table};") 
    if nama_table == 't_isi_bundel_soal' :
        sql_statements.append(f"WITH CTE AS ( SELECT c_id_bundel, c_id_soal, ROW_NUMBER() OVER (PARTITION BY c_id_bundel ORDER BY c_id_soal) AS new_urutan FROM {nama_table} WHERE c_id_bundel IN ( SELECT c_id_bundel FROM ( SELECT c_id_Bundel, c_nomor_soal FROM {nama_table} GROUP BY c_id_bundel, c_nomor_soal HAVING COUNT(*) > 1 ) cek ) ) UPDATE {nama_table} AS tgt SET c_nomor_soal = CTE.new_urutan FROM CTE WHERE tgt.c_id_bundel = CTE.c_id_bundel and tgt.c_id_soal = CTE.c_id_soal;") 
        sql_statements.append(f"update {nama_table} set c_nomor_soal = 1 where c_nomor_soal is null;")
        sql_statements.append(f"WITH CTE AS ( SELECT c_id_bundel, c_id_soal, ROW_NUMBER() OVER (PARTITION BY c_id_bundel ORDER BY c_id_soal) AS new_urutan FROM {nama_table} WHERE c_id_bundel IN ( SELECT c_id_bundel FROM ( SELECT c_id_Bundel, c_nomor_soal FROM {nama_table} GROUP BY c_id_bundel, c_nomor_soal HAVING COUNT(*) > 1 ) cek ) ) UPDATE {nama_table} AS tgt SET c_nomor_soal = CTE.new_urutan FROM CTE WHERE tgt.c_id_bundel = CTE.c_id_bundel and tgt.c_id_soal = CTE.c_id_soal;") 
    for i in range (len(unique_key)) :
        sql_statements.append(f"ALTER TABLE {nama_table} ADD CONSTRAINT unique_{nama_table_baru}_{i} UNIQUE ({', '.join(unique_key[i])});")
    for i in range (len(foreign_column)):
        sql_statements.append(f"DELETE FROM {nama_table} WHERE NOT EXISTS (SELECT 1 FROM {foreign_table[i]} WHERE {nama_table}.{foreign_column[i]} = {foreign_table[i]}.{foreign_column[i]});")
    for i in range (len(foreign_column)) :
        sql_statements.append(f"ALTER TABLE {nama_table} ADD CONSTRAINT {nama_table}_{foreign_column[i]}_fkey FOREIGN KEY ({foreign_column[i]})  REFERENCES {foreign_table[i]} ({foreign_column[i]});" )

elif jenis_table == 'master' :
    def generate_update_statement(kolom_table, primary_key):
        update_parts = [f"{col} = EXCLUDED.{col}" for col in kolom_table if col != primary_key]
        return ', '.join(update_parts)    
    for i in range(0, len(values), batch_size):
        batch_values = values[i:i + batch_size]
        update_statement = generate_update_statement(kolom_table, primary_key)
        batch_sql_query = []
        for value in batch_values:
            batch_sql_query.append(f"{value}")
        batch_sql_query = ', '.join(batch_sql_query)
        sql_query = f"SELECT DISTINCT {primary_key} FROM {nama_table}"
        sql_query_ = f"INSERT INTO {nama_table} ({', '.join(kolom_table)}) VALUES {batch_sql_query} ON CONFLICT ({primary_key}) DO UPDATE SET {update_statement};"
        sql_statements.append(sql_query_)
    sql_statements.append(f"GRANT INSERT, UPDATE, TRIGGER, TRUNCATE, SELECT, REFERENCES, DELETE ON TABLE {nama_table} TO developer;")
    if len(foreign_column) > 0 :
        for i in range (len(foreign_column)):
            sql_statements.append(f"DELETE FROM {nama_table} WHERE NOT EXISTS (SELECT 1 FROM {foreign_table[i]} WHERE {nama_table}.{foreign_column[i]} = {foreign_table[i]}.{foreign_column[i]});")
        for i in range (len(foreign_column)) :
            sql_statements.append(f"ALTER TABLE {nama_table} ADD CONSTRAINT {nama_table}_{foreign_column[i]}_fkey FOREIGN KEY ({foreign_column[i]})  REFERENCES {foreign_table[i]} ({foreign_column[i]});" ) 
new_sql_file = f'{nama_database}_{nama_table}.sql'

with open(new_sql_file, 'w', encoding='utf-8') as new_file:
    modified_statements = [statement.replace("\\'", "").replace("\\", "").replace("'NULL'","NULL") for statement in sql_statements]
    new_file.write('\n'.join(modified_statements))
print(f"File done : {new_sql_file}")

