data_nilai_siswa = [
    ["Rafli", 90, 85, "N/A", 92], 
    ["Budi", 78, "absen", 88, 80], 
    ["Cinta", 100, 95, 98, 99],
    ["Dewi", 70, 75, 68, 72]
]
siswa_terbaik = []

if len(data_nilai_siswa) <= 0:
  raise ValueError('data nilai mahasiswa tidak boleh kosong')

for siswa in data_nilai_siswa : 
  nama_siswa = siswa[0]
  print(f'Menganalisis Nilai dari {nama_siswa}.....')
  total = 0
  nilai_valid = 0
  for nilai in siswa : 
    try:
      total += nilai
    except:
      pass
    else:
      nilai_valid += 1
  rata_rata = total/nilai_valid
  if rata_rata >= 85 :
    siswa_terbaik.append(nama_siswa)
  print(f'Nama siswa : {nama_siswa}\nTotal Nilai : {total}\nRata-rata : {rata_rata}\n')

print(f'Mahasiswa terbaik : {siswa_terbaik}')