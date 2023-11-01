def query_select(nama_table) :
    if nama_table == 't_target_lulus_goa' :
        query = f"SELECT *, current_timestamp() FROM db_report_siswa_goa.t_targetlulusgoa where c_tahunajaran = '2023/2024';"
    return query
