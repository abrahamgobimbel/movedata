import os
import functioninput

def query_select(nama_table) :
    
    if nama_table == 't_jurusan' : 
        unique_select = ['tj.c_IdJurusan','tj.c_IdPerguruanTinggi','tj.c_NamaJurusan','tj.c_Kelompok','tj.c_Rumpun','tj.c_Keterangan','tj.c_Status','tj.c_PG','tj.c_PGUM','tj.c_PLUM','tj.c_LintasJurusan','tj.c_IsSBMPTN','tj.c_IsUM','tj.c_Jenjang','tj.c_IsSNMPTN','tj.c_Updater','tj.c_LastUpdate','CURRENT_TIMESTAMP()']
        query = (f"SELECT {', '.join(unique_select)}\n"
                 f"FROM db_GOIconsV2.t_Jurusan tj ")
    elif nama_table == 't_jurusan_deskripsi' : 
        query = (f"SELECT *\n"
                f"FROM db_GOIconsV2.t_JurusanDeskripsi tjd ")    
    elif nama_table == 't_kelompok_jurusan' :
        query = (f"SELECT *, CURRENT_TIMESTAMP() \n"
                f"FROM db_GOIconsV2.t_TransJurusan ttj\n"
                f"WHERE ttj.c_Kode  LIKE '03%';")
    elif nama_table == 't_perguruan_tinggi' :
        query = (f"SELECT *, CURRENT_TIMESTAMP()\n"
                f"FROM db_GOIconsV2.t_PerguruanTinggi tpt ")
    elif nama_table == 't_rumpun_jurusan' :
        query = (f"SELECT *, CURRENT_TIMESTAMP() \n"
                f"FROM db_GOIconsV2.t_TransJurusan ttj\n"
                f"WHERE ttj.c_Kode  LIKE '01%';")

    return query