import os
import functioninput

def query_select(nama_table) :
    if nama_table == 't_juklak' :
        query = ("SELECT *\n"
                "from db_IsianDPPV3.t_Juklak tj\n"
                "where c_TahunAjaran = '2023/2024'")
    elif nama_table == 't_juklak_detail' :
        query = ""
    elif nama_table == 't_kelompok_ujian' : 
        query = (f"SELECT *, CURRENT_TIMESTAMP() \n"
                f"from db_banksoalV2.t_KelompokUjian tku ")
    elif nama_table == 't_kurikulum' :
        query = (f"SELECT *, CURRENT_TIMESTAMP()\n" 
        f"from db_banksoalV2.t_Kurikulum tk  ")
    
    elif nama_table == 't_mapel_kelompok_ujian' :
        query = (f"SELECT tmu.*\n"
                f"FROM db_banksoalV2.t_MapelUji tmu\n"
                "join db_banksoalV2.t_MataPelajaran tmp on tmu.c_IdMataPelajaran = tmp.c_IdMataPelajaran \n"
                "join db_banksoalV2.t_KelompokUjian tku on tmu.c_IdKelompokUjian = tku.c_IdKelompokUjian \n")
    elif nama_table == 't_mata_pelajaran' :
        query = (f"SELECT *, CURRENT_TIMESTAMP()\n" 
                f"FROM db_banksoalV2.t_MataPelajaran tmp  ")
    
    elif nama_table == 't_sekolah' : 
        unique_select = ['ts.c_IdSekolah', 'ts.c_NamaSekolah', 'ts.c_IdDistrict c_IdSekolah', 'ts.c_JenjangPendidikan', 'ts.c_AlamatSekolah', 'ts.c_KodeSekolahDapodik', 'ts.c_Status', 'ts.c_Updater', 'ts.c_LastUpdate', 'CURRENT_TIMESTAMP()']
        query = (f"select  {', '.join(unique_select)}\n"
                 f"FROM db_GOIconsV2.t_Sekolah ts ")
    
    elif nama_table == 't_sekolah_kelas' :
        query = (f"SELECT *, CURRENT_TIMESTAMP() \n"
                f"FROM db_GOIconsV2.t_SekolahKelas tsk")
        
    elif nama_table == 't_sekolah_siswa' : 
        query = (f"select distinct tcs.c_IdSekolah , tcs.c_NoRegistrasi ,'go-bimbel',tcs.c_LastUpdate\n" 
                f"FROM db_GOIconsV2.t_Cluster_Siswa tcs \n"
                f"WHERE tcs.c_TahunAjaran  ='2023/2024'")
    
    elif nama_table == 't_semester' :
        query = (f"SELECT *\n"
                f"FROM db_GOIconsV2.t_Semester ts ")
    
    elif nama_table == 't_tahun_ajaran' :
        unique_select = ['tta.c_TahunAjaran','tta.c_IsDefault','tta.c_Status','tta.c_awal','tta.c_akhir','tta.c_Updater','tta.c_LastUpdate','CURRENT_TIMESTAMP()']
        query = (f"select  {', '.join(unique_select)}\n"
                 f"from db_GOIconsV2.t_TahunAjaran tta")
    return query