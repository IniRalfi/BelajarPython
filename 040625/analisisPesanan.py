import questionary


def analisis_pesanan(data_pesanan_mentah):
    data_normalisasi = []
    for item_mentah in data_pesanan_mentah:
        data_normalisasi.append(item_mentah.lower())

    data_pesanan_unik = list(set(data_normalisasi))

    jumlah_pesanan_unik = len(data_pesanan_unik)
    barang_paling_banyak = ""
    frekuensi_barang_terbanyak = 0

    for item_unik in data_pesanan_unik:
        jumlah_kemunculan = data_normalisasi.count(item_unik)
        if jumlah_kemunculan > frekuensi_barang_terbanyak:
            frekuensi_barang_terbanyak = jumlah_kemunculan
            barang_paling_banyak = item_unik

    daftar_pesanan_unik_terurut = sorted(data_pesanan_unik)

    item_dicari = (
        questionary.text("Masukkan nama barang yang ingin dicari: ", qmark="🔍 ")
        .ask()
        .strip()
        .lower()
    )
    apakah_ada_item = item_dicari in data_pesanan_unik

    return {
        "jumlah_pesanan_unik": jumlah_pesanan_unik,
        "barang_paling_banyak": barang_paling_banyak,
        "frekuensi_barang_terbanyak": frekuensi_barang_terbanyak,
        "daftar_pesanan_unik_terurut": daftar_pesanan_unik_terurut,
        "apakah_ada_item": apakah_ada_item,
    }


data_pesanan_mentah = [
    "kaos merah L",
    "celana biru S",
    "jaket hitam M",
    "kaos merah L",
    "topi hijau ALLSIZE",
    "kaos PUTIH M",
    "celana biru S",
    "sepatu coklat 42",
    "kaos merah L",
    "JAKET HITAM M",
]


hasil_analisis = analisis_pesanan(data_pesanan_mentah)
print(hasil_analisis)
