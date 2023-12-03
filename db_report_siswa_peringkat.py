def query_select(nama_table) :
    
    if nama_table == 't_pengerjaan_mata_uji' : 
        unique_select = ['tpmu.cNoRegistrasi','tpmu.cIdpelajaran','tpmu.cTanggal','tpmu.cSumber','tpmu.cJumlahPengerjaan','tpmu.cJumlahBenar','CURRENT_TIMESTAMP()','tpmu.cLastUpdate','tcs.c_IdBundling']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_pengerjaanMataUji tpmu\n"
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on tpmu.cNoRegistrasi = tcs.c_NoRegistrasi\n"
                f"join db_GOIconsV2.t_Bundling tb on tcs.c_IdBundling = tb.c_IdBundling\n"
                f"join db_GOIconsV2.t_ProdukMix tpm on tb.c_IdProdukMix = tpm.c_IdProdukMix\n" 
                f"join db_GOIconsV2.t_IsiProdukMix tipm on tpm.c_IdProdukMix = tipm.c_IdProdukMix\n"
                f"join db_GOIconsV2.t_Produk tp on tp.c_IdProduk = tipm.c_IdProdukMix\n"
                f"join db_banksoalV2.t_ProdukTOB tpt on tp.c_IdProduk = tpt.c_IdKomponenProduk\n"
                f"join db_banksoalV2.t_TOB tt on tt.c_KodeTOB = tpt.c_KodeTOB\n"
                f"join db_banksoalV2.t_IsiTOB tit on tit.c_KodeTOB = tit.c_KodePaket\n"
                f"join db_banksoalV2.t_PaketSoal tps on tit.c_KodePaket = tps.c_KodePaket\n"
                f" join db_banksoalV2.t_PaketDanBundel tpdb on tpdb.c_KodePaket = tps.c_KodePaket\n"
                f"join db_banksoalV2.t_BundelSoal tbs on tpdb.c_IdBundel = tbs.c_IdBundel and tbs.c_IdKelompokUjian = tpmu.cIdpelajaran\n"
                f"where tcs.c_TahunAjaran = '2023/2024'\n"
                f"and tpmu.cTanggal  < '2023-11-24';"
                )
 
    elif nama_table == 't_peringkat_new' :
        unique_select = ['tpn.c_id', 'tpn.cnoregister', 'tps.c_nama_lengkap', 'tpn.ctotal', 'tps.c_id_sekolah_kelas', 'tps.c_id_kota', 'tk.c_kota', 'tps.c_id_gedung', 'tg.c_nama_gedung', 'tpn.ctahunajaran', 'tpn.clastupdate', 'current_timestamp','tpn.cdetil']
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                f"FROM \n"
                f"    t_peringkatnew tpn \n"
                f"JOIN \n"
                f"    t_produk_siswa tps on tps.c_no_register = tpn.cnoregister\n"
                f"JOIN \n"
                f"    t_kota tk on tps.c_id_kota  = tk.c_id_kota\n"
                f"JOIN \n"
                f"    t_gedung tg on tg.c_id_gedung = tps.c_id_gedung ;\n"
                )
    elif nama_table == 't_peringkat_racing_new' : 
        query = (f"select row_number() OVER (), tp.c_NoRegistrasi , tcs.c_NamaLengkap,\n"
                 f"tcs.c_IdBundling , tp.c_KodeTOB , tp.c_KodeSoal , tp.c_Skor , tp.c_SkorPersen, \n"
                 f"tp.c_IdSekolahKelas , tp.c_IdPenanda , tp2.c_Penanda , tp.c_IdGedung , tg.c_NamaGedung, \n"
                 f"tp.c_MingguKe , tp.c_BulanKe , tp.c_SemesterKe , tp.c_TahunAjaran , tp.c_LastUpdate , CURRENT_TIMESTAMP() \n"
                 f"from db_GOKreasi.t_peringkatracing tp \n"
                 f"join db_GOIconsV2.t_Cluster_Siswa tcs on tcs.c_NoRegistrasi = tp.c_NoRegistrasi \n"
                 f"and tcs.c_IdSekolahKelas = tp.c_IdSekolahKelas and tcs.c_IdPenanda = tp.c_IdPenanda \n"
                 f"and tcs.c_IdGedung = tp.c_IdGedung join db_GOIconsV2.t_Penanda tp2 on tp.c_IdPenanda = tp2.c_IdPenanda \n"
                 
                 f"join db_GOIconsV2.t_Gedung tg on tg.c_IdGedung = tp.c_IdGedung where tcs.c_TahunAjaran = '2023/2024'")
    elif nama_table == 't_peringkat_new_temporary' :
        query = ("SELECT row_number() OVER (), tp.cNoRegister, tcs.c_NamaLengkap,\n"
                "tp.ctotal, tcs.c_IdSekolahKelas, tcs.c_IdPenanda, tp2.c_Penanda,\n"
                "tcs.c_IdGedung, tg.c_NamaGedung, tcs.c_TahunAjaran, CURRENT_TIMESTAMP,\n"
                "CURRENT_TIMESTAMP, tcs.c_IdBundling,\n"
                "JSON_EXTRACT(tp.cdetil, '$.benarlevel1'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.benarlevel2'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.benarlevel3'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.benarlevel4'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.benarlevel5'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.salahlevel1'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.salahlevel2'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.salahlevel3'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.salahlevel4'),\n"
                "JSON_EXTRACT(tp.cdetil, '$.salahlevel5')\n"
                "from db_GOKreasi.t_peringkatnew tp\n"
                "join db_GOIconsV2.t_Cluster_Siswa tcs on tp.cNoRegister = tcs.c_NoRegistrasi\n"
                "join db_GOIconsV2.t_Penanda tp2 on tcs.c_IdPenanda = tp2.c_IdPenanda\n"
                "join db_GOIconsV2.t_Gedung tg on tcs.c_IdGedung = tg.c_IdGedung\n"
                "where tcs.c_IdSekolahKelas is not null\n"
                "and tcs.c_IdGedung is not null\n"
                "and tcs.c_TahunAjaran = '2023/2024'\n"
                "and tcs.c_IdBundling is not null;"
                )

    elif nama_table == 't_target_mapel' : 
        unique_select = ['ttm.cIdSekolahKelas','ttm.cIdKelompokUjian','ttm.cSemester','ttm.cTahunAjaran','ttm.cPersen','CURRENT_TIMESTAMP()','CURRENT_TIMESTAMP()']
        query = (f"SELECT  {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_TargetMapel ttm \n"
                f"WHERE ttm.cTahunAjaran  = '2023/2024'")
    
    elif nama_table == 't_target_pengerjaan_siswa' : 
        unique_select = ['ttps.cIdSekolahKelas','ttps.cTargetHarian','ttps.cTotalTarget','CURRENT_TIMESTAMP','ttps.cLastUpdate','ttps.cNoRegister', 'tcs.c_IdBundling']
        query = (f"SELECT  {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_TargetPengerjaanSiswa ttps \n"
                f"JOIN db_GOIconsV2.t_Cluster_Siswa tcs on ttps.cNoRegister  = tcs.c_NoRegistrasi and ttps.cIdSekolahKelas = tcs.c_IdSekolahKelas \n"
                f"WHERE tcs.c_TahunAjaran = '2023/2024'")
    return query

