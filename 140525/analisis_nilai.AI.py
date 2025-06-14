data_nilai_siswa = [
    ["Rafli", 90, 85, "N/A", 92], 
    ["Budi", 78, "absen", 88, 80], 
    ["Cinta", 100, 95, 98, 99],
    ["Dewi", 70, 75, 68, 72]
]

# 1. Menangani Data Kosong
if not data_nilai_siswa:
    raise ValueError('Data nilai siswa tidak boleh kosong')
hasil_analisis = []

# 2. Nested Loop dengan Perbaikan
for data_siswa in data_nilai_siswa: 
    nama_siswa = data_siswa[0]
    total_nilai = 0
    jumlah_nilai_valid = 0

    for nilai in data_siswa[1:]: 
        try:
            total_nilai += int(nilai)
            jumlah_nilai_valid += 1
        except (ValueError, TypeError):
            # Mengabaikan nilai yang tidak bisa diubah ke angka
            pass
    
    
    if jumlah_nilai_valid > 0:
        rata_rata = total_nilai / jumlah_nilai_valid
    else:
        rata_rata = 0

    hasil_analisis.append({"nama": nama_siswa, "rata_rata": rata_rata})
    print(f"Analisis selesai untuk {nama_siswa}, rata-rata: {rata_rata:.2f}")

print("\n---")
siswa_terbaik = [
    siswa["nama"] 
    for siswa in hasil_analisis 
    if siswa["rata_rata"] > 85
]

print(f"Siswa dengan nilai rata-rata di atas 85: {siswa_terbaik}")