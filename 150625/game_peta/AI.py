import questionary
import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def cetak_peta(peta):
  print("=====PETA HARTA KARUN=====")
  for baris in peta:
    for kolom in baris:
      if kolom == 0:
        print(". ",end='')
      elif kolom == 1:
        print('# ', end='')
      elif kolom == 8:
        print('X ', end='')
      elif kolom == 9:
        print('P ',end='')
    print()
  print('========================')

def gerak(peta, posisi_pemain, arah):
  baris, kolom = posisi_pemain[0], posisi_pemain[1]
  baris_baru, kolom_baru = baris, kolom

  if arah == 'w':
    baris_baru -= 1
  elif arah == 's':
    baris_baru += 1
  elif arah == 'a':
    kolom_baru -= 1
  elif arah == 'd':
    kolom_baru += 1

  if not (0 <= baris_baru < len(peta) and 0 <= kolom_baru < len(peta[0])):
    print("\n>> Kamu tidak bisa keluar dari peta!")

  if peta[baris_baru][kolom_baru] == 1:
      print("\n>> Ouch! Kamu menabrak tembok.")
      return False
  
  peta[baris][kolom] = 0

  if peta[baris_baru][kolom_baru] == 8:
        peta[baris_baru][kolom_baru] = 9
        return True

  posisi_pemain[0], posisi_pemain[1] = baris_baru, kolom_baru
  peta[baris_baru][kolom_baru] = 9
  return False

peta = [
    [9, 0, 0, 1, 0],  # Angka 9 menandai posisi awal pemain
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 8]
]
posisi_pemain = [0, 0] 

while True:
    clear_screen()
    cetak_peta(peta)
    
    arah = questionary.select(
        'Pilih arah gerak (w/a/s/d):',
        choices=['w', 'a', 's', 'd', {'name': 'Keluar', 'value': 'q'}]
    ).ask()

    if arah == 'q' or arah is None:
        print("Kamu menyerah. Sampai jumpa!")
        break

    menang = gerak(peta, posisi_pemain, arah)

    if menang:
        clear_screen()
        cetak_peta(peta)
        print("\nSELAMAT! Kamu berhasil menemukan harta karun! 🏆")
        break