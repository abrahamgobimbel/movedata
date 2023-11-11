def query_select(nama_table) :
    
    if nama_table == 't_hasil_empati_12' : 
        query = f"SELECT DISTINCT the.cNoRegister , the.cKodeTOB_Em , the.cKodePaket, the.cJumlahSoal , the.cJumlahBenar , the.cJumlahSalah , the.cIsBoleh , the.cNIKVerifikasi , the.cLastUpdate , CURRENT_TIMESTAMP() FROM db_GOKreasi.t_hasilEmpati the join db_GOIconsV2.t_Cluster_Siswa tcs where tcs.c_TahunAjaran ='2023/2024' and tcs.c_IdSekolahKelas = 15 and the.cKodeTOB_Em in ( 16774, 16779, 17433, 16773, 16776, 17436, 16775, 17435, 17434, 16777, 16778, 17437, 17438, 17439 ) and cNoRegister ='000101825501'"
    return query