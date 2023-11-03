def query_select(nama_table) :
    if nama_table == 't_paket_dan_bundel' :
        query = f"SELECT pdb.c_idbundel, pdb.c_kodepaket, pdb.c_urutan, pdb.c_Updater, pdb.c_LastUpdate FROM db_produk.t_paketdanbundel pdb JOIN (select distinct c_IdBundel, c_kodepaket from t_paketdanbundel) upd ON upd.c_IdBundel = pdb.c_idbundel and upd.c_KodePaket = pdb. c_kodepaket;"
    return query    