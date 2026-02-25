# Program LacakStatusLampu

# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 31 Oktober 2025
# Deskripsi : Program untuk membantu Tuan Mik untuk melacak status semua lampu

# Input
jumlah_saklar = int(input("Jumlah lampu dan saklar: "))
lampu = [False]*jumlah_saklar # False = mati, True = nyala

# Proses
done = False
while done == False:
    saklar = int(input("Masukkan nomor saklar yang ditekan: "))

    if saklar == -1:
        done = True
    elif saklar >= 1 and saklar <= jumlah_saklar:
        for i in range (saklar - 1, jumlah_saklar, saklar):
            if lampu[i] == False:
                lampu[i] = True
            else:
                lampu[i] = False

# Output
print("Status lampu:")
for i in range (jumlah_saklar):
    if lampu[i] == True:
        print(f"Lampu {i+1}: Menyala")
    else:
        print(f"Lampu {i+1}: Mati")