# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 14 November 2025
# Deskripsi : Program untuk membantu Nona Sal menghitung hasil penukaran koin dan bonus yang didapat saat menukar ke goblin yang tidak pandai berhitung

# Kamus
# perunggu = integer
# perak, perunggu_sisa, emas, perak_sisa, bonus_emas = integer

# Input
perunggu = int(input("Masukkan jumlah koin perunggu: "))

# Fungsi perhitungan
def hitung_koin(perunggu):
    perak = perunggu // 10
    perunggu_sisa = perunggu % 10

    emas = perak // 10
    perak_sisa = perak % 10

    bonus_emas = emas // 5
    emas += bonus_emas

    return emas, perak_sisa, perunggu_sisa

# Fungsi output
def tampilkan_hasil(perunggu, emas, perak_sisa, perunggu_sisa):
    if perunggu < 10:
        print("Koin Nona Sal tidak cukup untuk ditukarkan.")
    else:
        if perunggu_sisa > 0:
            print(f"Nona Sal akan mendapatkan {emas} emas, {perak_sisa} perak, dan {perunggu_sisa} perunggu dari hasil penukaran.")
        else:
            if perak_sisa > 0:
                print(f"Nona Sal akan mendapatkan {emas} emas dan {perak_sisa} perak dari hasil penukaran.")
            else:
                print(f"Nona Sal akan mendapatkan {emas} emas dari hasil penukaran.")

# Pemanggilan fungsi
emas, perak_sisa, perunggu_sisa = hitung_koin(perunggu)
tampilkan_hasil(perunggu, emas, perak_sisa, perunggu_sisa)