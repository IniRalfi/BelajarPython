"""
Soal 1: Sapa Pengguna Pribadi
Buatlah sebuah program yang melakukan hal berikut:

Meminta input dari pengguna untuk nama depan mereka.
Meminta input dari pengguna untuk nama belakang mereka.
Meminta input dari pengguna untuk tahun kelahiran mereka (misalnya "1998").
Konversi tahun kelahiran menjadi tipe data integer.
Hitung usia pengguna saat ini (asumsikan tahun sekarang adalah 2025).
Gabungkan nama depan dan nama belakang menjadi satu string nama lengkap. Pastikan setiap kata pada nama lengkap diawali dengan huruf kapital (contoh: "Budi Santoso").
Cetak sapaan yang menyertakan nama lengkap dan usia mereka. Contoh output: Halo, Budi Santoso! Usia Anda tahun ini adalah 27 tahun.
Cek apakah nama lengkap pengguna mengandung huruf "a" (baik huruf kecil maupun besar) dan cetak hasilnya (True atau False).
Petunjuk:

Gunakan fungsi input() untuk mendapatkan data dari pengguna.
Gunakan fungsi int() untuk konversi ke integer.
Manfaatkan metode string seperti .capitalize() atau kombinasi .lower() dan slicing jika diperlukan untuk format nama.
Gunakan operator in untuk pengecekan huruf.
"""

import questionary


def sapa_pengguna():
    # Meminta input dari pengguna
    nama_depan = questionary.text("Masukkan nama depan Anda:").ask().strip()
    nama_belakang = questionary.text("Masukkan nama belakang Anda:").ask().strip()
    tahun_kelahiran = (
        questionary.text("Masukkan tahun kelahiran Anda (misalnya '1998'):")
        .ask()
        .strip()
    )
    # Konversi tahun kelahiran menjadi integer
    tahun_kelahiran = int(tahun_kelahiran)
    # Hitung usia pengguna
    tahun_sekarang = 2025
    usia = tahun_sekarang - tahun_kelahiran
    # Gabungkan nama depan dan nama belakang
    nama_lengkap = f"{nama_depan.capitalize()} {nama_belakang.capitalize()}"
    print(f"Halo, {nama_lengkap}! Usia Anda tahun ini adalah {usia} tahun.")

    # Cek apakah nama lengkap mengandung huruf 'a'
    mengandung_a = "a" in nama_lengkap.lower()
    print(f"Apakah nama lengkap Anda mengandung huruf 'a'? {mengandung_a}")


sapa_pengguna()
