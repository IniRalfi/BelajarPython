"""Kamu diberikan daftar belanjaan awal sebagai berikut:
daftar_awal = ["Apel", "pisang", "Apel", "Jeruk", "PISANG", "mangga", "apel"]

Buatlah program yang:

Membuat daftar belanjaan unik dari daftar_awal. Semua item dalam daftar unik ini harus dalam format huruf kecil (lowercase).
Urutkan daftar belanjaan unik tersebut berdasarkan abjad.
Cetak daftar belanjaan unik yang sudah diurutkan.
Cetak jumlah item unik dalam daftar belanjaan tersebut.
Minta pengguna memasukkan nama item yang ingin mereka cari jumlahnya di daftar_awal (pencarian tidak boleh sensitif terhadap huruf besar/kecil).
Tampilkan berapa kali item yang dicari pengguna tersebut muncul di daftar_awal.
Contoh Interaksi Pengguna untuk Poin 5 & 6:

Masukkan nama item yang ingin dihitung: apel
Item "apel" muncul 3 kali dalam daftar belanjaan awal.
Petunjuk:

Gunakan set untuk mendapatkan item unik.
Gunakan metode .lower() untuk konversi ke huruf kecil.
Gunakan fungsi sorted() atau metode .sort() untuk mengurutkan.
Gunakan fungsi len() untuk menghitung jumlah.
Gunakan metode .count() pada list (setelah melakukan normalisasi kasus huruf untuk pencarian).
"""

import questionary


def hitung_data(data):
    data_bersih = []
    for item in data:
        data_bersih.append(item.strip().lower())
    data_clean = list(set(data_bersih))
    data_clean_sorted = sorted(data_clean)
    print(data_clean_sorted)
    banyak_data = len(data_clean_sorted)
    print(banyak_data)

    data_dicari = (
        questionary.text("Masukkan data yang ingin dicari : ").ask().lower().strip()
    )

    if data_dicari in data_clean_sorted:
        banyak_data_dicari = data_bersih.count(data_dicari)
        return banyak_data_dicari
    else:
        return "Data tidak ditemukan"


daftar_awal = ["Apel", "pisang", "Apel", "Jeruk", "PISANG", "mangga", "apel"]
hitung = hitung_data(daftar_awal)
print(hitung)
