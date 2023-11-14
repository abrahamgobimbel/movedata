import os
import functioninput

def query_select(nama_table) :
    
    if nama_table == "t_bab" :
        unique_select = ['tb.c_KodeBab' , 'tb.c_NamaBab' , 'tb.c_Upline' , 'tb.c_Peluang' , 
                        'tb.c_Status' , 'tb.c_Updater' , 'tb.c_LastUpdate' , 'CURRENT_TIMESTAMP()' ]
        file_path_tob = 'db_produk_kode_tob.txt'
        data_tob = functioninput.data_input(file_path_tob)
        query = (f"SELECT DISTINCT {','.join(unique_select)}\n "
                f"from db_banksoalV2.t_Bab tb \n"
                f"join db_banksoalV2.t_SoalBab tsb USING (c_KodeBab)\n"
                f"join db_banksoalV2.t_Soal USING (c_IdSoal)"
                f"JOIN db_banksoalV2.t_IsiSoalBundel USING (c_IdSoal)\n"
                f"JOIN db_banksoalV2.t_BundelSoal USING (c_IdBundel)\n"
                f"JOIN db_banksoalV2.t_PaketDanBundel USING (c_IdBundel)\n"
                f"JOIN db_banksoalV2.t_PaketSoal USING (c_KodePaket)\n"
                f"JOIN db_banksoalV2.t_IsiTOB tit USING (c_KodePaket)"
                f"WHERE tit.c_KodeTOB IN ({', '.join(data_tob)});")
        if data_tob == [] :
            query = (f"SELECT DISTINCT {','.join(unique_select)}\n"
                     f"from db_banksoalV2.t_Bab tb")
    
    elif nama_table == 't_buku' :
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
                f"db_banksoalV2.t_Buku a \n"
                f"where a.c_TahunAjaran = '2023/2024'"
                )
    
    elif nama_table == 't_buku_produk' :
        query = ("SELECT * FROM db_banksoalV2.t_ProdukBuku tpb ;")
    
    elif nama_table == 't_bundel_soal' :
        unique_select = ["tbs.c_IdBundel" , "tbs.c_KodeBundel" , "tbs.c_Deskripsi"  , "tbs.c_WaktuPengerjaan" , 
                         "tbs.c_TahunAjaran" ,"tbs.c_JumlahSoal" , "tbs.c_Peruntukan" , "tbs.c_IdTingkatKelas" , "tbs.c_IdKelompokUjian" , 
                         "tbs.c_OpsiUrut" , "tbs.c_Status" , "tbs.c_Updater" , "tbs.c_LastUpdate" , "CURRENT_TIMESTAMP()" ]
        file_path_tob = 'db_produk_kode_tob.txt'
        data_tob = functioninput.data_input(file_path_tob)
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                 f"FROM db_banksoalV2.t_BundelSoal tbs \n"
                 f"JOIN db_banksoalV2.t_PaketDanBundel tpdb USING (c_IdBundel)\n"
                 f"JOIN db_banksoalV2.t_PaketSoal USING (c_KodePaket)\n"
                 f"JOIN db_banksoalV2.t_IsiTOB tit USING (c_KodePaket)\n"
                 f"WHERE tit.c_KodeTOB in ({', '.join(data_tob)});")
        if data_tob == [] :
            query =(f"SELECT DISTINCT {', '.join(unique_select)}\n"
                    f"FROM db_banksoalV2.t_BundelSoal tbs \n"
                    f"where tbs.c_TahunAjaran = '2023/2024'")
    
    elif nama_table == 't_isi_buku' :
        unique_select = ['c_KodeBuku', 'c_KodeBab', 'c_Updater', 'c_LastUpdate']
        query =(f"SELECT DISTINCT {', '.join(unique_select)}\n"
                f"FROM db_banksoalV2.t_IsiBuku tbs \n")
        
    elif nama_table == 't_isi_bundel_soal' :
        query = (f"SELECT tisb.c_IdSoal , tisb.c_IdBundel , tisb.c_NomorSoal ,tisb.c_Updater , tisb.c_LastUpdate \n"
                 f"from db_banksoalV2.t_IsiSoalBundel tisb\n")
        
    elif nama_table == 't_mapel_bab' :
        query = (
                f"SELECT c_KodeBab, c_IdMataPelajaran, c_Updater, c_LastUpdate, current_timestamp() from db_banksoalV2.t_Bab\n"
                f"where c_IdMataPelajaran IS NOT NULL"
                 )
    
    elif nama_table == 't_paket_dan_bundel_materi' :
        query = (f"SELECT tpdb.c_IdBundel , tpdb.c_KodePaket , tpdb.c_Urutan , tpdb.c_Updater , tpdb.c_LastUpdate\n" 
                f"from t_PaketDanBundel tpdb \n")
    
    elif nama_table == 't_soal':
        unique_select = ["s.c_idsoal", "s.c_soal", "s.c_LevelKognitif", "s.c_TingkatKesulitan", "s.c_TipeSoal", "s.c_Opsi", "s.c_Solusi", "s.c_Upline", "s.c_TheKing", "s.c_MetodePengambilan", "s.c_SaranPenggunaan", "s.c_WaktuPengerjaanSoal", "s.c_IdSumberDetail", "s.c_NIKPembuat", "s.c_IsVerifikasi", "s.c_TanggalVerifikasi", "s.c_NIKVerifikasi", "s.c_Updater", "s.c_TanggalPembuatan", "s.c_LastUpdate" ]
        file_path_tob = 'db_produk_kode_tob.txt'
        data_tob = functioninput.data_input(file_path_tob)
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                 f"FROM db_banksoalV2.t_Soal s\n"
                 f"JOIN db_banksoalV2.t_IsiSoalBundel USING (c_IdSoal)\n"
                 f"JOIN db_banksoalV2.t_BundelSoal USING (c_IdBundel)\n"
                 f"JOIN db_banksoalV2.t_PaketDanBundel USING (c_IdBundel)\n"
                 f"JOIN db_banksoalV2.t_PaketSoal USING (c_KodePaket)\n"
                 f"JOIN db_banksoalV2.t_IsiTOB tit USING (c_KodePaket)"
                 f"WHERE tit.c_KodeTOB IN ({', '.join(data_tob)});")
        if data_tob == [] :
            query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                    f"FROM db_banksoalV2.t_Soal s\n")
    
    elif nama_table == 't_soal_bab' : 
        query = (f"SELECT tsb.c_IdSoal , tsb.c_KodeBab , tsb.c_Updater , tsb.c_Insert , tsb.c_LastUpdate\n"
                f"from db_banksoalV2.t_SoalBab tsb \n")
    
    elif nama_table == 't_soal_video_soal' :
        query = (f"SELECT DISTINCT c_IdVideo, c_IdSoal, c_Updater, c_LastUpdate, current_timestamp()\n"
                f"FROM db_banksoalV2.t_Soal\n"
                f"where c_IdVideo is not null and c_IdVideo != 0")   
    
    elif nama_table == 't_teori_bab' :
        query = (
                f"SELECT *, current_timestamp() FROM db_banksoalV2.t_TeoriBab;"
                )
    elif nama_table == 't_teori_bab_video' : 
        unique_select = ['tvt.c_IdVideo','tvt.c_IdTeoriBab','tvt.c_Updater','tvt.c_LastUpdate','CURRENT_TIMESTAMP']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_banksoalV2.t_VideoTeori tvt ")
    
    elif nama_table == 't_video_soal' :
        unique_select = ['c_IdVideo', 'c_JudulVideo', 'c_Keyword', 'c_Deskripsi', 'c_LinkVideo', 'c_Updater', 'c_LastUpdate', 'current_timestamp()']
        query = (
                f"SELECT {', '.join(unique_select)} FROM db_banksoalV2.t_VideoSoal;"
                )
    
    elif nama_table == 't_video_teori' :
        unique_select = ['c_IdVideo','c_JudulVideo','c_Deskripsi','c_LinkVideo','c_KodeBab','c_Level','c_Kelengkapan','c_Updater','c_LastUpdate','current_timestamp()']
        query = (
                f"SELECT {', '.join(unique_select)} FROM db_banksoalV2.t_VideoTeori;"
                 )
    
    elif nama_table == 't_wacana' :
        file_path_tob = 'db_produk_kode_tob.txt'
        data_tob = functioninput.data_input(file_path_tob)
        query = (f"SELECT DISTINCT tw.*, current_timestamp()\n" 
                 f"FROM db_banksoalV2.t_Wacana tw\n"
                 f"join db_banksoalV2.t_Soal ts using (c_IdWacana)"
                 f"join db_banksoalV2.t_IsiSoalBundel tisb USING (c_IdSoal)"
                 f"JOIN db_banksoalV2.t_BundelSoal USING (c_IdBundel)\n"
                 f"JOIN db_banksoalV2.t_PaketDanBundel USING (c_IdBundel)\n"
                 f"JOIN db_banksoalV2.t_PaketSoal USING (c_KodePaket)\n"
                 f"JOIN db_banksoalV2.t_IsiTOB tit USING (c_KodePaket)"
                 f"WHERE tit.c_KodeTOB IN ({', '.join(data_tob)});")
        if data_tob == [] :
            query = (f"SELECT DISTINCT tw.*, current_timestamp()\n" 
                    f"FROM db_banksoalV2.t_Wacana tw\n")
    
    elif nama_table == 't_wacana_soal' :
        query = (f"SELECT c_idsoal, c_idwacana, c_Updater, c_LastUpdate, current_timestamp()\n"
                f"FROM db_banksoalV2.t_Soal\n"
                f"where c_IdWacana is not null and c_IdWacana != 0")
    return query

