def nama_table(database_name):
    table_names = {
        'db_go': ['t_berita', 't_bidang_go', 't_carousel', 't_daftar_kegiatan', 't_gedung', 't_gokomar', 't_kota', 't_outlet', 't_daftar_kegiatan_kbm'],
        'db_kbm': ['t_bah', 't_bah_kelas', 't_cluster_pengajar', 't_feedback_pengajaran', 't_feedback_pengajaran_lembaga', 't_isi_bah', 't_kelas', 't_kelas_siswa', 't_kelas_siswa_lembaga', 't_permintaan_tst', 't_realisasi_kelas', 't_realisasi_kerja', 't_realisasi_kerja_kbm', 't_rencana_kerja', 't_rencana_kerja_kbm', 't_feedback_question']
    }
    
    return table_names.get(database_name, [])

def jenis_table(nama_database, nama_table) :
    if nama_database == 'db_go' : 
        master = ['t_berita', 't_bidang_go', 't_carousel', 't_daftar_kegiatan', 't_gedung', 't_gokomar', 't_kota', 't_outlet', 't_daftar_kegiatan_kbm']
        if nama_table in master :
            jenis_table = 'm'
            
    elif nama_database == 'db_kbm' :
        master = ['t_bah']
        penghubung = ['t_isi_bah']
        if nama_table in master :
            jenis_table = 'm'
        elif nama_table in penghubung : 
            jenis_table = 'p'
    
    if jenis_table == 'm' :
        jenis_table = 'master'
    else : 
        jenis_table = 'penghubung' 
    return jenis_table 

def primary_key(nama_table) :
    # db_go
    if nama_table == 't_berita' : 
        primary_key = 'c_id_berita'
    elif nama_table == 't_gokomar' :
        primary_key = 'c_id_komar'
        
    # db_kbm
    elif nama_table == 't_bah' :
        primary_key = 'c_id_bah'
    elif nama_table == 't_isi_bah' :
        primary_key = 'c_id'
    return primary_key

def kolom_table(nama_table) :
    # db_go
    if nama_table == 't_berita' : 
        kolom_table = ['c_id_berita','c_tanggal_terbit','c_tanggal_berakhir','c_judul','c_deskripsi','c_url', 'c_updater',
                       'c_status','c_untuk','c_jenis','c_photo','c_jumlah_viewer','c_last_update','c_created_at']
    elif nama_table == 't_gokomar' :
        kolom_table = ['c_id_komar','c_nama_komar','c_id_kewilayahan','c_upline','c_id_kota','c_status','c_updater','c_last_update']
    
    # db_kbm
    elif nama_table == 't_bah' :
        kolom_table = ['c_id_bah','c_kode_bah','c_semester','c_tahun_ajaran','c_id_tingkat_kelas','c_id_kurikulum','c_id_jenis_layanan',
                       'c_id_kelompok_ujian','c_jumlah_pertemuan','c_id_silabus','c_updater','c_last_update']
    elif nama_table == 't_isi_bah' : 
        kolom_table = ['c_id','c_id_bah','c_kode_bab','c_pertemuan','c_updater','c_last_update']
    return kolom_table

def foreign_key(nama_table) :
    # db_go
    if nama_table == 't_gokomar' :
        foreign_key = ['c_id_kota']
        foreign_table = ['t_kota']

    # db_kbm 
    elif nama_table == 't_isi_bah' :
        foreign_key = ['c_id_bah']
        foreign_table = ['t_bah']
    
    else : foreign_key = foreign_table = []
    return foreign_key, foreign_table

def unique_key(nama_table) :
    # db_kbm
    if nama_table == 't_isi_bah' :
        unique_key = ['c_id_bah', 'c_kode_bab']
        
    else : unique_key = []
    return unique_key   