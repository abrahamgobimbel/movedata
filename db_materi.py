def query_select(sumber) :
    if sumber == "t_bab" :
        query = (f"SELECT a.c_kodebab,\n"
                f"a.c_NamaBab,\n"
                f"a.c_Upline,\n"
                f"a.c_Peluang,\n"
                f"a.c_Status,\n"
                f"a.c_Updater,\n"
                f"a.c_LastUpdate,\n"
                f"current_timestamp\n"
                f"FROM\n"
                f"db_materi.t_bab a\n"
                f"JOIN\n"
                f"(SELECT DISTINCT c_kodebab FROM t_bab) kodebab\n"
                f"ON kodebab.c_kodebab = a.c_kodebab;"
                )
    elif sumber == 't_buku' :
        query = (f"SELECT a.c_kodebuku,\n"
                f"a.c_NamaBuku,\n"
                f"a.c_Deskripsi,\n"
                f"a.c_Semester,\n"
                f"a.c_IdTingkatKelas,\n"
                f"a.c_IdKurikulum,\n"
                f"a.c_TahunAjaran,\n"
                f"a.c_Jenis,\n"
                f"a.c_IdKelompokUjian,\n"
                f"a.c_Updater,\n"
                f"a.c_LastUpdate,\n"
                f"current_timestamp\n"
                f"FROM\n"
                f"db_materi.t_buku a\n"
                f"JOIN\n"
                f"(SELECT DISTINCT c_kodebuku FROM t_buku) kodebuku\n"
                f"ON kodebuku.c_kodebuku = a.c_kodebuku;"
                )
    elif sumber == 't_produkbuku' :
        query = ("SELECT * FROM db_materi.t_produkbuku;")
    elif sumber == 't_bundelsoal' :
        query = (
                f"SELECT a.c_IdBundel, a.c_KodeBundel, a.c_Deskripsi, a.c_WaktuPengerjaan, a.c_TahunAjaran, a.c_JumlahSoal, a.c_Peruntukan, a.c_IdTingkatKelas, a.c_IdKelompokUjian, a.c_OpsiUrut, a.c_Status, a.c_Updater, a.c_LastUpdate, current_timestamp\n"
                f"FROM t_bundelsoal a\n"
                f"JOIN (SELECT DISTINCT c_IdBundel FROM t_bundelsoal) idbundel\n"
                f"ON idbundel.c_IdBundel = a.c_idbundel;"
                 )
    elif sumber == 't_mapel_bab' :
        query = (
                f"SELECT c_KodeBab, c_IdMataPelajaran, c_Updater, c_LastUpdate, current_timestamp() from t_bab\n"
                f"where c_IdMataPelajaran IS NOT NULL"
                 )
    elif sumber == 't_teori_bab' :
        query = (
                f"SELECT *, current_timestamp() FROM db_materi.t_teoribab;"
                 )
    elif sumber == 't_video_soal' :
        query = (
                f"SELECT c_IdVideo, c_JudulVideo, c_Keyword, c_Deskripsi, c_LinkVideo, c_Updater, c_LastUpdate, current_timestamp() FROM db_materi.t_videosoal;"
                 )
    elif sumber == 't_video_teori' :
        query = (
                f"SELECT c_IdVideo,c_JudulVideo,c_Deskripsi,c_LinkVideo,c_KodeBab,c_Level,c_Kelengkapan,c_Updater,c_LastUpdate,current_timestamp() FROM db_materi.t_videoteori;"
                 )
    elif sumber == 't_wacana' :
        query = (
                f"SELECT *, current_timestamp FROM db_materi_update.t_wacana;"
                 )
    return query

