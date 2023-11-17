def nama_table(database_name):
    table_names = {
        'db_go': ['t_berita', 't_bidang_go', 't_carousel', 't_gedung', 't_gokomar', 't_kota', 't_outlet'],
        'db_kbm': ['t_bah', 't_bah_kelas', 't_cluster_pengajar', 't_daftar_kegiatan_kbm','t_feedback_pengajaran', 't_feedback_pengajaran_lembaga', 't_isi_bah', 't_kelas', 
                   't_kelas_siswa', 't_kelas_siswa_lembaga', 't_permintaan_tst', 't_presensi_siswa','t_realisasi_kelas', 't_realisasi_kerja', 't_realisasi_kerja_kbm', 
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
        'db_pt' : ['t_jurusan', 't_jurusan_deskripsi', 't_kelompok_jurusan', 't_perguruan_tinggi', 't_rumpun_jurusan'],
        'db_report_siswa_empati_mandiri' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                            't_hasil_jawaban_3', 't_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
                                            't_hasil_jawaban_9', 't_jawaban_siswa', 't_peserta_to'],
        'db_report_siswa_empati_wajib' : ['t_hasil_empati_12','t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
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
        'db_report_siswa_peringkat' : ['t_data_siswa','t_jumlah_target', 't_pengerjaan_mata_uji', 't_peringkat_new', 't_peringkat_racing_new', 't_peringkat_rank', 't_rekap_nilai', 
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
        'db_kbm': ['t_bah', 't_cluster_pengajar', 't_daftar_kegiatan_kbm', 't_feedback_pengajaran_lembaga', 't_kelas', 
                    't_permintaan_tst',  't_realisasi_kerja', 't_realisasi_kerja_kbm', 't_rencana_kerja', 't_rencana_kerja_kbm', 't_feedback_question'],
        'db_materi': ['t_bab','t_buku','t_bundel_soal','t_soal','t_teori_bab','t_video_soal','t_video_teori','t_wacana'],
        'db_materi_teaser': ['t_bab_teaser','t_buku_teaser','t_bundel_soal_teaser', 't_soal_teaser','t_teori_bab_teaser','t_video_soal_teaser',
                             't_video_teaser','t_video_teori_teaser', 't_wacana_teaser'],
        'db_produk' : ['t_bundling', 't_jenis_kelas', 't_jenis_produk',  't_paket_soal','t_produk', 't_produk_mix', 't_tob'],
        'db_produk_teaser' : ['t_jenis_kelas_teaser', 't_jenis_produk_teaser', 't_paket_soal_teaser', 't_produk_teaser',
                              't_role_buku_teaser', 't_role_tob_teaser', 't_tob_teaser'],
        'db_pt' : ['t_jurusan', 't_jurusan_deskripsi', 't_kelompok_jurusan', 't_perguruan_tinggi', 't_rumpun_jurusan'],
        'db_report_siswa_empati_mandiri' : ['t_hasil_jawaban_1', 't_hasil_jawaban_10', 't_hasil_jawaban_11', 't_hasil_jawaban_12', 't_hasil_jawaban_13', 't_hasil_jawaban_2',
                                             't_hasil_jawaban_3','t_hasil_jawaban_4', 't_hasil_jawaban_5', 't_hasil_jawaban_6', 't_hasil_jawaban_7', 't_hasil_jawaban_8',
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
        'db_report_siswa_peringkat' : ['t_data_siswa', 't_peringkat_new', 't_peringkat_racing_new', 't_peringkat_rank', 't_rekap_nilai'],
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
        'db_kbm': ['t_isi_bah', 't_bah_kelas','t_feedback_pengajaran', 't_kelas_siswa', 't_kelas_siswa_lembaga', 't_presensi_siswa','t_realisasi_kelas'],
        'db_materi': ['t_buku_produk','t_isi_buku','t_isi_bundel_soal','t_mapel_bab','t_paket_dan_bundel_materi', 't_soal_bab','t_soal_video_soal',
                      't_teori_bab_video',  't_wacana_soal'],
        'db_materi_teaser' : ['t_buku_produk_teaser','t_isi_buku_teaser', 't_isi_bundel_soal_teaser','t_mapel_bab_teaser','t_soal_bab_teaser','t_soal_video_soal_teaser',
                              't_teori_bab_video_teaser','t_wacana_soal_teaser'],
        'db_produk' : [ 't_isi_produk_mix', 't_isi_tob','t_paket_dan_bundel', 't_produk_tob'],
        'db_produk_teaser' : ['t_isi_tob_teaser','t_paket_dan_bundel_teaser','t_produk_tob_teaser'],
        'db_pt' : [],
        'db_report_siswa_empati_mandiri' : [],
        'db_report_siswa_empati_wajib' : ['t_hasil_empati_12'],
        'db_report_siswa_goa' : ['t_target_lulus_goa'],
        'db_report_siswa_irt' : [],
        'db_report_siswa_kuis' : [],
        'db_report_siswa_lateks' : [],
        'db_report_siswa_paket_intensif' : [],
        'db_report_siswa_pendalaman_materi' : [],
        'db_report_siswa_peringkat' : ['t_pengerjaan_mata_uji','t_jumlah_target', 't_target_pengerjaan_siswa', 't_target_mapel'],
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
        't_bidang_go' : 'c_id_bidang',
        't_gedung' : 'c_id_gedung',
        't_gokomar': 'c_id_komar',
        't_kota' : 'c_id_kota',
        # db_kbm
        't_bah': 'c_id_bah',
        't_bah_kelas' : 'c_id',
        't_cluster_pengajar' : 'c_id_pengajar',
        't_daftar_kegiatan_kbm' : 'c_id_kegiatan',
        't_feedback_pengajaran' : 'c_id',
        't_kelas' : 'c_id_kelas',
        't_kelas_siswa' : 'c_id',
        't_isi_bah': 'c_id',
        't_permintaan_tst' : 'c_id_permintaan',
        't_presensi_siswa' : 'c_id',
        't_rencana_kerja' : 'c_id_rencana',
        't_rencana_kerja_kbm' : 'c_id_rencana',
        #db_materi
        't_bab' : 'c_kode_bab',
        't_buku' : 'c_id_buku',
        't_buku_produk' : 'c_id',
        't_bundel_soal' : 'c_id_bundel',
        't_isi_buku' : 'c_id',
        't_isi_bundel_soal' : 'c_id',
        't_mapel_bab' : 'c_id',
        't_paket_dan_bundel_materi' : 'c_id',
        't_teori_bab' : 'c_id_teori_bab',
        't_teori_bab_video' : 'c_id',
        't_soal' : 'c_id_soal',
        't_soal_bab' : 'c_id',
        't_soal_video_soal' : 'c_id',
        't_video_soal' : 'c_id_video',
        't_video_teori' : 'c_id_video',
        't_wacana' : 'c_id_wacana',
        't_wacana_soal' : 'c_id',
        #db_produk
        't_bundling' : 'c_id_bundling',
        't_isi_produk_mix' : 'c_id',
        't_isi_tob' : 'c_id',
        't_jenis_kelas' : 'c_id_jenis_kelas',
        't_jenis_produk' : 'c_id_jenis_produk',
        't_paket_soal' : 'c_kode_paket',
        't_paket_dan_bundel' : 'c_id',
        't_produk' : 'c_id_produk',
        't_produk_mix' : 'c_id_produk_mix',
        't_produk_tob' : 'c_id',
        't_tob' : 'c_kode_tob',
        #db_pt
        't_jurusan' : 'c_id_jurusan',
        't_jurusan_deskripsi' : 'c_id_jurusan',
        't_kelompok_jurusan' : 'c_kode_kelompok_jurusan',
        't_perguruan_tinggi' : 'c_id_perguruan_tinggi',
        't_rumpun_jurusan' : 'c_kode_rumpun_jurusan',
        
        
        't_hasil_jawaban_3' :  'c_id',
        't_hasil_jawaban_4' : 'c_id',
        't_hasil_jawaban_5' : 'c_id',
        't_hasil_jawaban_6' : 'c_id',
        't_hasil_jawaban_7' : 'c_id',
        't_hasil_jawaban_8' : 'c_id',
        't_hasil_jawaban_9' : 'c_id',
        't_hasil_jawaban_10' : 'c_id',
        't_hasil_jawaban_11' : 'c_id',
        't_hasil_jawaban_12' : 'c_id',
        't_hasil_jawaban_13' : 'c_id',
        't_peserta_to' : 'c_id',
        
        
        #db_report_siswa_empati_wajib
        't_hasil_empati_12' : 'c_id',
        #db_report_siswa_goa
        't_target_lulus_goa' : 'c_id_target_lulus',
        #db_report_siswa_peringkat :
        't_pengerjaan_mata_uji' :'c_id',
        't_peringkat_new' : 'c_id',
        't_jumlah_target' : 'c_id',
        't_target_pengerjaan_siswa' : 'c_id',
        't_target_mapel' : 'c_id',
        #db_sekolah 
        't_kelompok_ujian' : 'c_id_kelompok_ujian',
        't_kurikulum' : 'c_id_kurikulum',
        't_mapel_kelompok_ujian' : 'c_id',
        't_mata_pelajaran' : 'c_id_mata_pelajaran',
        't_sekolah' : 'c_id_sekolah',
        't_sekolah_kelas' : 'c_id_sekolah_kelas',
        't_sekolah_siswa' : 'c_id',
        't_semester' : 'c_id_semester',
        't_tahun_ajaran' :'c_tahun_ajaran',
        #db_user
        't_mapel_pilihan_siswa' : 'c_id',
        't_produk_aktif' : 'c_id',
        't_produk_siswa' : 'c_id',
        't_siswa' : 'c_no_register',
        't_siswa_detail' : 'c_id'
        
    }

    return primary_keys.get(nama_table, None)
def kolom_table(nama_table):
    kolom_tables = {
        # db_go
        't_berita': ['c_id_berita', 'c_tanggal_terbit', 'c_tanggal_berakhir', 'c_judul', 'c_deskripsi', 'c_url', 'c_updater','c_status', 
                     'c_untuk', 'c_jenis', 'c_photo', 'c_jumlah_viewer', 'c_last_update', 'c_created_at'],
        't_bidang_go' : ['c_id_bidang','c_nama_bidang','c_status','c_id_kewilayahan','c_upline','c_updater','c_created_at','c_last_update'],
        't_gedung' : ['c_id_gedung','c_id_komar','c_id_lurah','c_id_peruntukan','c_nama_gedung','c_alamat','c_rt','c_rw','c_kode_pos','c_telp_1','c_telp_2','c_geolokasi','c_luas_tanah','c_luas_bangunan_awal','c_luas_bangunan_sekarang','c_luas_bidang_datar','c_jumlah_lantai','c_luas_parkir','c_daya_listrik_awal','c_daya_listrik_sekarang','c_sumber_listrik','c_sumber_air','c_status','c_keterangan','c_updater','c_ip_vpn','c_key','c_last_update','c_zona_waktu'],
        't_gokomar': ['c_id_komar', 'c_nama_komar', 'c_id_kewilayahan', 'c_upline', 'c_id_kota', 'c_status', 'c_updater',
                      'c_last_update'],
        't_kota' : ['c_id_kota','c_kota','c_updater','c_created_at','c_last_update'],
        #db_kbm
        't_bah' : ['c_id_bah', 'c_kode_bah', 'c_semester', 'c_tahun_ajaran', 'c_id_tingkat_kelas', 'c_id_kurikulum', 
                  'c_id_jenis_layanan', 'c_id_kelompok_ujian', 'c_jumlah_pertemuan', 'c_id_silabus', 'c_updater', 'c_last_update'],
        't_bah_kelas' :['c_id_kelas','c_id_bah','c_updater','c_last_update'],
        't_cluster_pengajar' : ['c_id_biodata','c_id_pengajar','c_nik','c_nama_lengkap','c_inisial','c_tingkat_kelas','c_jumlah_kuota','c_status_pengajar','c_id_gedung','c_id_penanda','c_status','c_id_pelajaran_sd','c_id_pelajaran_smp','c_id_pelajaran_sma','c_grade_sd','c_grade_smp','c_grade_sma','c_grade_tst','c_grade_global','c_info_kontak'],
        't_daftar_kegiatan_kbm' : ['c_id_kegiatan','c_nama_kegiatan','c_deskripsi_siswa','c_deskripsi_petugas','c_deskripsi_pengajar',
                                   'c_kr','c_pf','c_ph','c_pk','c_pengali','c_is_relatif','c_pengali_sd','c_waktu_maksimal',
                                   'c_waktu_minimal','c_id_jenis_petugas','c_dasar_pengajian','c_updater','c_created_at','c_last_update','c_id_info_kegiatan'],
        't_feedback_pengajaran' : ['c_id_rencana','c_no_register','c_nis','c_n0','c_n1','c_n2','c_n3','c_n4','c_n5','c_last_update'],
        't_kelas' : ['c_id_kelas','c_id_sekolah_kelas','c_tahun_ajaran','c_nama_kelas','c_tanggal_start','c_tanggal_berakhir','c_status','c_updater','c_last_update','c_id_gedung','c_tanggal_status','c_tanggal_re','c_status_rptk','c_id_jenis_kelas'],
        't_kelas_siswa' : ['c_id_kelas','c_no_register','c_updater','c_last_update'],
        't_isi_bah': [ 'c_id_bah', 'c_kode_bab', 'c_pertemuan', 'c_updater', 'c_last_update'],
        't_permintaan_tst' : ['c_id_permintaan','c_tanggal_permintaan','c_jam_awal_tst','c_jam_akhir_tst','c_id_jenis_tst','c_tanggal_kegunaan','c_id_pelajaran','c_kegunaan','c_status','c_tanggal_acc','c_permintaan_dari','c_id_gedung','c_tahun_ajaran','c_nik_pengajar','c_id_rencana','c_updater','c_last_update'],
        't_presensi_siswa' : ['c_id_rencana','c_no_register','c_id_gedung','c_latitude','c_longitude','c_jarak','c_waktu','c_imei','c_tanggal','c_id_kelas','c_nama_kelas','c_sesi','c_last_update','c_id_kelas_siswa','c_flag_kelas','c_nik','c_nama_pengajar','c_jam_awal','c_jam_akhir','c_is_feedback'],
        't_rencana_kerja' : ['c_id_rencana','c_id_gedung','c_nik','c_jam_awal','c_jam_akhir','c_id_kegiatan','c_info_1','c_info_2','c_info_3','c_tahun_ajaran','c_keterangan','c_status_rencana','c_updater_rencana','c_last_update'],
        't_rencana_kerja_kbm' : ['c_id_rencana','c_id_gedung','c_nik','c_jam_awal','c_jam_akhir','c_id_kegiatan','c_info_1','c_info_2','c_info_3','c_tahun_ajaran','c_status_rencana','c_updater_rencana','c_last_update','c_rencana','c_realisasi','c_siswa_hadir'],
        #db_materi :
        't_bab' : ['c_kode_bab','c_nama_bab','c_upline','c_peluang','c_status','c_updater','c_created_at','c_last_update'],
        't_buku' : ['c_id_buku','c_nama_buku','c_deskripsi','c_semester','c_id_sekolah_kelas','c_id_kurikulum','c_tahun_ajaran',
                    'c_jenis_buku','c_id_kelompok_ujian','c_updater','c_created_at','c_last_update'],
        't_buku_produk' : ['c_id_buku','c_id_produk','c_updater','c_last_update'],
        't_teori_bab' : ['c_id_teori_bab','c_uraian','c_level','c_kelengkapan','c_kode_bab','c_updater','c_created_at','c_last_update'],
        't_teori_bab_video' : ['c_id_video','c_id_teori_bab','c_updater','c_insert','c_last_update'],
        't_bundel_soal' : ['c_id_bundel','c_kode_bundel','c_deskripsi','c_waktu_pengerjaan','c_tahun_ajaran','c_jumlah_soal',
                           'c_peruntukan','c_id_sekolah_kelas','c_id_kelompok_ujian','c_opsi_urut','c_status','c_updater',
                           'c_created_at','c_last_update'],
        't_isi_buku' : ['c_id_buku','c_kode_bab','c_updater','c_last_update'],
        't_isi_bundel_soal' : ['c_id_soal','c_id_bundel','c_nomor_soal','c_updater','c_last_update'],
        't_mapel_bab' : ['c_kode_bab','c_id_mata_pelajaran','c_updater','c_insert','c_last_update'],
        't_paket_dan_bundel_materi' : ['c_id_bundel','c_kode_paket','c_urutan','c_updater','c_last_update'],
        't_soal': ['c_id_soal','c_soal','c_level_kognitif','c_tingkat_kesulitan','c_tipe_soal','c_opsi','c_solusi','c_upline','c_the_king','c_metode_pengambilan','c_saran_penggunaan','c_waktu_pengerjaan_soal','c_id_sumber_detail','c_nik_pembuat','c_is_verifikasi','c_tanggal_verifikasi','c_nik_verifikasi','c_updater','c_tanggal_pembuatan','c_last_update'],
        't_soal_bab' : ['c_id_soal', 'c_kode_bab', 'c_updater', 'c_insert','c_last_update'],
        't_soal_video_soal' : ['c_id_video','c_id_soal','c_updater','c_insert','c_last_update'],
        't_video_soal' : ['c_id_video','c_judul_video','c_keyword','c_deskripsi','c_link_video','c_updater','c_created_at','c_last_update'],
        't_video_teori' : ['c_id_video','c_judul_video','c_deskripsi','c_link_video','c_kode_bab','c_level','c_kelengkapan',
                           'c_updater','c_created_at','c_last_update'],
        't_wacana' : ['c_id_wacana','c_judul_wacana','c_text','c_keyword','c_id_mata_pelajaran','c_updater','c_created_at','c_last_update'],
        't_wacana_soal': ['c_id_soal', 'c_id_wacana', 'c_updater', 'c_insert', 'c_last_update'],
        #db_produk
        't_bundling' : ['c_id_bundling','c_id_produk_mix','c_id_kota','c_id_jenis_kelas','c_id_sekolah_kelas','c_is_kerja_sama','c_is_online','c_nama_bundling','c_tanggal_awal','c_tanggal_akhir','c_deskripsi','c_harga_pt','c_harga_fasilitas','c_biaya_operasional','c_tahun_ajaran','c_jenis_biaya_operasion','c_margin','c_biaya_tercantum','c_harga_sebelum','c_harga_peneyesuaian','c_harga_total','c_status','c_updater','c_last_update','c_insert','c_id_pola','c_is_teaser','c_perpanjangan','c_is_jaminan_100'],
        't_isi_produk_mix' : ['c_id_produk_mix','c_id_produk','c_jumlah','c_index','c_updater','c_created_at','c_last_update'],
        't_isi_tob' : ['c_kode_tob','c_kode_paket','c_nomor_urut','c_is_wajib','c_updater','c_last_update'],
        't_jenis_kelas' : ['c_id_jenis_kelas','c_jenis_kelas','c_singkatan','c_kapasitas_maksimal','c_status','c_updater','c_last_update','c_luas'],
        't_jenis_produk' : ['c_id_jenis_produk','c_nama_jenis_produk','c_id_bidang_penanggung_jawab','c_id_bidang_penentu_biaya','c_is_ongkos_kirim','c_status','c_updater','c_created_at','c_last_update'],
        't_paket_dan_bundel' : ['c_id_bundel','c_kode_paket','c_urutan','c_updater','c_last_update'],
        't_paket_soal' : ['c_kode_paket','c_deskripsi_paket','c_tahun_ajaran','c_tanggal_awal','c_tanggal_akhir','c_id_jenis_produk','c_id_sekolah_kelas','c_is_blocking_time','c_is_random','c_status','c_updater','c_created_at','c_last_update'],
        't_produk' : ['c_id_produk','c_id_jenis_produk','c_id_kurikulum','c_id_sekolah_kelas','c_id_bidang_penanggung_jawab','c_id_jenis_kelas','c_nama_produk','c_keterangan','c_status','c_updater','c_last_update','c_created_at'],
        't_produk_mix' : ['c_id_produk_mix','c_nama_produk_mix','c_id_jenis_kelas','c_id_kurikulum','c_id_sekolah_kelas','c_is_kerjasama','c_is_jenis_pertemuan','c_jum_s1','c_jum_s2','c_jum_s3','c_is_jaminan','c_zona','c_kode_unik','c_status','c_updater','c_created_at','c_last_update'],
        't_produk_tob' : ['c_kode_tob','c_id_produk','c_updater','c_last_update'],
        't_tob' : ['c_kode_tob','c_nama_tob','c_menit_antar_soal','c_tanggal_awal','c_tanggal_kedaluwarsa','c_tahun_ajaran','c_jenis','c_to_merdeka','c_status','c_updater','c_created_at','c_last_update'],
        #db_pt
        't_jurusan' : ['c_id_jurusan','c_id_perguruan_tinggi','c_nama_jurusan','c_kode_kelompok_jurusan','c_kode_rumpun_jurusan','c_keterangan','c_status','c_pg','c_pgum','c_plum','c_lintas_jurusan','c_is_sbmptn','c_is_um','c_jenjang','c_is_snmptn','c_updater','c_created_at','c_last_update'],
        't_jurusan_deskripsi' : ['c_id_jurusan','c_deskripsi','c_lapangan_kerja'],
        't_kelompok_jurusan' : ['c_kode_kelompok_jurusan','c_deskripsi','c_upline','c_keterangan','c_status','c_updater','c_created_at','c_last_update'],
        't_perguruan_tinggi' : ['c_id_perguruan_tinggi','c_id_district','c_nama_perguruan_tinggi','c_akronim','c_jenis','c_is_internasional','c_status','c_updater','c_created_at','c_last_update'],
        't_rumpun_jurusan' : ['c_kode_rumpun_jurusan','c_deskripsi','c_upline','c_keterangan','c_status','c_updater','c_created_at','c_last_update'],
        
        
        
        # db_report_siswa_empati_mandiri
        't_hasil_jawaban_3' : ['c_id','c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_4' : ['c_id','c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_5' : ['c_id','c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],         
        't_hasil_jawaban_6' : ['c_id','c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_7' : ['c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_8' : ['c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_9' : ['c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_10' : ['c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_11' : ['c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],       
        't_hasil_jawaban_12' : ['c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_hasil_jawaban_13' : ['c_no_register', 'c_kode_paket', 'c_detil_jawaban', 'c_detil_hasil', 'c_last_update', 'c_tahun_ajaran', 'c_keterangan'],
        't_peserta_to' : ['c_no_register','c_kode_paket','c_tanggal_mengumpulkan','c_tanggal_mulai_to','c_tanggal_deadline_to','c_persetujuan','c_flag','c_merk','c_versi','c_versi_os','c_sudah_selesai','c_ok','c_created_at','c_last_update'],
        
        #db_report_siswa_empati_wajib
        't_hasil_empati_12' : ['c_no_register','c_kode_tob', 'c_kode_paket', 'c_jumlah_soal', 'c_jumlah_benar', 'c_jumlah_salah', 'c_is_boleh','c_nik_verif', 'c_created_at', 'c_last_update'],
        #db_report_siswa_goa
        't_target_lulus_goa' : ['c_id_tingkat_kelas','c_tahun_ajaran','c_id_kelompok_ujian','c_minimal_benar','c_updater','c_created_at',
                                'c_last_update'],
        #db_report_siswa_peringkat
        't_pengerjaan_mata_uji' : ['c_no_register','c_id_kelompok_ujian','c_tanggal','c_id_jenis_produk','c_jumlah_pengerjaan','c_jumlah__benar','c_last_update','c_created_at'],
        't_peringkat_new' : ['c_id', 'c_no_register', 'c_nama_lengkap', 'c_total', 'c_id_sekolah_kelas', 'c_id_kota', 'c_nama_kota', 'c_id_gedung', 'c_nama_gedung', 'c_tahun_ajaran', 'c_created_at', 'c_last_update', 'c_detil'],
        't_target_mapel' : ['c_id_sekolah_kelas','c_id_kelompok_ujian','c_semester','c_tahun_ajaran','c_persen','c_last_update','c_created_at'],
        't_target_pengerjaan_siswa' : ['c_id_sekolah_kelas','c_target_harian','c_total_target','c_last_update','c_created_at','c_no_register'],
        #db_sekolah
        't_kelompok_ujian' : ['c_id_kelompok_ujian','c_nama_kelompok_ujian','c_singkatan','c_upline','c_status','c_updater','c_created_at','c_last_update'],
        't_kurikulum' : ['c_id_kurikulum','c_nama_kurikulum','c_singkatan','c_tahun_terbit','c_tanggal_awal','c_tanggal_akhir','c_status','c_updater','c_created_at','c_last_update'],
        't_mapel_kelompok_ujian' : ['c_id_mata_pelajaran','c_id_kelompok_ujian','c_updater','c_last_update'],
        't_mata_pelajaran' : ['c_id_mata_pelajaran','c_nama_mata_pelajaran','c_singkatan','c_is_ada_utbk','c_status','c_updater','c_created_at','c_last_update'],
        't_sekolah' : ['c_id_sekolah','c_nama_sekolah','c_id_district','c_jenjang_pendidikan','c_alamat_sekolah','c_kode_sekolah_dapodik','c_status','c_updater','c_created_at','c_last_update'],
        't_sekolah_kelas' : ['c_id_sekolah_kelas','c_tingkat_kelas','c_jurusan','c_kelompok_sekolah','c_updater','c_status','c_created_at','c_last_update'],
        't_sekolah_siswa' : ['c_id_sekolah','c_no_register','c_updater','c_last_update'],
        't_semester' : ['c_id_semester','c_id_sekolah_kelas','c_semester','c_tahun_ajaran','c_awal','c_akhir'],
        't_tahun_ajaran' : ['c_tahun_ajaran','c_is_default','c_status','c_awal','c_akhir','c_updater','c_created_at','c_last_update'],
        #db_user
        't_mapel_pilihan_siswa' : ['c_no_register','c_id_kelompok_ujian'],
        't_produk_aktif' : ['c_no_register','c_id_produk', 'c_status','c_tanggal_awal','c_tanggal_akhir'],
        't_produk_siswa' : ['c_id_pembelian','c_no_register','c_tanggal_daftar','c_id_kelas','c_tahun_ajaran','c_id_dikdasken','c_nama_lengkap','c_id_gedung','c_id_komar','c_id_kota','c_id_sekolah','c_id_sekolah_kelas','c_tingkat_sekolah_kelas','c_id_jenis_kelas','c_kapasitas_max','c_status_bayar','c_id_bundling','c_kerjasama','c_last_update'],
        't_siswa' : ['c_no_register','c_nama_lengkap','c_email','c_nomor_hp','c_id_device','c_is_login','c_is_aktif','c_created_at','c_password','c_last_update_password','is_last_login'],
        't_siswa_detail' : ['c_id','c_no_register','c_nama_lengkap','c_nama_panggilan','c_jenis_kelamin','c_gol_darah','c_id_district','c_tgl_lahir','c_agama','c_nama_ibu_kandung','c_pekerjaan_ortu','c_id_lurah','c_alamat','c_no_tlp','c_no_tlp2','c_hp','c_hp2','c_email','c_email2','c_status_kepemilikan','c_hubungan','c_is_aktif','c_updater','c_insert','c_last_update','c_id_gedung','c_nisn']
    }

    return kolom_tables.get(nama_table, [])

def foreign_key(nama_table):
    foreign_keys = {
        #db_go+
        't_berita' : [],
        't_gokomar': ['c_id_kota'],
        #db_kbm
        't_bah_kelas' : ['c_id_kelas', 'c_id_bah'],
        't_feedback_pengajaran' : ['c_id_rencana'],
        't_isi_bah': ['c_id_bah'],
        't_kelas_siswa' : ['c_id_kelas'],
        't_presensi_siswa' : ['c_id_rencana', 'c_id_kelas'],
        't_rencana_kerja_kbm' : ['c_id_kegiatan'],
        #db_materi
        't_buku_produk' : ['c_id_buku'],
        't_isi_buku' : ['c_id_buku', 'c_kode_bab'],
        't_isi_bundel_soal' : ['c_id_soal', 'c_id_bundel'],
        't_mapel_bab' : ['c_kode_bab'],
        't_paket_dan_bundel_materi' : ['c_id_bundel'],
        't_soal_bab' : ['c_id_soal','c_kode_bab'],
        't_soal_video_soal' : ['c_id_soal','c_id_video'],
        't_teori_bab' : ['c_kode_bab'],
        't_teori_bab_video' : ['c_id_teori_bab', 'c_id_video'],
        't_video_soal' : [],
        't_video_teori' : ['c_kode_bab'],
        't_wacana' : [],
        't_wacana_soal' :['c_id_soal','c_id_wacana'],
        #db_produk
        't_bundling' : ['c_id_jenis_kelas', 'c_id_produk_mix'],
        't_isi_produk_mix' : ['c_id_produk', 'c_id_produk_mix'],
        't_isi_tob' : ['c_kode_tob', 'c_kode_paket'],
        't_jenis_kelas' : [],
        't_paket_dan_bundel' : ['c_kode_paket'],
        't_paket_soal' : ['c_id_jenis_produk'],
        't_produk' : ['c_id_jenis_kelas', 'c_id_jenis_produk'],
        't_produk_mix' : ['c_id_jenis_kelas'],
        't_produk_tob' : ['c_kode_tob', 'c_id_produk'],
        't_tob' : [],
        #db_pt
        't_jurusan' : ['c_id_perguruan_tinggi','c_kode_kelompok_jurusan','c_kode_rumpun_jurusan'],
        't_jurusan_deskripsi' : ['c_id_jurusan'],
        #db_report_siswa_goa
        't_target_lulus_goa' : [],
        #db_sekolah
        't_mapel_kelompok_ujian' : ['c_id_mata_pelajaran', 'c_id_kelompok_ujian'],
        't_semester' : ['c_id_sekolah_kelas'],
        't_sekolah_siswa' : ['c_id_sekolah'],
        #db_user
        't_mapel_pilihan_siswa' :['c_no_register'],
        't_produk_aktif' : ['c_no_register'],
        't_produk_siswa' : ['c_no_register']
        
    }

    foreign_tables = {
        #db_go
        't_berita' : [],
        't_gokomar': ['t_kota'],
        #db_kbm
        't_bah_kelas' : ['t_kelas', 't_bah'],
        't_daftar_kegiatan_kbm' : [],
        't_feedback_pengajaran' :['t_rencana_kerja_kbm'],
        't_isi_bah': ['t_bah'],
        't_kelas_siswa' : ['t_kelas'],
        't_presensi_siswa' : ['t_rencana_kerja_kbm', 't_kelas'],
        't_rencana_kerja_kbm' : ['t_daftar_kegiatan_kbm'],
        #db_materi 
        't_bab' : [''],
        't_buku_produk' : ['t_buku'],
        't_bundel_soal' :[],
        't_isi_buku' : ['t_buku', 't_bab'],
        't_isi_bundel_soal' : ['t_soal', 't_bundel_soal'],
        't_mapel_bab' : ['t_bab'],
        't_paket_dan_bundel_materi' : ['t_bundel_soal'],
        't_soal_bab' : ['t_soal','t_bab'],
        't_soal_video_soal' : ['t_soal','t_video_soal'],
        't_teori_bab' : ['t_bab'],
        't_teori_bab_video' : ['t_teori_bab', 't_video_teori'],
        't_video_soal' : [],
        't_video_teori' : ['t_bab'],
        't_wacana' : [],
        't_wacana_soal' : ['t_soal','t_wacana'],
        #db_produk
        't_bundling' : ['t_jenis_kelas', 't_produk_mix'],
        't_isi_produk_mix' : ['t_produk', 't_produk_mix'],
        't_isi_tob' : ['t_tob', 't_paket_soal'],
        't_paket_dan_bundel' : ['t_paket_soal'],
        't_paket_soal' : ['t_jenis_produk'],
        't_produk' : ['t_jenis_kelas', 't_jenis_produk'],
        't_produk_mix' : ['t_jenis_kelas'],
        't_produk_tob' : ['t_tob', 't_produk'],
        #db_pt
        't_jurusan' : ['t_perguruan_tinggi','t_kelompok_jurusan','t_rumpun_jurusan'],
        't_jurusan_deskripsi' : ['t_jurusan'],
        #db_report_siswa_goa
        't_target_lulus_goa' : [],
        
        #db_sekolah
        't_mapel_kelompok_ujian' : ['t_mata_pelajaran', 't_kelompok_ujian'],
        't_semester' : ['t_sekolah_kelas'],
        't_sekolah_siswa' : ['t_sekolah'],
        
        #db_user
        't_mapel_pilihan_siswa':['t_siswa'],
        't_produk_aktif' : ['t_siswa'],
        't_produk_siswa' : ['t_siswa']
    }

    return foreign_keys.get(nama_table, []), foreign_tables.get(nama_table, [])

def unique_key(nama_table):
    unique_keys = {
        #db_go
        #db_kbm
        't_bah_kelas' : [['c_id_kelas', 'c_id_bah']],
        't_daftar_kegiatan_kbm' : [],
        't_feedback_pengajaran' :[['c_no_register', 'c_id_rencana']],
        't_isi_bah': [['c_id_bah', 'c_kode_bab']],
        't_kelas_siswa' : [['c_id_kelas', 'c_no_register']],
        't_presensi_siswa' : [['c_id_rencana', 'c_no_register']],
        #db_materi
        't_buku_produk' : [['c_id_buku', 'c_id_produk']],
        't_isi_buku' :[['c_id_buku','c_kode_bab']],
        't_isi_bundel_soal' : [['c_id_bundel', 'c_id_soal'],['c_id_bundel','c_id_soal','c_nomor_soal'], ['c_id_bundel', 'c_nomor_soal']],
        't_mapel_bab' : [['c_kode_bab', 'c_id_mata_pelajaran']],
        't_paket_dan_bundel_materi' : [['c_kode_paket','c_id_bundel','c_urutan'],['c_kode_paket','c_urutan'],['c_kode_paket','c_id_bundel']],
        't_teori_bab' : [],
        't_teori_bab_video' : [['c_id_video', 'c_id_teori_bab']],
        't_soal_bab' : [['c_id_soal','c_kode_bab']],
        't_soal_video_soal' : [['c_id_soal','c_id_video']],
        't_video_soal' : [],
        't_video_teori' : [],
        't_wacana' : [],
        't_wacana_soal': [['c_id_soal', 'c_id_wacana']],
        #db_produk
        't_bundling' : [],
        't_isi_produk_mix' : [['c_id_produk','c_id_produk_mix']],
        't_isi_tob'  : [['c_kode_paket','c_kode_tob']],
        't_jenis_kelas' : [],
        't_jenis_produk' : [],
        't_paket_dan_bundel' : [['c_kode_paket','c_id_bundel','c_urutan'],['c_kode_paket','c_urutan'],['c_kode_paket','c_id_bundel']],
        't_paket_soal' : [],
        't_produk' : [],
        't_produk_mix' : [],
        't_produk_tob' : [['c_kode_tob', 'c_id_produk']],
        't_tob' : [],
        #db_report_siswa_empati_mandiri
        #db_report_siswa_empati_wajib
        't_hasil_empati_12' : [['c_no_register', 'c_kode_tob','c_kode_paket']],
        #db_report_siswa_goa
        't_target_lulus_goa' : [['c_id_tingkat_kelas','c_tahun_ajaran','c_id_kelompok_ujian']],
        #db_report_siswa_peringkat
        't_pengerjaan_mata_uji' : [['c_no_register', 'c_id_kelompok_ujian', 'c_id_jenis_produk', 'c_tanggal']],
        't_target_mapel' : [['c_id_sekolah_kelas','c_id_kelompok_ujian', 'c_semester']],
        't_target_pengerjaan_siswa' : [['c_id_sekolah_kelas', 'c_no_register']],
        #db_sekolah
        't_mapel_kelompok_ujian' : [['c_id_kelompok_ujian','c_id_mata_pelajaran']],
        't_sekolah_siswa' : [['c_no_register','c_id_sekolah']],
        #db_user
        't_mapel_pilihan_siswa' : [['c_no_register']],
        't_produk_aktif' : [['c_no_register', 'c_id_produk']],
        't_produk_siswa' : [['c_id_pembelian']]
        
    }

    return unique_keys.get(nama_table, [])