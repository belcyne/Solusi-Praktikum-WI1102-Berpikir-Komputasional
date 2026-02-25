# Program MengecekPersegiDari4Titik

# Identitas
# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 17 Oktober 2025
# Deskripsi : Program untuk membantu Tuan Mik mencari tahu apakah 4 titik koordinat dapat membentuk persegi atau tidak 

# Kamus
# x1, x2, x3, x4 : int
# y1, y2, y3, y4 : int
# x, y : int
# x3_ideal, y3_ideal : int
# x4_ideal, y4_ideal : int

# Input
x1, y1 = map(int, input("Titik 1: ").split(', '))
x2, y2 = map(int, input("Titik 2: ").split(', '))
x3, y3 = map(int, input("Titik 3: ").split(', '))
x4, y4 = map(int, input("Titik 4: ").split(', '))

# Proses
x = x2 - x1           # Menghitung selisih jarak di koordinat x antara titik 1 dan 2
y = y2 - y1           # Menghitung selisih jarak di koordinat y antara titik 1 dan 2

x3_ideal = x2 - y     # x3 & y3 ideal diperoleh dari pergeseran tegak lurus terhadap titik 2
y3_ideal = y2 + x
x4_ideal = x1 - y     # x4 & y4 ideal diperoleh dari pergeseran tegak lurus terhadap titik 1
y4_ideal = y1 + x

# Pengecekkan kondisi & Output
if (x3_ideal == x3 and y3_ideal == y3 and x4_ideal == x4 and y4_ideal == y4):
    print("Keempat titik tersebut membentuk Persegi")
else:
    print("Keempat titik tersebut tidak membentuk Persegi")