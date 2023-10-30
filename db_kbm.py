def query_select(sumber) :
    if sumber == 't_bah' :
        query = f"SELECT a.* FROM {sumber} a JOIN (SELECT DISTINCT c_idbah FROM {sumber}) idbah ON a.c_idbah = idbah.c_idbah;"
    elif sumber == "t_cluster_pengajar_idpp" :
        query = f"SELECT * FROM {sumber} a JOIN (SELECT DISTINCT c_IdPengajar FROM {sumber}) idpengajar ON a.c_IdPengajar = idpengajar.c_IdPengajar;"
    return query