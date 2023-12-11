def query_select(nama_table) :
    
    if nama_table == 't_berita' :
        query = (f"SELECT id, tglterbit, tglberakhir, judul, deskripsi, url, updater, status, untuk, jenis, \n"
                f"photo, jmlhviewer, lastupdate, current_timestamp() FROM db_GOKreasi.t_berita tb;")
        
    elif nama_table == 't_bidang_go' :
        query = (f"SELECT tg.c_IdBidang , tg.c_NamaBidang , tg.c_Status , tg.c_IdKewilayahan,\n"
                f" tg.c_Upline , tg.c_Updater , tg.c_LastUpdate , CURRENT_TIMESTAMP()\n"
                f"FROM db_GOIconsV2.t_GOBidang tg ;")
        
    elif nama_table == 't_biodata_karyawan' :
        unique_select = ['tbk.*']
        query = (
            f"select distinct {', '.join(unique_select)}\n"
            "FROM  db_GOIconsV2.t_Biodata_Karyawan tbk \n"
            "JOIN db_GOIconsV2.t_Idn_Lurah til on tbk.c_IdLurah = til.c_IdLurah\n"
            "JOIN db_GOIconsV2.t_Idn_Camat tic on til.c_IdCamat = tic.c_IdCamat\n"
            "JOIN db_GOIconsV2.t_Idn_District tid on tbk.c_IdDistrict = tid.c_IdDistrict and tic.c_IdDistrict = tid.c_IdDistrict\n"
            "JOIN db_GOIconsV2.t_Idn_Provinsi tip on tid.c_IdProvinsi = tip.c_IdProvinsi\n"
        )
        
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
        
    elif nama_table == 't_kecamatan_indonesia' :
        unique_select = ['tic.*', 'current_timestamp']
        query = (
            f"select distinct {', '.join(unique_select)}\n"
            "from db_GOIconsV2.t_Idn_Camat tic\n"
            "join db_GOIconsV2.t_Idn_District tid on tic.c_IdDistrict = tid.c_IdDistrict\n"
            "join db_GOIconsV2.t_Idn_Provinsi tip on tid.c_IdProvinsi = tip.c_IdProvinsi;"
        )
    elif nama_table == 't_karyawan_go' :
        unique_select = [
           'tk.c_NIK','tk.c_IdBiodata','tk.c_TglMulaiKerja','tk.c_TglAkhirKerja','tk.c_MBTI',
           'tk.c_FotoKarakter','tk.c_LastUpdate','tk.c_Status','tk.c_Updater','tk.c_AlasanResign',
           'tk.c_KeteranganResign'
        ]
        query = (
            f"select distinct {', '.join(unique_select)}\n"
            "from db_GOIconsV2.t_Karyawan tk\n"
            "JOIN db_GOIconsV2.t_Biodata_Karyawan tbk on tk.c_IdBiodata = tbk.c_IdBiodata \n"
            "JOIN db_GOIconsV2.t_Idn_Lurah til on tbk.c_IdLurah = til.c_IdLurah\n"
            "JOIN db_GOIconsV2.t_Idn_Camat tic on til.c_IdCamat = tic.c_IdCamat\n"
            "JOIN db_GOIconsV2.t_Idn_District tid on tbk.c_IdDistrict = tid.c_IdDistrict and tic.c_IdDistrict = tid.c_IdDistrict\n"
            "JOIN db_GOIconsV2.t_Idn_Provinsi tip on tid.c_IdProvinsi = tip.c_IdProvinsi;"
        )
    elif nama_table == 't_kelurahan_indonesia' :
        unique_select = ['til.*', 'current_timestamp']
        query = (
            f"select distinct {', '.join(unique_select)}\n"
            "from db_GOIconsV2.t_Idn_Lurah til\n"
            "join db_GOIconsV2.t_Idn_Camat tic on til.c_IdCamat = tic.c_IdCamat\n"
            "join db_GOIconsV2.t_Idn_District tid on tic.c_IdDistrict = tid.c_IdDistrict\n"
            "join db_GOIconsV2.t_Idn_Provinsi tip on tid.c_IdProvinsi = tip.c_IdProvinsi;"
        )   
    
    elif nama_table == 't_kota' : 
        query = (f"SELECT *, CURRENT_TIMESTAMP() \n"
                f"FROM db_GOIconsV2.t_Penanda tp ")
        
    elif nama_table == 't_kota_indonesia' :
        unique_select = ['tid.*', 'current_timestamp']
        query = (
            f"select distinct {', '.join(unique_select)}\n"
            "from db_GOIconsV2.t_Idn_District tid\n"
            "join db_GOIconsV2.t_Idn_Provinsi tip on tid.c_IdProvinsi = tip.c_IdProvinsi;"
        )
        
    elif nama_table == 't_provinsi_indonesia' : 
        unique_select = ['tip.*', 'current_timestamp']
        query = (
            f"select distinct {', '.join(unique_select)}\n"
            "from db_GOIconsV2.t_Idn_Provinsi tip;"
        )
        
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