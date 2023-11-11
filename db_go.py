def query_select(nama_table) :
    
    if nama_table == 't_berita' :
        query = (f"SELECT id, tglterbit, tglberakhir, judul, deskripsi, url, updater, status, untuk, jenis, \n"
                f"photo, jmlhviewer, lastupdate, current_timestamp() FROM db_GOKreasi.t_berita tb;")
    elif nama_table == 't_bidang_go' :
        query = (f"SELECT tg.c_IdBidang , tg.c_NamaBidang , tg.c_Status , tg.c_IdKewilayahan,\n"
                f" tg.c_Upline , tg.c_Updater , tg.c_LastUpdate , CURRENT_TIMESTAMP()\n"
                f"FROM db_GOIconsV2.t_GOBidang tg ;")
    elif nama_table == 't_gedung' : 
        query = (f"SELECT * \n"
                f"FROM db_GOIconsV2.t_Gedung tg ")
    elif nama_table == 't_gokomar' : 
        query = (f"SELECT *\n"
                f"FROM db_GOIconsV2.t_GOKomar tg ")
    elif nama_table == 't_kota' : 
        query = (f"SELECT *, CURRENT_TIMESTAMP() \n"
                f"FROM db_GOIconsV2.t_Penanda tp ")
    return query