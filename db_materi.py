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
    return query