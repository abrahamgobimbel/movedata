def query_select(sumber) :
    if sumber == 't_bah' :
        query = f"SELECT a.* FROM {sumber} a JOIN (SELECT DISTINCT c_idbah FROM {sumber}) idbah ON a.c_idbah = idbah.c_idbah;"
    elif sumber == "t_cluster_pengajar_idpp" :
        query = f"SELECT * FROM {sumber} a JOIN (SELECT DISTINCT c_IdPengajar FROM {sumber}) idpengajar ON a.c_IdPengajar = idpengajar.c_IdPengajar;"
    elif sumber == 't_daftar_kegiatan_kbm' :
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
    elif sumber == 't_presensisiswa' :
        query = (
            f"SELECT p.*\n" 
            f"FROM db_kbm.t_presensisiswa p\n"
            f"JOIN (select distinct c_IdRencana, c_NoRegistrasi from t_presensisiswa) id\n"
            f"ON id.c_IdRencana = p.c_idrencana and id.c_NoRegistrasi=p.c_noregistrasi ;"
        )    
    elif sumber =='t_rencanakerja_kbm' : 
    return query