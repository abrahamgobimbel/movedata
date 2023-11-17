import pandas as pd

data_komar = [
    {
        'c_id_komar': 1800,
        'c_nama_komar': 'Jln. Sultan Agung Utara No. 24',
        'c_id_kewilayahan': 9,
        'c_upline': 1379,
        'c_id_kota': 0,
        'c_status': 'TidakAktif',
        'c_updater': 1510500459,
        'c_last_update': '2023-07-28 11:02:31'
    }
]

# Membuat dataframe dari array
df = pd.DataFrame(data_komar)

# Menyimpan dataframe ke dalam file Excel
df.to_excel('t_gokomar.xlsx', index=False)
