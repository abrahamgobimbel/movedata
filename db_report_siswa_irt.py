import os
import functioninput

def query_select(nama_table) :
    
    if nama_table == 't_irt_nilai_to' : 
        query = ("select tit.c_PeriodeTO, tit.c_IdPenanda,c_PUNilaiTO,\n"
                "c_PBMNilaiTO,c_PPUNilaiTO,c_PKNilaiTO,\n"
                "c_INGNilaiTO,c_MAIPANilaiTO,c_FINilaiTO,\n"
                "c_KINilaiTO,c_BIONilaiTO, c_MAIPSNilaiTO,\n"
                "c_SEJNilaiTO,c_SOSNilaiTO,c_GEONilaiTO,\n"
                "c_EKONilaiTO,c_PS,c_IsSimulasi,c_KodeTOB,\n"
                "c_PKOGNilaiTO,c_PMNilaiTO,c_LBINDNilaiTO,\n"
                "c_LBINGNilaiTO,c_KKNilaiTO,c_KPUPDNilaiTO,\n"
                "c_KPUPINilaiTO,c_KPUPKNilaiTO,c_KPUNilaiTO,\n"
                "ROW_NUMBER() OVER (),\n"
                "tit.formatted_no_registrasi_int,NULL\n"
                "FROM \n"
                "(SELECT *, CAST(LPAD(REPLACE(tit.c_noregistrasi, ' ', ''), 12, '0') AS UNSIGNED) AS formatted_no_registrasi_int\n"
                "FROM\n"
                "db_GOIconsV2.t_IRTNilaiTO tit\n"
                ") tit\n"
                "JOIN db_GOIconsV2.t_Cluster_Siswa tcs ON tit.formatted_no_registrasi_int = tcs.c_NoRegistrasi\n"
                "where tcs.c_TahunAjaran = '2023/2024';\n")
    return query