def nama_table(database_name):
    table_names = {
        'db_go': ['t_berita', 't_bidang_go', 't_carousel', 't_gedung', 't_gokomar', 't_kota', 't_outlet'],
        'db_kbm': ['t_bah', 't_bah_kelas', 't_cluster_pengajar', 't_daftar_kegiatan_kbm','t_feedback_pengajaran', 't_feedback_pengajaran_lembaga', 't_isi_bah', 't_kelas', 
                   't_kelas_siswa', 't_kelas_siswa_lembaga', 't_permintaan_tst', 't_realisasi_kelas', 't_realisasi_kerja', 't_realisasi_kerja_kbm', 
                   't_rencana_kerja', 't_rencana_kerja_kbm', 't_feedback_question'],
        'db_materi' : ['t_bab','t_buku','t_buku_produk','t_bundel_soal','t_isi_buku','t_isi_bundel_soal','t_mapel_bab','t_paket_dan_bundel_materi',
                       't_soal','t_soal_bab','t_soal_video_soal','t_teori_bab','t_teori_bab_video','t_video_soal','t_video_teori','t_wacana',
                       't_wacana_soal'],
        'db_materi_teaser': ['t_bab_teaser','t_buku_produk_teaser','t_buku_teaser','t_bundel_soal_teaser','t_isi_buku_teaser',
                             't_isi_bundel_soal_teaser','t_mapel_bab_teaser','t_soal_bab_teaser','t_soal_teaser','t_soal_video_soal_teaser',
                             't_teori_bab_teaser','t_teori_bab_video_teaser','t_video_soal_teaser','t_video_teaser','t_video_teori_teaser',
                             't_wacana_soal_teaser','t_wacana_teaser'],
        'db_produk' : ['t_bundling', 't_isi_produk_mix', 't_isi_tob', 't_jenis_kelas', 't_jenis_produk', 't_paket_dan_bundel', 't_paket_soal',
                       't_produk', 't_produk_mix', 't_produk_tob', 't_tob'],
        'db_produk_teaser' : ['t_isi_tob_teaser', 't_jenis_kelas_teaser', 't_jenis_produk_teaser', 't_paket_dan_bundel_teaser', 't_paket_soal_teaser', 
                              't_produk_teaser', 't_produk_tob_teaser', 't_role_buku_teaser', 't_role_tob_teaser', 't_tob_teaser'],
        'db_ptn' : ['t_jurusan', 't_jurusan_deskripsi', 't_kelompok_jurusan', 't_perguruan_tinggi', 't_rumpun_jurusan'],
        'db_report_siswa_empati_mandiri' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                            't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                            't_hasil_jawaban_9', 't_jawaban_siswa', 't_peserta_to'],
        'db_report_siswa_empati_wajib' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                        't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                        't_hasil_jawaban_9',  't_jawaban_siswa', 't_peserta_to', 't_syarat_empati'],
        'db_report_siswa_goa' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to', 't_target_lulus_goa'],
        'db_report_siswa_irt' : ['t_hasil_irt', 't_irt_nilai_to', 't_nilai_irt_tobk'],
        'db_report_siswa_kuis' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_lateks' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_paket_intensif' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_pendalaman_materi' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_peringkat' : ['t_data_siswa', 't_pengerjaan_mata_uji', 't_peringkat_new', 't_peringkat_racing_new', 't_peringkat_rank', 't_rekap_nilai', 
                                       't_target_mapel', 't_target_pengerjaan_siswa'],
        'db_report_siswa_presensi' : [],
        'db_report_siswa_racing' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_soref' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_tobk' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_vak' : ['t_detailvak','t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to', 't_vak'],
        'db_report_siswa_koding' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_report_tamu' : ['t_hasil_jawaban_tamu', 't_tamu_register'],
        'db_sekolah' : ['t_kelompok_ujian', 't_kurikulum', 't_list_mapel_pilihan', 't_mapel_kelompok_ujian', 't_mata_pelajaran', 't_sekolah', 't_sekolah_kelas', 
                        't_sekolah_kelas_kelompok_ujian', 't_sekolah_siswa', 't_sekolah_siswa_lembaga', 't_semester', 't_tahun_ajaran'],
        'db_user' : ['t_bookmark', 't_log_aktivitas', 't_mapel_pilihan_siswa', 't_orangtua', 't_orangtua_siswa', 't_pembayaran', 't_pilihan_ptn_siswa', 't_produk_aktif', 
                     't_produk_siswa', 't_siswa', 't_siswa_detail', 't_siswa_tata_tertib', 't_tata_tertib'],
        'db_user_lembaga' : ['t_mapel_pilihan_siswa_lembaga', 't_orangtua_lembaga', 't_pilihan_ptn_siswa_lembaga', 't_produk_aktif_lembaga', 't_produk_lembaga', 't_user_lembaga', 't_user_lembaga_detail'],
        'db_user_tamu' : ['t_tamu']
    }
    return table_names.get(database_name, [])

