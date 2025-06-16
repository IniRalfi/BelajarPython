import questionary

def cetak_peta(peta, posisi_pemain):
  print()
  for i in range(len(peta)):
    for j in range(len(peta)):
      if posisi_pemain[0] == i and posisi_pemain[1] == j:
        print(f'P', end=" ")
      elif peta[i][j] == 0:
        print('.',end=' ')
      elif peta[i][j] == 1:
        print('#',end=' ')
      elif peta[i][j] == 8:
        print('X',end=' ')
    print()
      
def gerak(peta, posisi_pemain, arah):
  if arah == 'w':
    if posisi_pemain[0] == 0:
      print('Anda sudah berada dibatas peta!')
      return posisi_pemain
    posisi_pemain[0] -= 1
    if peta[posisi_pemain[0]][posisi_pemain[1]] == 1:
      print('Anda menabrak tembok!')
      posisi_pemain[0] += 1
    elif peta[posisi_pemain[0]][posisi_pemain[1]] == 8:
      print('Selamat Anda menemukan harta karun!')
    return posisi_pemain
  
  elif arah == 'd':
    posisi_pemain[1] += 1
    if peta[posisi_pemain[0]][posisi_pemain[1]] == 1:
      print('Anda menabrak tembok!')
      posisi_pemain[1] -= 1
    elif peta[posisi_pemain[0]][posisi_pemain[1]] == 8:
      print('Selamat Anda menemukan harta karun!')
    return posisi_pemain
  
  elif arah == 's':
    posisi_pemain[0] += 1
    if peta[posisi_pemain[0]][posisi_pemain[1]] == 1:
      print('Anda menabrak tembok!')
      posisi_pemain[0] -= 1
    elif peta[posisi_pemain[0]][posisi_pemain[1]] == 8:
      print('Selamat Anda menemukan harta karun!')
    return posisi_pemain
  
  elif arah == 'a':
    if posisi_pemain[1] == 0:
      print('Anda sudah berada dibatas peta!')
      return posisi_pemain
    posisi_pemain[1] -= 1
    if peta[posisi_pemain[0]][posisi_pemain[1]] == 1:
      print('Anda menabrak tembok!')
      posisi_pemain[1] += 1
    elif peta[posisi_pemain[0]][posisi_pemain[1]] == 8:
      print('Selamat Anda menemukan harta karun!')
    return posisi_pemain
  
peta = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 8]
]

posisi_pemain = [0, 1] 

while True:
  print('Selamat datang di game peta: ')
  main = questionary.select('Silahkan pilih: ', ['main','keluar']).ask()

  if main == 'main':
    print('Ini adalah posisi awal anda: ')
    print()
    cetak_peta(peta, posisi_pemain)
    arah = questionary.select('Pilih arah gerak: ', [
    {'name' : 'atas', 'value' : 'w'},
    {'name' : 'kanan', 'value':'d'},
    {'name':'bawah', 'value':'s'},
    {'name':'kiri', 'value':'a'}
  ]).ask()
    print()
    gerak(peta,posisi_pemain,arah)
    print()
    print('Posisi Terbaru anda: ')
    cetak_peta(peta, posisi_pemain)
    print()
  else:
    break
