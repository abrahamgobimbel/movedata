def query_select(nama_table) :
    if nama_table == 't_bundling' : 
        query = f"SELECT c_IdBundling, c_IdProdukMix, c_IdPenanda, c_IdJenisKelas, c_IdSekolahKelas, c_IsKerjaSama, c_IsOnline, c_NamaBundling, c_TanggalAwal, c_TanggalAkhir, c_Deskripsi, c_HargaPT, c_HargaFasilitas, c_BiayaOperasional, c_TahunAjaran, c_JenisBiayaOperasional, c_Margin, c_BiayaTercantum, c_HargaSebelum, c_HargaPenyesuaian, c_HargaTotal, c_Status, c_Updater, c_Lastupdate, c_Insert, c_IdPola, c_IsTeaser, c_Perpanjangan, c_IsJaminan100 FROM db_produk.t_bundling;"
    elif nama_table == 't_isi_tob' : 
        query = f"SELECT it.* FROM db_produk.t_isitob it join (select distinct c_kodetob, c_kodepaket, c_nomorurut from t_isitob) upd on it.c_kodetob = upd.c_kodetob and it.c_kodepaket = upd.c_kodepaket and it.c_nomorurut = upd.c_nomorurut;"
    elif nama_table == 't_jenis_kelas' : 
        query = f"SELECT * FROM db_produk.t_mkt_jeniskelas;"
    elif nama_table == 't_jenis_produk' :
        query = f"SELECT *, current_timestamp FROM db_produk.t_mkt_jenisproduk;"
    elif nama_table == 't_paket_dan_bundel' :
        query = f"SELECT pdb.c_idbundel, pdb.c_kodepaket, pdb.c_urutan, pdb.c_Updater, pdb.c_LastUpdate FROM db_produk.t_paketdanbundel pdb JOIN (select distinct c_IdBundel, c_kodepaket from t_paketdanbundel) upd ON upd.c_IdBundel = pdb.c_idbundel and upd.c_KodePaket = pdb. c_kodepaket;"
    elif nama_table == 't_paket_soal' :
        query = f"SELECT *, current_timestamp() FROM db_produk.t_paketsoal;"
    elif nama_table == 't_produk' :
        query = f"SELECT * FROM db_produk.t_produk;"
    elif nama_table == 't_produk_mix' :
        query = f"SELECT c_idprodukmix, c_NamaProdukMix, c_IdJenisKelas, c_IdKurikulum, c_IdSekolahKelas, c_IsKerjaSama, c_IsJenisPertemuan, c_JumS1, c_JumS2, c_jums3, c_IsJaminan, c_Zona, c_KodeUnik, c_Status, c_Updater, c_Lastupdate, current_timestamp FROM db_produk.t_produkmix;"
    elif nama_table == 't_produk_tob' :
        query = f"select p.* from t_produktob p join (select c_kodetob, c_idkomponenproduk from t_produktob) upd where p.c_kodetob = upd.c_kodetob and p.c_idkomponenproduk = upd.c_idkomponenproduk;"
    elif nama_table == 't_tob' : 
        query = f"SELECT c_KodeTOB, c_NamaTOB, c_JarakAntarPaket, c_TanggalAktif, c_TanggalKadaluarsa, c_TahunAjaran, c_Jenis, c_IsTOMerdeka, c_Status, c_Updater, c_LastUpdate, current_timestamp() FROM db_produk.t_tob;"
    return query    