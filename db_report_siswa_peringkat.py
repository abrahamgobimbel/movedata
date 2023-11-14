def query_select(nama_table) :
    
    if nama_table == 't_pengerjaan_mata_uji' : 
        unique_select = ['tpmu.cNoRegistrasi','tpmu.cIdpelajaran','tpmu.cTanggal','tpmu.cSumber','tpmu.cJumlahPengerjaan','tpmu.cJumlahBenar','CURRENT_TIMESTAMP()','tpmu.cLastUpdate']
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_pengerjaanMataUji tpmu  \n"
                f"WHERE tpmu.cTanggal > '2023-01-01';")
    elif nama_table == 't_target_mapel' : 
        unique_select = ['ttm.cIdSekolahKelas','ttm.cIdKelompokUjian','ttm.cSemester','ttm.cTahunAjaran','ttm.cPersen','CURRENT_TIMESTAMP()','CURRENT_TIMESTAMP()']
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_TargetMapel ttm \n"
                f"WHERE ttm.cTahunAjaran  = '2023/2024'")
    
    elif nama_table == 't_target_pengerjaan_siswa' : 
        unique_select = ['ttps.cIdSekolahKelas','ttps.cTargetHarian','ttps.cTotalTarget','CURRENT_TIMESTAMP','ttps.cLastUpdate','ttps.cNoRegister']
        query = (f"SELECT  DISTINCT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_TargetPengerjaanSiswa ttps \n"
                f"JOIN db_GOIconsV2.t_Cluster_Siswa tcs on ttps.cNoRegister  = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_TahunAjaran = '2023/2024'")
    return query

