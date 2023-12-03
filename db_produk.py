import os
import functioninput

def query_select(nama_table) :
    
    
    if nama_table == 't_bundling' : 
        file_path_bundling = 'db_produk_bundling.txt'
        data_bundling = functioninput.data_input(file_path_bundling)
        query = f"SELECT DISTINCT tb.* FROM db_GOIconsV2.t_Bundling tb WHERE c_IdBundling IN ({', '.join(data_bundling)});"
        if data_bundling == [] :
            query = (f"SELECT tb.*\n"
                     "FROM db_GOIconsV2.t_Bundling tb\n"
                     "JOIN db_GOIconsV2.t_ProdukMix tpm on tb.c_IdProdukMix  = tpm.c_IdProdukMix\n"
                     "JOIN db_GOIconsV2.t_MKT_JenisKelas tmjk on tb.c_IdJenisKelas = tmjk.c_IdJenisKelas and tpm.c_IdJenisKelas = tmjk.c_IdJenisKelas;")
    
    elif nama_table == 't_isi_tob' : 
        file_path_tob = 'db_produk_tob.txt'
        query = (f"SELECT tit.*\n"
                f"from t_IsiTOB tit \n"
                "JOIN t_TOB tt on tit.c_KodeTOB = tt.c_KodeTOB\n"
                "JOIN t_PaketSoal tps on tit.c_KodePaket = tps.c_KodePaket \n"
                "JOIN db_GOIconsV2.t_MKT_JenisProduk tmjp on tps.c_JenisPaket = tmjp.c_IdJenisProduk")
    
    elif nama_table == 't_isi_produk_mix' :
        query = (f"SELECT tipm.*, CURRENT_TIMESTAMP()\n"
                 f"FROM db_GOIconsV2.t_IsiProdukMix tipm\n"
                "JOIN db_GOIconsV2.t_Produk tp on tipm.c_IdProduk = tp.c_IdProduk\n"
                "JOIN db_GOIconsV2.t_ProdukMix tpm on tipm.c_IdProdukMix - tpm.c_IdProdukMix\n"
                "JOIN db_GOIconsV2.t_MKT_JenisKelas tmjk on tp.c_IdJenisKelas  = tmjk.c_IdJenisKelas and tpm.c_IdJenisKelas = tmjk.c_IdJenisKelas \n"
                "JOIN db_GOIconsV2.t_MKT_JenisProduk tmjp on tp.c_IdJenisProduk = tmjp.c_IdJenisProduk;" 
                )
    
    elif nama_table == 't_jenis_kelas' : 
        query = f"SELECT * FROM db_GOIconsV2.t_MKT_JenisKelas;"
    
    
    elif nama_table == 't_jenis_produk' :
        query = f"SELECT *, current_timestamp FROM db_GOIconsV2.t_MKT_JenisProduk;"
    
    
    elif nama_table == 't_paket_dan_bundel' :
        query = (f"SELECT tpdb.c_IdBundel , tpdb.c_KodePaket , tpdb.c_Urutan , tpdb.c_Updater , tpdb.c_LastUpdate\n" 
                f"from t_PaketDanBundel tpdb \n")
    
    elif nama_table == 't_paket_soal' :
        unique_select = ["tps.c_KodePaket", "tps.c_Deskripsi" , "tps.c_TahunAjaran" ,"tps.c_TanggalBerlaku", 
                         "tps.c_TanggalKedaluwarsa","tps.c_JenisPaket" , "tps.c_IdTingkatKelas" , "tps.c_IsBlockingTime" , 
                         "tps.c_IsRandom" , "'Aktif' as c_Status" , "tps.c_Updater" ,"tps.c_LastUpdate", "CURRENT_TIMESTAMP" ]
        file_path_tob = 'db_produk_kode_tob.txt'
        data_tob = functioninput.data_input(file_path_tob)
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                 f"from db_banksoalV2.t_PaketSoal tps \n"
                 f"JOIN db_banksoalV2.t_IsiTOB tit ON tit.c_KodePaket = tps.c_KodePaket\n"
                 f"WHERE tit.c_KodeTOB IN ({', '.join(data_tob)});") 
        if data_tob == [] :
            query = (f"SELECT {', '.join(unique_select)}\n"
                 f"from db_banksoalV2.t_PaketSoal tps \n"
                 "JOIN db_GOIconsV2.t_MKT_JenisProduk tmjp on tps.c_JenisPaket = tmjp.c_IdJenisProduk ")
    
    
    elif nama_table == 't_produk' :
        file_path_produk = 'db_produk_produk.txt'
        data_produk = functioninput.data_input(file_path_produk)
        query = (f"SELECT DISTINCT tp.*\n"
                f"FROM db_GOIconsV2.t_Produk tp\n"
                f"WHERE tp.c_IdProduk IN ({', '.join(data_produk)})")
        if data_produk == [] : 
            data_produk_mix = []
            file_path_produk_mix = 'db_produk_produk_mix.txt'
            if os.path.exists(file_path_produk_mix) :
                with open('db_produk_produk_mix.txt', 'r') as file:
                    for line in file : 
                        data_produk_mix.append(line.strip())
            data_produk_mix = list(set(data_produk_mix))
            query = (f"SELECT DISTINCT tp.*\n"
                    f"FROM db_GOIconsV2.t_Produk tp\n"
                    f"JOIN db_GOIconsV2.t_IsiProdukMix tispm USING (c_IdProduk)"
                    f"WHERE tispm.c_IdProdukMix IN ({', '.join(data_produk_mix)});")
            if data_produk_mix == [] : 
                query = (f"SELECT DISTINCT tp.*\n"
                        f"FROM db_GOIconsV2.t_Produk tp\n"
                        "JOIN db_GOIconsV2.t_MKT_JenisProduk tmjp on tp.c_IdJenisProduk = tmjp.c_IdJenisProduk \n"
                        "JOIN db_GOIconsV2.t_MKT_JenisKelas tmjk on tp.c_IdJenisKelas = tmjk.c_IdJenisKelas ;"
                        )
                
    elif nama_table == 't_produk_mix' :
        unique_select = ['tpm.c_IdProdukMix' , 'tpm.c_NamaProdukMix' , 'tpm.c_IdJenisKelas' , 'tpm.c_IdKurikulum' , 
                        'tpm.c_IdSekolahKelas' ,' tpm.c_IsKerjaSama' , 'tpm.c_IsJenisPertemuan' , 'tpm.c_JumS1' , 
                        'tpm.c_JumS2' , 'tpm.c_JumS3' , 'tpm.c_IsJaminan' , 'tpm.c_Zona' , 'tpm.c_KodeUnik' , 
                        'tpm.c_Status' , 'tpm.c_Updater' , 'tpm.c_Lastupdate' , 'CURRENT_TIMESTAMP']
        file_path_produk_mix = 'db_produk_produk_mix.txt'
        data_produk_mix = functioninput.data_input(file_path_produk_mix)
        query = (f"SELECT {', '.join(unique_select)}\n"
                 f"FROM db_GOIconsV2.t_ProdukMix tpm\n"
                 f"WHERE c_IdProdukMix IN ({', '.join(data_produk_mix)});")
        if data_produk_mix == [] :
            file_path_bundling = 'db_produk_bundling.txt'
            data_bundling = functioninput.data_input(file_path_bundling)
            query = (f"SELECT {', '.join(unique_select)}\n"
                    f"FROM db_GOIconsV2.t_ProdukMix tpm\n"
                    f"JOIN db_GOIconsV2.t_Bundling tb USING (c_IdProdukMix)"
                    f"WHERE tb.c_IdBundling IN ({', '.join(data_bundling)});")
            if data_bundling == [] :
                query = (f"SELECT {', '.join(unique_select)}\n"
                    f"FROM db_GOIconsV2.t_ProdukMix tpm\n"
                    "JOIN db_GOIconsV2.t_MKT_JenisKelas tmjk on tpm.c_IdJenisKelas = tmjk.c_IdJenisKelas;")

        
        
    elif nama_table == 't_produk_tob' :
        file_path_tob ='db_produk_kode_tob.txt'
        data_tob = functioninput.data_input(file_path_tob)
        query = (f"SELECT tpt.* FROM t_ProdukTOB tpt\n")
    
    
    elif nama_table == 't_tob' : 
        unique_select = ["tt.c_KodeTOB" , "c_NamaTOB" , "c_JarakAntarPaket" , "c_TanggalAktif", 
                         "c_TanggalKadaluarsa","tt.c_TahunAjaran" , "tt.c_Jenis" , "tt.c_IsTOMerdeka" ,
                         "c_Status" , "tt.c_Updater" , "tt.c_LastUpdate" , "CURRENT_TIMESTAMP()" ]
        file_path_tob = 'db_produk_kode_tob.txt'
        data_tob = functioninput.data_input(file_path_tob)
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                 f"FROM db_banksoalV2.t_TOB tt\n"
                 f"WHERE tt.c_KodeTOB in ({', '.join(data_tob)});")
        if data_tob == [] :
            file_path_produk = 'db_produk_produk.txt'
            data_produk = functioninput.data_input(file_path_produk)
            query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                 f"FROM db_banksoalV2.t_TOB tt\n"
                 f"JOIN db_banksoalV2.t_ProdukTOB tpt ON tt.c_KodeTOB = tpt.c_KodeTOB"
                 f"WHERE tpt.c_IdKomponenProduk in ({', '.join(data_produk)});")
            if data_produk == [] :
                data_produk_mix = []
                if data_produk_mix ==[]:
                    data_bundling = []
                    if data_bundling == [] :
                        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                                f"FROM db_banksoalV2.t_TOB tt\n") 
    
                
    
    return query    