def nama_table(database_name):
    table_names = {
        'db_go': ['t_berita', 't_bidang_go', 't_carousel', 't_daftar_kegiatan', 't_gedung', 't_gokomar', 't_kota', 't_outlet', 't_daftar_kegiatan_kbm'],
        'db_kbm': ['t_bah', 't_bah_kelas', 't_cluster_pengajar', 't_feedback_pengajaran', 't_feedback_pengajaran_lembaga', 't_isi_bah', 't_kelas', 
                   't_kelas_siswa', 't_kelas_siswa_lembaga', 't_permintaan_tst', 't_realisasi_kelas', 't_realisasi_kerja', 't_realisasi_kerja_kbm', 
                   't_rencana_kerja', 't_rencana_kerja_kbm', 't_feedback_question'],
        'db_materi' : ['t_bab','t_buku','t_buku_produk','t_bundel_soal','t_isi_buku','t_isi_bundel_soal','t_mapel_bab','t_paket_dan_bundel_materi',
                       't_soal','t_soal_bab','t_soal_video_soal','t_teori_bab','t_teori_bab_video','t_video_soal','t_video_teori','t_wacana',
                       't_wacana_soal'],
        'db_materi_teaser': ['t_bab_teaser','t_buku_produk_teaser','t_buku_teaser','t_bundel_soal_teaser','t_isi_buku_teaser',
                             't_isi_bundel_soal_teaser','t_mapel_bab_teaser','t_soal_bab_teaser','t_soal_teaser','t_soal_video_soal_teaser',
                             't_teori_bab_teaser','t_teori_bab_video_teaser','t_video_soal_teaser','t_video_teaser','t_video_teori_teaser',
                             't_wacana_soal_teaser','t_wacana_teaser'],
        'db_produk' : [],
        'db_produk_teaser' : [],
        'db_ptn' : [],
        'db_report_siswa_empati_mandiri' : [],
        'db_report_siswa_empati_wajib' : [],
        'db_report_siswa_goa' : [],
        'db_report_siswa_irt' : [],
        'db_report_siswa_kuis' : [],
        'db_report_siswa_lateks' : [],
        'db_report_siswa_paket_intensif' : [],
        'db_report_siswa_pendalaman_materi' : [],
        'db_report_siswa_peringkat' : [],
        'db_report_siswa_presensi' : [],
        'db_report_siswa_racing' : [],
        'db_report_siswa_soref' : [],
        'db_report_siswa_tobk' : [],
        'db_report_siswa_vak' : [],
        'db_report_siswa_koding' : [],
        'db_report_report_tamu' : [],
        'db_sekolah' : [],
        'db_user' : [],
        'db_user_lembaga' : [],
        'db_user_tamu' : []
    }
    return table_names.get(database_name, [])

def jenis_table(nama_database, nama_table):
    master_tables = {
        'db_go': ['t_berita', 't_bidang_go', 't_carousel', 't_daftar_kegiatan', 't_gedung', 't_gokomar', 't_kota', 't_outlet', 't_daftar_kegiatan_kbm'],
        'db_kbm': ['t_bah'],
    }
    penghubung_tables = {
        'db_kbm': ['t_isi_bah'],
    }

    if nama_table in master_tables.get(nama_database, []):
        jenis_table = 'master'
    elif nama_table in penghubung_tables.get(nama_database, []):
        jenis_table = 'penghubung'
    else:
        jenis_table = None

    return jenis_table

def primary_key(nama_table):
    primary_keys = {
        # db_go
        't_berita': 'c_id_berita',
        't_gokomar': 'c_id_komar',
        # db_kbm
        't_bah': 'c_id_bah',
        't_isi_bah': 'c_id',
    }

    return primary_keys.get(nama_table, None)
def kolom_table(nama_table):
    kolom_tables = {
        # db_go
        't_berita': ['c_id_berita', 'c_tanggal_terbit', 'c_tanggal_berakhir', 'c_judul', 'c_deskripsi', 'c_url', 'c_updater','c_status', 
                     'c_untuk', 'c_jenis', 'c_photo', 'c_jumlah_viewer', 'c_last_update', 'c_created_at'],
        't_gokomar': ['c_id_komar', 'c_nama_komar', 'c_id_kewilayahan', 'c_upline', 'c_id_kota', 'c_status', 'c_updater',
                      'c_last_update'],
        #db_kbm
        't_bah': ['c_id_bah', 'c_kode_bah', 'c_semester', 'c_tahun_ajaran', 'c_id_tingkat_kelas', 'c_id_kurikulum', 
                  'c_id_jenis_layanan', 'c_id_kelompok_ujian', 'c_jumlah_pertemuan', 'c_id_silabus', 'c_updater', 'c_last_update'],
        't_isi_bah': ['c_id', 'c_id_bah', 'c_kode_bab', 'c_pertemuan', 'c_updater', 'c_last_update'],
    }

    return kolom_tables.get(nama_table, [])

def foreign_key(nama_table):
    foreign_keys = {
        #db_go
        't_gokomar': ['c_id_kota'],
        #db_kbm
        't_isi_bah': ['c_id_bah'],
    }

    foreign_tables = {
        #db_go
        't_gokomar': ['t_kota'],
        #db_kbm
        't_isi_bah': ['t_bah'],
    }

    return foreign_keys.get(nama_table, []), foreign_tables.get(nama_table, [])

def unique_key(nama_table):
    unique_keys = {
        #db_kbm
        't_isi_bah': ['c_id_bah', 'c_kode_bab'],
    }

    return unique_keys.get(nama_table, [])