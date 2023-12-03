def query_select(nama_table) :
    
    if nama_table == 't_berita' :
        query = (f"SELECT id, tglterbit, tglberakhir, judul, deskripsi, url, updater, status, untuk, jenis, \n"
                f"photo, jmlhviewer, lastupdate, current_timestamp() FROM db_GOKreasi.t_berita tb;")
    elif nama_table == 't_bidang_go' :
        query = (f"SELECT tg.c_IdBidang , tg.c_NamaBidang , tg.c_Status , tg.c_IdKewilayahan,\n"
                f" tg.c_Upline , tg.c_Updater , tg.c_LastUpdate , CURRENT_TIMESTAMP()\n"
                f"FROM db_GOIconsV2.t_GOBidang tg ;")
    elif nama_table == 't_daftar_kegiatan' :
        query = (f"SELECT * FROM db_IsianDPPV3.t_BankData")
    elif nama_table == 't_gedung' : 
        query = (f"SELECT * \n"
                f"FROM db_GOIconsV2.t_Gedung tg ")
    elif nama_table == 't_gedung_zona' :
        query = (f"SELECT *, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP\n"
                f"FROM db_IsianDPPV3.t_ZonaGedung;")
    elif nama_table == 't_gokomar' : 
        query = (f"SELECT *\n"
                f"FROM db_GOIconsV2.t_GOKomar tg ")
    elif nama_table == 't_kota' : 
        query = (f"SELECT *, CURRENT_TIMESTAMP() \n"
                f"FROM db_GOIconsV2.t_Penanda tp ")
    elif nama_table == 't_rencana_kerja' :
        query = (f"SELECT *\n"
                f"FROM db_IsianDPPV3.t_RencanaKerja trk\n"
                f"WHERE c_JamAwal IS NOT NULL\n"
                f"AND c_JamAwal BETWEEN DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 WEEK)\n"
                f"AND DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL 1 WEEK);")
    elif nama_table == 't_zona' :
        query = (f"select *, CURRENT_TIMESTAMP\n"
                f"from db_IsianDPPV3.t_Zona tz;")
        
    return query