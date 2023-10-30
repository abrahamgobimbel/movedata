def query_select(sumber, primary_key) :
    if sumber == "t_cluster_pengajar_idpp" :
        query = f"SELECT * FROM {sumber} a join (select distinct {primary_key} from db_materi.t_cluster_pengajar_idpp) idpengajar ON a. c_idpengajar = idpengajar;"
    elif sumber == "t_bankdata"
        query = f"select * from {sumber} where c_parents = 0201"    