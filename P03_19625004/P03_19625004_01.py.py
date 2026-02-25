# Program AnalisisPolaTidur

# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 31 Oktober 2025
# Deskripsi : Program untuk membantu Nona Sal menganalisis pola tidur

# Input
jam_tidur = [0, 0, 0, 0, 0, 0, 0]
total_7hari = 0
i = 0
print("Masukkan jam tidur untuk 7 hari:")
for i in range (7):
    jam_tidur[i] = float(input(f"Hari ke-{i+1}: "))

# Proses
total_7hari += jam_tidur[i]
rata_7hari = round((total_7hari)/7,2)

min_tidur = jam_tidur[0]
hari_min = 1

for i in range (1, 7):
    if jam_tidur[i] < min_tidur:
        min_tidur = jam_tidur[i]
        hari_min = i + 1

streak = 0
sleep_debt = False
start = 0
finish = 0

for i in range(7):
    if jam_tidur[i] < 6:
        streak += 1
    else:
        streak = 0

    if streak == 3 and sleep_debt == False:
        sleep_debt = True
        start = i - 1
        finish = i + 1

# Output
print(f"Rata-rata jam tidur: {rata_7hari} jam per hari")
print(f"Jam tidur paling sedikit: {min_tidur} jam (Hari ke-{hari_min})")
if sleep_debt == False:
    print("Pola tidur sehat! Tidak ada sleep debt streak.")
else:
    print(f"PERINGATAN : Ditemukan sleep debt streak! Hari ke-{start} sampai ke-{finish} tidur kurang dari 6 jam berturut-turut.")