# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


# %%
SN12_KRT_PATH = './data_susenas/sn12_krt.csv'
COLUMNS = ['URUT', 'B1R1', 'B1R2', 'B1R5', 'B2R1', 'B8R2A', 'B8R2B', 'B8R2C', 'B8R3A', 'B8R3B', 'B9R1A', 'B9R1B', 'EXP_CAP', 'WERT']
def get_dataframe(path):
    return pd.read_csv(path)

# %% [markdown]
# - URUT: 
# - B1R1: Kode Provinsi
# - B1R2: Kode Kabupaten
# - B1R5: Klasifikasi desa/kelurahan (apakah berstatus daerah perkotaan/pedesaan)
# - B8R2A: Banyaknya anggota rumah tangga yang menguasai nomor HP yang aktif
# - B8R2B: Apakah ada anggota rumah tangga yang menguasai telepon seluler (HP)?
# - B8R2C: Jumlah nomor HP aktif yang dikuasai seluruh anggota keluarga
# - B8R3A: Apakah di rumah tangga ini ada komputer (PC)
# - B8R3B: Apakah di rumah tangga ini ada komputer (Laptop)
# - B9R1A: Apa lapangan usaha atau bidang pekerjaan (utama) dari tempat pekerjaan (nama) selama seminggu terakhir?
# - B9R1B: Status Pekerjaan
# - EXP_CAP: Pengeluaran per kapita
# - WERT: bobot

# %%
df_sn12_krt = get_dataframe(SN12_KRT_PATH)
df_sn12_krt['B2R1'].describe()


# %%
df_raw = df_sn12_krt[COLUMNS]
df_raw


# %%
pekerjaan = {
    1: "Pertanian tanaman padi & palawija",
    2: "Hortikultura",
    3: "Perkebunan",
    4: "Perikanan",
    5: "Peternakan",
    6: "Kehutanan & pertanian lainnya",
    7: "Pertambangan & penggalian",
    8: "Industri pengolahan",
    9: "Listrik & gas",
    10: "Konstruksi/bangunan",
    11: "Perdagangan",
    12: "Hotel dan rumah makan",
    13: "Transportasi dan pergudangan",
    14: "Informasi dan komunikasi",
    15: "Keuangan dan asuransi",
    16: "Jasa pendidikan",
    17: "Jasa kesehatan",
    18: "Jasa kemasyarakatan, pemerintahan, & perorangan",
    19: "Lainnya"
}


# %%



# %%
new_df = df_raw.copy()
new_df["Pekerjaan"] = new_df["B9R1A"].apply(lambda x: pekerjaan.get(x))
new_df


# %%
new_df.describe()


# %%
# Histogram for Log Expenditure per Capita Variable

new_df=new_df.assign(log_exp_cap=np.log(new_df['EXP_CAP']))
plot_exp = new_df['log_exp_cap']

plot_exp.plot.hist(grid=False, bins=50, rwidth=0.9,color='maroon',label='Log PCE')
plt.title('Distribution for Log Per Capita Expenditure Variable')
plt.xlabel('Value of x-variable')
plt.ylabel('Counts')
plt.legend(loc="best")
plt.tight_layout()
plt.rcParams['figure.figsize'] = [10, 4]
plt.show()


# %%
income = new_df[['EXP_CAP', 'B2R1', 'B8R2A', 'B8R2B', 'B8R2C']]
# income = income.sort_values(by=['EXP_CAP'])
income = income[income['B8R2A'] == 1]
income = income[income['EXP_CAP'] < 500000]
income = income[income['B8R2C'] < 10]
income

# %%
x_age = income['EXP_CAP']
y_age = income['B8R2C']

# Plot
plt.scatter(x_age, y_age, alpha=0.4)
plt.title('Pendapatan Per Kapita dan Kepemilikan HP')
plt.xlabel('Pendapatan Per Kapita')
plt.ylabel('Kepemilikan HP')
plt.rcParams['figure.figsize'] = [7,7]
plt.show()
