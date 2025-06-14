# Status awal Ksatria
kekuatan = 10
nyawa = 100
koin = 200

print(f"--- Status Awal Ksatria ---")
print(f"Kekuatan: {kekuatan}")
print(f"Nyawa: {nyawa}")
print(f"Koin: {koin}\n")

# --- Bagian 1: Menemukan Harta Karun ---
print("--- Menemukan Harta Karun ---")
kekuatan_tambahan = 15
nyawa_tambahan = 50

kekuatan += kekuatan_tambahan # kekuatan = kekuatan + kekuatan_tambahan
nyawa += nyawa_tambahan       # nyawa = nyawa + nyawa_tambahan

print(f"Ksatria menemukan Pedang Legendaris (+{kekuatan_tambahan} Kekuatan) dan Ramuan Ajaib (+{nyawa_tambahan} Nyawa).")
print(f"Kekuatan baru: {kekuatan}")
print(f"Nyawa baru: {nyawa}\n")

# --- Bagian 2: Berbelanja di Toko ---
# Menggunakan operator aritmetika (-=) untuk mengurangi koin
print("--- Berbelanja di Toko ---")
harga_perisai = 125

koin -= harga_perisai # koin = koin - harga_perisai

print(f"Ksatria membeli Perisai Baja seharga {harga_perisai} koin.")
print(f"Koin tersisa: {koin}\n")

# --- Bagian 3: Misi Khusus (Gerbang Gua Naga) ---
# Menggunakan operator relasional (>) dan logika (and)
print("--- Misi Khusus: Gerbang Gua Naga ---")
syarat_kekuatan_min = 20
syarat_koin_min = 50

siap_bertualang = (kekuatan > syarat_kekuatan_min) and (koin > syarat_koin_min)

print(f"Syarat masuk Gua Naga: Kekuatan > {syarat_kekuatan_min} DAN Koin > {syarat_koin_min}")
print(f"Apakah Ksatria siap bertualang ke Gua Naga? {siap_bertualang}\n")

# --- Bagian 4: Bonus Keberuntungan ---
# Menggunakan operator modulo (%)
print("--- Bonus Keberuntungan ---")
if koin % 2 == 0:
    bonus_koin = 20
    koin += bonus_koin
    print(f"Selamat! Sisa koinmu genap ({koin - bonus_koin}), kamu mendapatkan bonus {bonus_koin} koin!")
    print(f"Total koin sekarang: {koin}\n")
else:
    print(f"Sisa koinmu ({koin}) ganjil, tidak ada bonus keberuntungan kali ini.\n")


# --- Hasil Akhir ---
# Mencetak semua nilai akhir
print("--- Status Akhir Ksatria ---")
print(f"Kekuatan: {kekuatan}")
print(f"Nyawa: {nyawa}")
print(f"Koin: {koin}")
print(f"Siap Bertualang ke Gua Naga: {siap_bertualang}")