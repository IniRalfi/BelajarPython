# Validasi dan pembersihan kode produk
def validasi_kode_produk(kode_input):
    kode_bersih = kode_input.strip().upper()
    parts = kode_bersih.split("-")

    if len(parts) != 3:
        return "KODE_INVALID"

    if (
        parts[0].isalpha()
        and len(parts[0]) == 3
        and parts[1].isdigit()
        and len(parts[1]) == 7
        and parts[2].isalpha()
        and len(parts[2]) == 1
    ):
        return "-".join(parts)
    else:
        return "KODE_INVALID"


kode1 = "   abc-1234567-d   "
kode2 = "xyz-9876543-a"  # Sudah bersih tapi perlu kapitalisasi
kode3 = "  AbC-123x567-Z  "  # Ada karakter non-digit di bagian angka
kode4 = "DEF-123456-G"  # Bagian angka kurang dari 7 digit
kode5 = "GHI12345678J"  # Tidak ada tanda hubung
kode6 = "   jkl-7654321-9   "  # Karakter terakhir bukan huruf

print(f"'{kode1}' -> '{validasi_kode_produk(kode1)}'")
print(f"'{kode2}' -> '{validasi_kode_produk(kode2)}'")
print(f"'{kode3}' -> '{validasi_kode_produk(kode3)}'")
print(f"'{kode4}' -> '{validasi_kode_produk(kode4)}'")
print(f"'{kode5}' -> '{validasi_kode_produk(kode5)}'")
print(f"'{kode6}' -> '{validasi_kode_produk(kode6)}'")
