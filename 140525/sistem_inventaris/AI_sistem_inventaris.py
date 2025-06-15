import questionary

def tampilkan_inventaris(data_inventaris):
    """Menampilkan semua barang dalam inventaris."""
    if not data_inventaris:
        print("\n>> Inventaris masih kosong.\n")
        return
    
    print("\n--- Daftar Inventaris ---")
    for barang in data_inventaris:
        print(f"Nama  : {barang['nama']}")
        print(f"Stok  : {barang['stok']}")
        print(f"Harga : Rp {barang['harga']:,}") # Format angka dengan pemisah ribuan
        print("-------------------------")
    print()

def tambahkan_inventaris(data_inventaris):
    """Menambahkan barang baru ke inventaris dengan validasi input."""
    try:
        nama = questionary.text('Masukkan nama barang: ').ask()
        # Cek jika pengguna membatalkan input
        if not nama:
            print("\n>> Penambahan barang dibatalkan.\n")
            return

        stok = int(questionary.text('Masukkan jumlah stok barang: ').ask())
        harga = int(questionary.text('Masukkan harga barang: Rp').ask())

    except (ValueError, TypeError):
        # Menangani jika input stok/harga bukan angka
        print("\n>> ERROR: Pastikan stok dan harga adalah angka! Barang tidak ditambahkan.\n")
    else:
        # Blok ini hanya berjalan jika tidak ada error
        barang_baru = {'nama': nama, 'stok': stok, 'harga': harga}
        data_inventaris.append(barang_baru)
        print(f"\n>> Berhasil menambahkan '{nama}' ke inventaris.\n")

def cari_barang(data_inventaris):
    """Mencari barang berdasarkan nama dan menampilkan hasilnya."""
    nama_barang = questionary.text('Masukkan nama barang yang ingin dicari: ').ask()
    if not nama_barang:
        print("\n>> Pencarian dibatalkan.\n")
        return

    for barang in data_inventaris:
        if nama_barang.lower() == barang['nama'].lower(): # Pencarian case-insensitive
            print("\n--- Barang Ditemukan ---")
            print(f"Nama  : {barang['nama']}")
            print(f"Stok  : {barang['stok']}")
            print(f"Harga : Rp {barang['harga']:,}")
            print("------------------------\n")
            return # Keluar dari fungsi setelah menemukan barang

    # Baris ini hanya akan dieksekusi jika loop selesai tanpa menemukan apa pun
    print(f"\n>> Maaf, barang dengan nama '{nama_barang}' tidak ditemukan.\n")

# --- Program Utama ---
inventaris = [
    {"nama": "Buku Tulis", "stok": 20, "harga": 5000},
    {"nama": "Pensil 2B", "stok": 50, "harga": 2000},
    {"nama": "Penghapus", "stok": 30, "harga": 1500},
    {"nama": "Penggaris", "stok": 15, "harga": 2500}
]

while True:
    operasi = questionary.select(
        'Silahkan pilih operasi berikut:',
        choices=[
            '1. Tampilkan Inventaris',
            '2. Tambah Barang Baru',
            '3. Cari Barang',
            '4. Keluar'
        ]
    ).ask()

    if operasi == '1. Tampilkan Inventaris':
        tampilkan_inventaris(inventaris)
    elif operasi == '2. Tambah Barang Baru':
        tambahkan_inventaris(inventaris)
    elif operasi == '3. Cari Barang':
        cari_barang(inventaris) # Fungsi ini sekarang mencetak hasilnya sendiri
    elif operasi == '4. Keluar' or operasi is None: # Menangani jika pengguna menekan Ctrl+C
        print("Terima kasih telah menggunakan sistem inventaris!")
        break