def jenis_table(nama_database, nama_table):
    master_tables = {
        'db_go': ['t_berita', 't_bidang_go', 't_carousel', 't_daftar_kegiatan', 't_gedung', 't_gokomar', 't_kota', 't_outlet', 't_daftar_kegiatan_kbm'],
        'db_kbm': ['t_bah', 't_cluster_pengajar', 't_daftar_kegiatan_kbm','t_feedback_pengajaran', 't_feedback_pengajaran_lembaga', 't_kelas', 
                    't_permintaan_tst',  't_realisasi_kerja', 't_realisasi_kerja_kbm', 't_rencana_kerja', 't_rencana_kerja_kbm', 't_feedback_question'],
        'db_materi': ['t_bab','t_buku','t_bundel_soal','t_soal','t_teori_bab','t_video_soal','t_video_teori','t_wacana'],
        'db_materi_teaser': ['t_bab_teaser','t_buku_teaser','t_bundel_soal_teaser', 't_soal_teaser','t_teori_bab_teaser','t_video_soal_teaser',
                             't_video_teaser','t_video_teori_teaser', 't_wacana_teaser'],
        'db_produk' : ['t_bundling', 't_jenis_kelas', 't_jenis_produk',  't_paket_soal','t_produk', 't_produk_mix', 't_tob'],
        'db_produk_teaser' : ['t_jenis_kelas_teaser', 't_jenis_produk_teaser', 't_paket_soal_teaser', 't_produk_teaser',
                              't_role_buku_teaser', 't_role_tob_teaser', 't_tob_teaser'],
        'db_ptn' : ['t_jurusan', 't_jurusan_deskripsi', 't_kelompok_jurusan', 't_perguruan_tinggi', 't_rumpun_jurusan'],
        'db_report_siswa_empati_mandiri' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                            't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                            't_hasil_jawaban_9', 't_jawaban_siswa', 't_peserta_to'],
        'db_report_siswa_empati_wajib' : ['t_hasil_empati_1','t_hasil_empati_10','t_hasil_empati_11','t_hasil_empati_12','t_hasil_empati_13','t_hasil_empati_2','t_hasil_empati_3',
                                        't_hasil_empati_4','t_hasil_empati_5','t_hasil_empati_6','t_hasil_empati_7','t_hasil_empati_8','t_hasil_empati_9','t_hasil_jawaban_1',
                                        't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2','t_hasil_jawaban_3', 
                                        't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8','t_hasil_jawaban_9', 
                                        't_jawaban_siswa', 't_peserta_to', 't_syarat_empati'],
        'db_report_siswa_goa' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_irt' : ['t_hasil_irt', 't_irt_nilai_to', 't_nilai_irt_tobk'],
        'db_report_siswa_kuis' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_lateks' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_paket_intensif' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_pendalaman_materi' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_peringkat' : ['t_data_siswa', 't_pengerjaan_mata_uji', 't_peringkat_new', 't_peringkat_racing_new', 't_peringkat_rank', 't_rekap_nilai', 
                                       't_target_mapel', 't_target_pengerjaan_siswa'],
        'db_report_siswa_presensi' : [],
        'db_report_siswa_racing' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_soref' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_tobk' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_siswa_vak' : ['t_detailvak','t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to', 't_vak'],
        'db_report_siswa_koding' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                't_hasil_jawaban_9', 't_jawaban_siswa','t_peserta_to'],
        'db_report_report_tamu' : ['t_hasil_jawaban_tamu', 't_tamu_register'],
        'db_sekolah' : ['t_kelompok_ujian', 't_kurikulum', 't_mata_pelajaran', 't_sekolah', 't_sekolah_kelas', 't_semester', 't_tahun_ajaran'],
        'db_user' : ['t_bookmark', 't_log_aktivitas','t_orangtua','t_pembayaran','t_siswa', 't_siswa_detail','t_tata_tertib'],
        'db_user_lembaga' : ['t_orangtua_lembaga','t_user_lembaga','t_user_lembaga_detail'],
        'db_user_tamu' : ['t_tamu']
    }
    penghubung_tables = {
        'db_kbm': ['t_isi_bah', 't_bah_kelas', 't_kelas_siswa', 't_kelas_siswa_lembaga', 't_realisasi_kelas'],
        'db_materi': ['t_buku_produk','t_isi_buku','t_isi_bundel_soal','t_mapel_bab','t_paket_dan_bundel_materi', 't_soal_bab','t_soal_video_soal',
                      't_teori_bab_video',  't_wacana_soal'],
        'db_materi_teaser' : ['t_buku_produk_teaser','t_isi_buku_teaser', 't_isi_bundel_soal_teaser','t_mapel_bab_teaser','t_soal_bab_teaser','t_soal_video_soal_teaser',
                              't_teori_bab_video_teaser','t_wacana_soal_teaser'],
        'db_produk' : [ 't_isi_produk_mix', 't_isi_tob','t_paket_dan_bundel', 't_produk_tob'],
        'db_produk_teaser' : ['t_isi_tob_teaser','t_paket_dan_bundel_teaser','t_produk_tob_teaser'],
        'db_ptn' : [],
        'db_report_siswa_empati_mandiri' : [],
        'db_report_siswa_empati_wajib' : [],
        'db_report_siswa_goa' : ['t_target_lulus_goa'],
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
        'db_sekolah' : ['t_list_mapel_pilihan', 't_mapel_kelompok_ujian','t_sekolah_siswa', 't_sekolah_siswa_lembaga'],
        'db_user' : ['t_mapel_pilihan_siswa','t_orangtua_siswa','t_pilihan_ptn_siswa', 't_produk_aktif', 't_produk_siswa','t_siswa_tata_tertib'],
        'db_user_lembaga' : ['t_mapel_pilihan_siswa_lembaga','t_pilihan_ptn_siswa_lembaga','t_produk_aktif_lembaga','t_produk_lembaga'],
        'db_user_tamu' : []
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
        't_daftar_kegiatan_kbm' : 'c_id_kegiatan',
        't_isi_bah': 'c_id',
        #db_materi
        't_bab' : 'c_kode_bab',
        't_buku' : 'c_id_buku',
        't_buku_produk' : 'c_id_buku_produk',
        't_bundel_soal' : 'c_id_bundel',
        #db_report_siswa_goa
        't_target_lulus_goa' : 'c_id_target_lulus',
        
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
        't_bah' : ['c_id_bah', 'c_kode_bah', 'c_semester', 'c_tahun_ajaran', 'c_id_tingkat_kelas', 'c_id_kurikulum', 
                  'c_id_jenis_layanan', 'c_id_kelompok_ujian', 'c_jumlah_pertemuan', 'c_id_silabus', 'c_updater', 'c_last_update'],
        't_daftar_kegiatan_kbm' : ['c_id_kegiatan','c_nama_kegiatan','c_deskripsi_siswa','c_deskripsi_petugas','c_deskripsi_pengajar',
                                   'c_kr','c_pf','c_ph','c_pk','c_pengali','c_is_relatif','c_pengali_sd','c_waktu_maksimal',
                                   'c_waktu_minimal','c_id_jenis_petugas','c_dasar_pengajian','c_updater','c_created_at','c_last_update'],
        't_isi_bah': ['c_id', 'c_id_bah', 'c_kode_bab', 'c_pertemuan', 'c_updater', 'c_last_update'],
        #db_materi :
        't_bab' : ['c_kode_bab','c_nama_bab','c_upline','c_peluang','c_status','c_updater','c_created_at','c_last_update'],
        't_buku' : ['c_id_buku','c_nama_buku','c_deskripsi','c_semester','c_id_sekolah_kelas','c_id_kurikulum','c_tahun_ajaran',
                    'c_jenis_buku','c_id_kelompok_ujian','c_updater','c_created_at','c_last_update'],
        't_buku_produk' : ['c_id_buku','c_id_produk','c_updater','c_last_update'],
        't_bundel_soal' : ['c_id_bundel','c_kode_bundel','c_deskripsi','c_waktu_pengerjaan','c_tahun_ajaran','c_jumlah_soal',
                           'c_peruntukan','c_id_sekolah_kelas','c_id_kelompok_ujian','c_opsi_urut','c_status','c_updater',
                           'c_created_at','c_last_update'],
        #db_report_siswa_goa
        't_target_lulus_goa' : ['c_id_tingkat_kelas','c_tahun_ajaran','c_id_kelompok_ujian','c_minimal_benar','c_updater','c_created_at',
                                'c_last_update',]
    }

    return kolom_tables.get(nama_table, [])

