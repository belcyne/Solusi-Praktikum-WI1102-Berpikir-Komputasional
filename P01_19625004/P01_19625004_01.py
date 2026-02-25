# Program MenghitungUkuranFileKompresi

# Identitas
# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 3 Oktober 2025
# Deskripsi : Program untuk membantu Nona Sal menghitung ukuran file setelah dikompresi

# Kamus
# w, h, d, r : int
# ukuran_file_1 : float
# ukuran_file_2 : float

# Input
w = int(input("Masukkan lebar gambar (pixel):"))
h = int(input("Masukkan tinggi gambar (pixel):"))
d = int(input("Masukkan kedalaman warna (pixel):"))
r = int(input("Masukkan kompresi (persen):"))

# Perhitungan
ukuran_file_1 = (w*h*d)/(8*1000000)
ukuran_file_2 = round(ukuran_file_1*(r/100),2)

# Output
print(f"Ukuran file gambar setelah kompresi adalah {ukuran_file_2} MB")