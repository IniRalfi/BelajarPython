"""Soal 3: Pemroses Data Kontak Sederhana
Buatlah sebuah program yang:

Membuat sebuah dictionary untuk menyimpan informasi kontak seorang teman. Dictionary ini harus memiliki kunci (key) berikut:
nama (string)
telepon (string, contoh: "081234567890")
email (string, contoh: "TemanBaik@example.com")
hobi (list of strings, contoh: ["membaca", "berenang", "coding"])
Isi dictionary tersebut dengan data contoh untuk satu teman.
Cetak email teman tersebut, namun pastikan semua hurufnya adalah huruf kecil.
Cetak hobi pertama dan hobi terakhir dari teman tersebut.
Jika teman tersebut hanya memiliki satu hobi, tampilkan hobi tersebut untuk "hobi pertama" dan "hobi terakhir".
Jika teman tersebut tidak memiliki hobi (list hobi kosong), cetak pesan "Teman ini belum punya hobi."
Lakukan pengecekan apakah nilai pada kunci telepon hanya terdiri dari angka. Cetak hasil pengecekannya (True jika hanya angka, False jika ada karakter lain).
Petunjuk:

Akses nilai dalam dictionary menggunakan kuncinya.
Gunakan indexing list (misal nama_list[0]) untuk mendapatkan hobi pertama/terakhir.
Gunakan metode string .lower() dan .isdecimal().
"""

import questionary


def tambah_kontak():
    kontak = {}
    nama = questionary.text("Masukkan nama kontak: ", qmark="👤 ").ask()
    telepon = questionary.text("Masukkan nomor telepon: ").ask()
    email = questionary.text("Masukkan email:").ask()
    hobi = []
    while True:
        item = questionary.text('Masukkan hobi: ("n" untuk berhenti)').ask().lower()
        if item == "n":
            break
        hobi.append(item)

    kontak = {"nama": nama, "telepon": telepon, "email": email, "hobi": hobi}
    print("Kontak berhasil ditambahkan")
    return kontak


def cetak_kontak(kontak):
    print(f"Nama: {kontak['nama']}")
    print(f"Telepon: {kontak['telepon']}")
    print(f"email: {kontak['email']}")
    if len(kontak["hobi"]) == 0:
        print(f"{kontak['nama']} belum memiliki hobi")
    else:
        print(f"Hobi pertama: {kontak['hobi'][0]}")
        print(f"Hobi terakhir: {kontak['hobi'][-1]}")

    decimal = kontak["telepon"].isdecimal()
    print(f"Apakah telepon semuanya angka: {decimal}")


cetak_kontak(tambah_kontak())
