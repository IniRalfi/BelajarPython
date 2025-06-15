import questionary

def tampilkan_inventaris(data_inventaris) :
  if len(data_inventaris) == 0:
    return 'Inventaris masih kosong'
  
  for data in data_inventaris:
    print(f'''Nama : {data['nama']}
Stock : {data['stok']}
Harga : Rp.{data['harga']}\n''')
    
def tambahkan_inventaris(data_inventaris):
  try:
    nama = questionary.text('Masukkan nama barang: ').ask()
    stok = int(questionary.text('Masukkan jumlah stok barang: ').ask())
    harga = int(questionary.text('Masukkan harga barang: Rp').ask())
  except(ValueError, SyntaxError):
    raise ValueError('Pastikan stok atau harga adalah angka!')
  else:
    data = {'nama' : nama, 'stok':stok, 'harga' : harga}
    data_inventaris.append(data)
  finally:
    return data_inventaris

def cari_barang(data_inventaris):
  barang = questionary.text('Masukkan nama barang yang ingin dicari: ').ask()
  for data in data_inventaris:
    if barang == data['nama']:
      return data
  else:
    return None


inventaris = [
    {"nama": "Buku Tulis", "stok": 20, "harga": 5000},
    {"nama": "Pensil 2B", "stok": 50, "harga": 2000},
    {"nama": "Penghapus", "stok": 30, "harga": 1500},
    {"nama": "Penggaris", "stok": 15, "harga": 2500}
]

while True:
  operasi = questionary.select('Silahkan pilih operasi berikut: ', [
    {'name' : '1. Tambah Inventaris', 'value':'1'},
    {'name':'2. Cetak Inventaris', 'value' : '2'},
    {'name' : '3. Cari barang', 'value': '3'},
    {'name' : '4. Keluar', 'value':'4'}
  ]).ask()

  if operasi == '1':
    tambahkan_inventaris(inventaris)
  elif operasi == '2':
    tampilkan_inventaris(inventaris)
  elif operasi == '3':
    cari_barang(inventaris)
  elif operasi == '4':
    break

