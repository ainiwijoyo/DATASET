# -*- coding: utf-8 -*-
"""Covid19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_eNO3rk8_24ovhXpm6eKMD0re0JDtSMz

## Data Selection
"""

import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None)

# Memanggil dataset
data = pd.read_csv('/content/drive/MyDrive/Dataset/covid_19_indonesia_time_series_all.csv')

data.head(10)

# Menampilkan baris dan kolom dari dataset
data.shape

# Melihat semua kolom dalam dataset
data.columns

# Menampilkan informasi feature dari dataset
data.info()

"""Dataset covid-19 yang digunakan terdiri dari 38 Feature, yaitu:



1.   Date: Tanggal dicatatnya data, tipe data nominal
2. Location ISO Code: Kode lokasi berdasarkan standar ISO
3. Location: nama lokasi
4. New Cases: kasus positif baru harian
5. New Deaths: kematian baru harian
6. New Recovered: Sembuh dalam harian
7. New Active Cases: kasus aktif baru harian
8. Total Cases: Total kasus positif sampai tanggal terkait
9. Total Deaths: Total kematian sampai tanggal terkait
10. Total Recovered: Total sembuh sampai tanggal terkait
11. Total Active Cases: Total kasus aktif sampai tanggal terkait
12. Location Level: level lokasi (provinsi & country)
13. Province: Nama provinsi dari Location
14. Country: Nama country dari Location
15. Continent: nama kontinen dari Location (unique: Asia)
16. Island: nama pulau dari Location
17. Time Zone: Waktu
18. Special Status
19. Total Regencies: Jumlah kabupaten di lokasi.
20. Total Cities: Jumlah kota di lokasi.
21. Total Districts: Jumlah kecamatan di lokasi.
22. Total Urban Villages: Jumlah kelurahan di lokasi.
23. Total Rural Villages: Jumlah desa di lokasi.
24. Area(km2): Area lokasi (km2)
25. Population: populasi di lokasi
26. Population Density: Kepadatan penduduk di lokasi (Rumus: Penduduk/Luas).
27. Longitude: Longitude lokasi
28. Latitude of location: latitude
29. New Cases per Million: Formula: (New Cases / Population) * 1000000
30. Total Cases per Million: Formula: (Total Cases / Population) * 1000000
31. New Deaths per Million: Formula: (New Deaths / Population) * 1000000
32. Total Deaths per Million: Formula: (Total Deaths / Population) * 1000000
33. Total Deaths per 100rb: Formula: (Total Deaths / Total Cases) * 100
34. Case Fatality Rate: Formula: (Total Recovered / Total Cases) * 100
35. Case Recovered Rate: Under 1 means decrease, 1 means flat, above 1 means increase. Formula: Today New Cases / Yesterday New Cases
36. Growth Factor of New Cases: Under 1 means decrease, 1 means flat, above 1 means increase. Formula: Today New Deaths / Yesterday New Deaths
37. Growth Factor of New Death


Dataset memiliki jumlah record/baris 31822
Untuk atribut '

1.   Tipe data kolom Date masih object jadi harus diubah dulu
2.   Kolom City of Regency kosong dan special status banyak yg kosong jadi dihapus aja
"""

# Merubah format tanggal
import datetime as datetime

NewDate=[]
for item in data['Date']:
    item2=item.split('/')
    month=int(item2[0])
    day=int(item2[1])
    year=int(item2[2])
    NewDate +=[datetime.date(year,month,day)]
data['Date'] = NewDate
data['Date'] = pd.to_datetime(data['Date'])

data.head(10)

data.isna().sum()

# Menghapus kolom yang paling banyak memiliki missing value
data = data.drop(['City or Regency',"Special Status"], axis=1)

#menghapus record yang banyak missing valuenya
data = data.dropna(axis = 0, how ='any')

data.isna().sum()

# Memanggil data untuk level provinsi
data1 = data[data['Location Level'] != 'Country']

# Data Terbaru
newest = data1.drop_duplicates(subset='Location', keep="last")
newest.head()

data.to_csv('filename.csv', index=False)

# Memanggil Data COVID 19 as per updated 2022
newest[newest.Location != 'Indonesia'].sort_values(by=['Total Cases'], ascending=False)

"""# VISUALISASI"""

# Provinsi dengan Total Kasus Terbanyak
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,6))
sns.barplot(newest[newest.Location != 'Indonesia'].sort_values(by=['Total Cases'], ascending=False)['Location'].values[:5], newest[newest.Location != 'Indonesia'].sort_values(by=['Total Cases'], ascending=False)['Total Cases'].values[:5])
plt.title('5 Provinsi Teratas Dengan Total Kasus Paling Banyak', fontsize=14)
plt.xlabel('Provinsi')
plt.ylabel('Jumlah Kasus')
plt.show()

# Provinsi dengan Angka Kematian Terbanyak
plt.figure(figsize=(12,6))
sns.barplot(newest[newest.Location != 'Indonesia'].sort_values(by=['Total Deaths'], ascending=False)['Location'].values[:5],  newest[newest.Location != 'Indonesia'].sort_values(by=['Total Deaths'], ascending=False)['Total Deaths'].values[:5])
plt.title('5 Provinsi Teratas Dengan Total Kematian Paling Banyak', fontsize=25)
plt.xlabel('Provinsi', fontsize=12)
plt.ylabel('Jumlah Kasus Kematian', fontsize=12)
plt.show()

# Provinsi dengan Angka Kesembuhan Terbanyak
plt.figure(figsize=(12,9))
sns.barplot(newest[newest.Location != 'Indonesia'].sort_values(by=['Total Recovered'], ascending=False)['Location'].values[:5],  newest[newest.Location != 'Indonesia'].sort_values(by=['Total Recovered'], ascending=False)['Total Recovered'].values[:5])
plt.title('5 Provinsi Teratas Dengan Total Kesembuhan Paling Banyak', fontsize=25)
plt.xlabel('Provinsi', fontsize=15)
plt.ylabel('Kasus Kesembuhan', fontsize=15)
plt.show()

# Provinsi dengan Angka Kasus Aktif Terbanyak
plt.figure(figsize=(12,9))
sns.barplot(newest[newest.Location != 'Indonesia'].sort_values(by=['Total Active Cases'], ascending=False)['Location'].values[:5],  newest[newest.Location != 'Indonesia'].sort_values(by=['Total Active Cases'], ascending=False)['Total Active Cases'].values[:5])
plt.title('5 Provinsi Teratas Dengan Total Kasus Aktif Paling Banyak', fontsize=25)
plt.xlabel('Provinsi', fontsize=15)
plt.ylabel('Kasus Aktif', fontsize=15)
plt.show()

data2 = data1[['New Deaths', 'New Cases','Total Cases', 'New Recovered', 'Total Recovered', 'Total Deaths','Population', 'Population Density']]
sns.pairplot(data2)
plt.show()
