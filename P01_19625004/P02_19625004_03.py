# Program MenentukanClockCycleDanEfisiensi

#  Identitas
# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 3 Oktober 2025
# Deskripsi : Program untuk membantu Nona Sal menentukan jumlah clock cycle yang dibutuhkan dan efisiensi algoritma dalam operasi per detik

# Kamus
# n, t, o, f : int
# t_total : float
# clock_cycle : float
# efisiensi : float

# Input
n = int(input("Masukkan jumlah operasi:"))
t = int(input("Masukkan waktu per operasi (mikrodetik):"))
o = int(input ("Masukkan overhead (persen):"))
f = int(input("Masukkan frekuensi (GHz):"))

# Perhitungan
t_total = (n*t + n*t*(o/100))
clock_cycle = t_total*f*1000
efisiensi = round(n/(t_total*0.000001),2)

# Output
print(f"Clock cycle yang dihasilkan adalah {clock_cycle} cycle dengan efisiensi {efisiensi} operasi/detik")