import os
import functioninput

def query_select(nama_table) :
    
    if nama_table == 't_karyawan' : 
        unique_select = [
            'cNIK', 'cNamaLengkap', 'cEmail', 'cPilihan', 'cSiapa',
            'null as cIdDevice', 'cNomorHP', 'cStatus', 'cCreated',' null as cLastLogin'
        ]
        query = (f"SELECT DISTINCT {', '.join(unique_select)}\n"
                 f"FROM db_GOKreasi.t_registerpengajar tr\n"
                 f"JOIN (SELECT DISTINCT max(Id) as Id\n"
                 f"FROM db_GOKreasi.t_registerpengajar tr2\n"
                 f"where tr2.cNIK is not null group by cNomorHP) sq on tr.Id = sq.Id")
    elif nama_table == 't_mapel_pilihan_siswa' :
        query = (f"SELECT DISTINCT \n"
                f"cNoRegister , cIdKelompokUjian \n"
                f"from db_GOKreasi.t_mapelpilihan tm ")
    elif nama_table == 't_orangtua_siswa_new_fix' :
        query = (f"SELECT ROW_NUMBER() OVER () + 230000000000 AS c_id_ortu,\n"
                f"tcst.c_email, tcst.c_telp, NULL, NULL, 'aktif',\n"
                f"tcs.c_lastupdate, '', CURRENT_TIMESTAMP(), NULL\n"
                f"FROM db_GOIconsV2.t_Cluster_Siswa tcs\n"
                f"JOIN (SELECT c_NoRegistrasi, JSON_UNQUOTE(c_InfoKontak->'$.HP2') AS c_telp,JSON_UNQUOTE(c_InfoKontak->'$.EMAIL2') AS c_email\n"
                f"FROM db_GOIconsV2.t_Cluster_Siswa) tcst ON tcst.c_NoRegistrasi = tcs.c_NoRegistrasi\n"
                f"WHERE tcst.c_telp NOT IN ('', '08')\n"
                f"AND tcst.c_telp NOT LIKE '%+%'\n"
                f"AND LENGTH(tcst.c_telp) >= 10\n"
                f"and tcs.c_tahunajaran = '2023/2024';")
    elif nama_table == 't_produk_aktif' :
        query = (f"SELECT DISTINCT \n"
                f"tp.c_NoRegistrasi , tp.c_IdKomponentProduk , tp.c_Status , tp.c_TanggalAwal , tp.c_TanggalAkhir \n"
                f"from db_GOKreasi.t_produkdibeli tp\n"
                "join db_GOIconsV2.t_Cluster_Siswa tcs on tcs.c_NoRegistrasi = tp.c_NoRegistrasi\n"
                "LEFT JOIN db_GOKreasi.t_register tr  on tr.cNoRegister = tcs.c_NoRegistrasi\n"
                "where tcs.c_TahunAjaran = '2023/2024' \n")    
    elif nama_table == 't_produk_siswa' : 
        unique_select = ['tcs.c_IdPembelian','tcs.c_NoRegistrasi','tcs.c_TanggalDaftar','tcs.c_IdKelas','tcs.c_TahunAjaran','tcs.c_IdDikDasMen','tcs.c_NamaLengkap','c_IdGedung','c_IdKomar','c_IdPenanda','c_IdSekolah','c_IdSekolahKelas','c_TingkatSekolahKelas','c_IdJenisKelas','c_KapasitasMax','c_StatusBayar','c_IdBundling','c_KerjaSama','c_LastUpdate']
        query = (f"SELECT DISTINCT {', '.join(unique_select)} from db_GOIconsV2.t_Cluster_Siswa tcs \n"    
                f"WHERE tcs.c_TahunAjaran  = '2023/2024'")
    elif nama_table == 't_siswa' : 
        unique_select = ['tcs.c_NoRegistrasi', 'tcs.c_NamaLengkap', "JSON_EXTRACT(tcs.c_InfoKontak, '$.EMAIL') AS email", "JSON_EXTRACT(tcs.c_InfoKontak, '$.HP') AS no_hp", 'NULL AS c_id_device', 'NULL AS c_id_login', "'aktif' AS status", 'current_timestamp', "'' AS c_password", 'current_timestamp','NULL AS c_is_last_login']
        query = (f"SELECT DISTINCT  {', '.join(unique_select)} \n"
                f"FROM db_GOIconsV2.t_Cluster_Siswa tcs\n"
                f"LEFT JOIN db_GOKreasi.t_register tr  on tr.cNoRegister = tcs.c_NoRegistrasi \n"
                f"WHERE  c_TahunAjaran  = '2023/2024'")
    elif nama_table == 't_siswa_detail' :
        query = (f"SELECT DISTINCT tb.* \n"
                f"from db_GOIconsV2.t_Biodata tb \n"
                f"join db_GOIconsV2.t_Cluster_Siswa tcs on tb.c_NoRegistrasi = tcs.c_NoRegistrasi \n"
                f"where tcs.c_TahunAjaran  = '2023/2024'")
    return query



