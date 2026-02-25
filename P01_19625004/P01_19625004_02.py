# Program UangUntukMembeliTiket

# Identitas
# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 3 Oktober 2025
# Deskripsi : Program untuk membantu Nona Deb menghitung berapa banyak uang yang harus dikumpulkan untuk membeli tiket

# Kamus
# uang_sekarang, harga_tiket : float
# jumlah_tiket : int
# harga_diskon : float
# harga_total_pajak : float
# uang diperlukan : float


# Input
uang_sekarang = float(input("Uang Nona Deb sekarang:"))
harga_tiket = float(input("Harga tiket:"))
jumlah_tiket = int(input("Jumlah tiket yang dibeli:"))

# Perhitungan
harga_diskon = harga_tiket*(1-0.05)
harga_total_pajak = (harga_diskon*jumlah_tiket)*(1+0.1)
uang_diperlukan = round(harga_total_pajak - uang_sekarang,0)

# Output
print(f"Nona Deb perlu mengumpulkan uang sebesar {uang_diperlukan}")
