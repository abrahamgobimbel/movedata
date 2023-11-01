def query_select(nama_table) :
    if nama_table == 't_bah' :
        query = f"SELECT a.* FROM t_bah a JOIN (SELECT DISTINCT c_idbah FROM t_bah) idbah ON a.c_idbah = idbah.c_idbah;"
    elif nama_table == "t_cluster_pengajar_idpp" :
        query = f"SELECT * FROM t_cluster_pengajar_idpp a JOIN (SELECT DISTINCT c_IdPengajar FROM t_cluster_pengajar_idpp) idpengajar ON a.c_IdPengajar = idpengajar.c_IdPengajar;"
    elif nama_table == 't_daftar_kegiatan_kbm' :
        query = (f"SELECT row_number() OVER (ORDER BY c_id) AS row_num,\n"
                f"c_Nama,\n"
                f"JSON_UNQUOTE(c_Deskripsi->'$.c_DesSiswa') AS c_DesSiswa,\n"
                f"JSON_UNQUOTE(c_Deskripsi->'$.c_DesPetugas') AS c_DesPetugas,\n"
                f"JSON_UNQUOTE(c_Deskripsi->'$.c_DesPengajar') AS c_DesPengajar,\n"
                f"CASE WHEN JSON_UNQUOTE(c_Info->'$.c_KR') = 'true' THEN 1 WHEN JSON_UNQUOTE(c_Info->'$.c_KR') = 'false' THEN 0 END AS c_KR,\n"
                f"CASE WHEN JSON_UNQUOTE(c_Info->'$.c_PF') = 'true' THEN 1 WHEN JSON_UNQUOTE(c_Info->'$.c_PF') = 'false' THEN 0 END AS c_PF,\n"
                f"CASE WHEN JSON_UNQUOTE(c_Info->'$.c_PH') = 'true' THEN 1 WHEN JSON_UNQUOTE(c_Info->'$.c_PH') = 'false' THEN 0 END AS c_PH,\n"
                f"CASE WHEN JSON_UNQUOTE(c_Info->'$.c_PK') = 'true' THEN 1 WHEN JSON_UNQUOTE(c_Info->'$.c_PK') = 'false' THEN 0 END AS c_PK,\n"
                f"JSON_UNQUOTE(c_Info->'$.c_Pengali') AS c_Pengali,\n"
                f"CASE WHEN JSON_UNQUOTE(c_Info->'$.c_IsRelatif') = 'Y' THEN 1 WHEN JSON_UNQUOTE(c_Info->'$.c_IsRelatif') = 'N' THEN 0 END AS c_IsRelatif,\n"
                f"JSON_UNQUOTE(c_Info->'$.c_PengaliSD') AS c_PengaliSD,\n"
                f"JSON_UNQUOTE(c_Info->'$.c_WaktuMaximal') AS c_WaktuMaximal,\n"
                f"JSON_UNQUOTE(c_Info->'$.c_WaktuMinimal') AS c_WaktuMinimal,\n"
                f"JSON_UNQUOTE(c_Info->'$.c_IdJenisPetugas') AS c_IdJenisPetugas,\n"
                f"JSON_UNQUOTE(c_Info->'$.c_DasarPenggajian') AS c_DasarPenggajian,\n"
                f"c_Updater,\n"
                f"c_lastupdate,\n"
                f"current_timestamp\n"
                f"FROM t_bankdata\n"
                f"WHERE c_parents in('0202','0201')\n"
                f"ORDER BY c_id;")
    elif nama_table == 't_presensi_siswa' :
        query = (
            f"SELECT p.*\n" 
            f"FROM db_kbm.t_presensisiswa p\n"
            f"JOIN (select distinct c_IdRencana, c_NoRegistrasi from t_presensisiswa) id\n"
            f"ON id.c_IdRencana = p.c_idrencana and id.c_NoRegistrasi=p.c_noregistrasi ;"
        )    
    return query