def foreign_key(nama_table):
    foreign_keys = {
        #db_go
        't_gokomar': ['c_id_kota'],
        #db_kbm
        't_isi_bah': ['c_id_bah'],
        #db_materi
        't_bab' : ['c_id_buku'],
        't_bundel_soal' : [],
        #db_report_siswa_goa
        't_target_lulus_goa' : [],
    }

    foreign_tables = {
        #db_go
        't_gokomar': ['t_kota'],
        #db_kbm
        't_daftar_kegiatan_kbm' : [],
        't_isi_bah': ['t_bah'],
        #db_materi 
        't_bab' : ['t_buku'],
        't_bundel_soal' :[],
        #db_report_siswa_goa
        't_target_lulus_goa' : [],
    }

    return foreign_keys.get(nama_table, []), foreign_tables.get(nama_table, [])

def unique_key(nama_table):
    unique_keys = {
        #db_go
        #db_kbm
        't_daftar_kegiatan_kbm' : [],
        't_isi_bah': [['c_id_bah', 'c_kode_bab']],
        #db_materi
        't_bab': [],
        't_buku' : [],
        't_buku_produk' : [['c_id_buku', 'c_id_produk']],
        't_bundelsoal' : [],
        #db_report_siswa_goa
        't_target_lulus_goa' : [['c_id_tingkat_kelas','c_tahun_ajaran','c_id_kelompok_ujian']],
    }

    return unique_keys.get(nama_table, [])