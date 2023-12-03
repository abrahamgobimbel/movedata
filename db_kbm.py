def query_select(nama_table) :
    
    if nama_table == 't_anggota_tst' :
        query = (f"SELECT c_IdPermintaan, c_NIS,\n"
                f"CASE WHEN c_IsKetua = 'Y' THEN true ELSE false END AS is_ketua_boolean,\n"
                f"CASE when c_IsHadir = 'Y' THEN true else false end as is_hadir_boolean,\n"
	            f"c_idrealisasi, c_jamdatang, c_jampulang, c_updater, c_lastupdate, CURRENT_TIMESTAMP()\n"
                f"FROM db_IsianDPPV3.t_AnggotaTST tat\n"
                f"where c_lastupdate BETWEEN DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 MONTH)\n"
                f"AND DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL 1 MONTH);")
    
    elif nama_table == 't_bah' :
        query = (f"SELECT *\n"
                f"FROM db_banksoalV2.t_BAH  tb \n"  
                f"WHERE tb.c_TahunAjaran = '2023/2024'")
    
    elif nama_table == 't_bah_kelas' :
        query = (f"SELECT * FROM db_banksoalV2.t_BAHKelas tb")
    
    elif nama_table == "t_cluster_pengajar" :
        query = (f"SELECT *\n"
                f"from db_GOIconsV2.t_Cluster_Pengajar_iDPP tcpid ")
    elif nama_table == 't_daftar_kegiatan_kbm' : 
        query = f"SELECT row_number() OVER (ORDER BY c_id) AS row_num, c_Nama, JSON_UNQUOTE(c_Deskripsi->'$.c_DesSiswa') AS c_DesSiswa, JSON_UNQUOTE(c_Deskripsi->'$.c_DesPetugas') AS c_DesPetugas, JSON_UNQUOTE(c_Deskripsi->'$.c_DesPengajar') AS c_DesPengajar, CASE WHEN JSON_UNQUOTE(c_Info->'$.c_KR') = 'true' THEN 1 ELSE 0 END AS c_KR, CASE WHEN JSON_UNQUOTE(c_Info->'$.c_PF') = 'true' THEN 1 ELSE 0 END AS c_PF, CASE WHEN JSON_UNQUOTE(c_Info->'$.c_PH') = 'true' THEN 1 ELSE 0 END AS c_PH, CASE WHEN JSON_UNQUOTE(c_Info->'$.c_PK') = 'true' THEN 1 ELSE 0 END AS c_PK, JSON_UNQUOTE(c_Info->'$.c_Pengali') AS c_Pengali, CASE WHEN JSON_UNQUOTE(c_Info->'$.c_IsRelatif') = 'Y' THEN 1 ELSE 0 END AS c_IsRelatif, JSON_UNQUOTE(c_Info->'$.c_PengaliSD') AS c_PengaliSD, JSON_UNQUOTE(c_Info->'$.c_WaktuMaximal') AS c_WaktuMaximal, JSON_UNQUOTE(c_Info->'$.c_WaktuMinimal') AS c_WaktuMinimal, JSON_UNQUOTE(c_Info->'$.c_IdJenisPetugas') AS c_IdJenisPetugas, JSON_UNQUOTE(c_Info->'$.c_DasarPenggajian') AS c_DasarPenggajian, c_Updater, c_lastupdate, CURRENT_TIMESTAMP AS current_time_alias, CASE WHEN c_parents = '0201' THEN 1 ELSE 2 END AS c_id_info_kegiatan FROM db_IsianDPPV3.t_BankData WHERE c_parents IN ('0202', '0201') ORDER BY c_id;"

    elif nama_table == 't_feedback_pengajaran' :
        query = f"SELECT * FROM db_kbm.t_feedbackpengajaran WHERE c_LastUpdate >= DATE_SUB(CURDATE(), INTERVAL 2 WEEK) AND c_LastUpdate <= DATE_ADD(CURDATE(), INTERVAL 2 WEEK);"
    
    elif nama_table == 't_isi_bah' :
        query = (f"SELECT c_IdBAH , c_KodeBab , c_Pertemuan , c_Updater , c_LastUpdate  \n"
                f"FROM db_banksoalV2.t_IsiBAH tib ")
    
    elif nama_table == 't_kelas' :
        query = (f"select * \n"
                f"from db_GOIconsV2.t_Kelas tk\n"
                f"where c_TahunAjaran = '2023/2024'")
        
    elif nama_table == 't_kelas_siswa' :
        query = (f"SELECT DISTINCT tk.c_IdKelas, tcs.c_NoRegistrasi, tk.c_Updater , tk.c_LastUpdate \n"
                f"FROM db_GOIconsV2.t_Kelas tk \n"
                f"JOIN db_GOIconsV2.t_Cluster_Siswa tcs USING (c_idkelas)\n"
                f"WHERE tcs.c_TahunAjaran = '2023/2024'")
    
    elif nama_table == 't_permintaan_tst' :
        query = (f"SELECT *\n"
                f"FROM db_IsianDPPV3.t_PermintaanTST tpt\n"
                f"WHERE c_tanggalpermintaan > DATE_SUB(CURDATE(), INTERVAL 1 MONTH)\n"
                f"AND c_TanggalPermintaan <= DATE_ADD(CURDATE(), INTERVAL 1 MONTH);")
    
    elif nama_table == 't_presensi_siswa' :
        query = (f"SELECT p.* FROM db_GOIconsV2.t_PresensiSiswa p\n"
                f"JOIN (select distinct c_IdRencana, c_NoRegistrasi from db_GOIconsV2.t_PresensiSiswa) id\n"
                f"ON id.c_IdRencana = p.c_idrencana and id.c_NoRegistrasi=p.c_noregistrasi\n"
                f"WHERE p.c_tanggal >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK)\n" 
                f"AND p.c_tanggal <= DATE_ADD(CURDATE(), INTERVAL 1 WEEK);")
    
    elif nama_table == 't_rencana_kerja_kbm' :
        query = f"SELECT r.c_IdRencana, r.c_IdGedungPelaksana, r.c_NIK, r.c_JamAwal, r.c_JamAkhir,  r.c_idkegiatan, r.c_Info1 , r.c_Info2, r.c_Info3, r.c_TahunAjaran, r.c_StatusRencana, r.c_UpdaterRencana, r.c_LastUpdate, JSON_UNQUOTE(r.c_Keterangan->'$.RENCANA') AS c_rencana, JSON_UNQUOTE(r.c_Keterangan->'$.REALISASI') AS c_realisasi, JSON_UNQUOTE(r.c_Keterangan->'$.siswahadir') AS c_siswahadir FROM db_IsianDPPV3.t_RencanaKerja r WHERE (c_idkegiatan LIKE '0201%' OR c_idkegiatan LIKE '0202%') AND r.c_JamAwal >= DATE_SUB(CURDATE(), INTERVAL 2 WEEK) AND r.c_JamAwal <= DATE_ADD(CURDATE(), INTERVAL 2 WEEK);"
    return query