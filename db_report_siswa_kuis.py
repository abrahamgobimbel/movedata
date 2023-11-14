import os
import functioninput

def query_select(nama_table) :
    
    if nama_table == 't_hasil_jawaban_3' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SD ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas = 3\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    
    elif nama_table == 't_hasil_jawaban_4' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SD ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas = 4\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
        
    elif nama_table == 't_hasil_jawaban_5' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SD ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas = 5\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
        
    elif nama_table == 't_hasil_jawaban_6' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SD ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas = 6\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")    
    elif nama_table == 't_hasil_jawaban_7' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SMP ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas = 7\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    elif nama_table == 't_hasil_jawaban_8' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SMP ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas = 8\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    elif nama_table == 't_hasil_jawaban_9' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SMP ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas = 9\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    elif nama_table == 't_hasil_jawaban_10' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SMA ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas in (10,11,16,17,18,25,49)\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    elif nama_table == 't_hasil_jawaban_11' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_SMA ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas in (12,13,19,20,21,26,34,36,38,40,50)\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    elif nama_table == 't_hasil_jawaban_12' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_12IPA ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas in (14,15,22,23,24,27,32,35,37,39,41,51)\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    elif nama_table == 't_hasil_jawaban_13' : 
        unique_select = ['cNoRegister','cKodeSoal','cdetiljawaban','cdetilhasil','cLastUpdate',"'2023/2024'",'cKeterangan']
        query = (f"SELECT {', '.join(unique_select)}\n"
                f"FROM db_GOKreasi.t_hasiljawaban_Alumni ths\n" 
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on ths.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE tcs.c_IdSekolahKelas in (28,29,30)\n"
                f"and tcs.c_TahunAjaran = '2023/2024'\n"
                f"and ths.cKodeSoal LIKE 'EMMA-%'")
    elif nama_table == 't_peserta_to' : 
        unique_select = ["tp.cNoRegister" , "tp.cKodeSoal" , "tp.cTanggalTO" , "tp.cTglMulai" , "tp.cTglSelesai" , "tp.cPersetujuan", "tp.cFlag" , "JSON_EXTRACT(tp.cKeterangan , '$.merk') AS merk", "JSON_EXTRACT(tp.cKeterangan, '$.versi') AS versi", "JSON_EXTRACT(tp.cKeterangan, '$.versi_os') AS versi_os", "tp.cSudahSelesai" , "tp.cOK" , "CURRENT_TIMESTAMP", "CURRENT_TIMESTAMP"]
        query = (f"SELECT  DISTINCT  {', '.join(unique_select)}\n"
                 f"FROM db_GOKreasi.tbl_pesertato tp \n"
                 f"join db_GOIconsV2.t_Cluster_Siswa tcs on tp.cNoRegister  = tcs.c_NoRegistrasi\n"
                 f"and tcs.c_TahunAjaran = '2023/2024'\n"
                 f"and tp.cKodeSoal LIKE 'EMMA-%'")
    return query
