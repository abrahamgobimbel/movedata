def query_select(sumber) :
    if sumber == "t_bab" :
        query = (f"SELECT c_kodebab,\n"
                f"c_NamaBab,\n"
                f"c_Upline,\n"
                f"c_Peluang,\n"
                f"c_Status,\n"
                f"c_Updater,\n"
                f"c_LastUpdate,\n"
                f"current_timestamp\n"
                f"FROM db_materi.t_bab;"
                f"JOIN (SELECT DISTINCT c_kodebab FROM t_bab) kodebab\n"
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
    return query