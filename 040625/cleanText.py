# Normalisasi data


def normalisasi_komentar(komentar):
    komentar = komentar.strip().lower()
    komentar_bersih = komentar.replace("bagus", "baik").replace("cepat", "responsif")
    return komentar_bersih


komentar = " Produk Ini Sangat BAGUS. pelayanannya sangat cepat dan RAMAH! saya suka sekali.        "

komentar_normal = normalisasi_komentar(komentar)
print("Komentar Asli:", komentar)
print("Komentar Normalisasi:", komentar_normal)
