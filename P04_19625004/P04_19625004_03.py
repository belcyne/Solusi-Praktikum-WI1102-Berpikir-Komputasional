# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 14 November 2025
# Deskripsi : Program untuk membantu Tuan Vin bisa menentukan hari ke-n sebelum atau setelah hari tertentu pada penanggalan Martian

# Kamus
# nama_bulan, jumlah_hari = array
# hari, bulan, tahun, n = integer
# tanggal, fungsi = string
# return, i = integer
# total, hari_ke, global_hari = integer
# print_hari, print_bulan, print_tahun = integer

# Database penanggalan Martian
nama_bulan = ["Solan", "Lunara", "Terran", "Pyron", "Aquen", "Zephyr", "Umbra", "Lumen", "Astra", "Dimensi"]
jumlah_hari = [37, 38, 39, 40, 39, 36, 41, 36, 37]

# Input
tanggal = input("Masukkan tanggal: ").split()          #Menggunakan Split agar hari-bulan-tahun pada tanggal dapat didefinisikan. Jika tidak pakai split, maka nilai tanggal menjadi satu string penuh.
hari = int(tanggal[0])                                 #Mendefinisikan tanggal yang displit menjadi integer
bulan = int(tanggal[1])
tahun = int(tanggal[2])

fungsi = input("Masukkan fungsi: ")
n = int(input("Masukkan n: "))

def total_setahun(tahun):
    return 343 + (tahun % 5)                           #Jumlah hari berubah tiap tahun berdasarkan siklus 5 tahun

def ke_hari_global(hari, bulan, tahun):                #Variabel total penghitung hari
    total = 0

    for i in range(1, tahun):
        total += total_setahun(i)

    if bulan == 10:
        total += 343 + hari
    else:
        for i in range(bulan - 1):
            total += jumlah_hari[i]
        total += hari
    
    return total

def dari_hari_global(hari_ke):
    tahun = 1                                       #Mulai mengecek dari tahun 1

    while hari_ke > total_setahun(tahun):
        hari_ke -= total_setahun(tahun)
        tahun += 1
    
    if hari_ke > 343:
        return hari_ke - 343, 10, tahun
    
    bulan = 1
    i = 0
    while i < 9 and hari_ke > jumlah_hari[i]:
        hari_ke -= jumlah_hari[i]
        bulan += 1
        i += 1
    
    hari = hari_ke
    return hari, bulan, tahun

def sebelum(hari, bulan, tahun, n):                #Menghitung tanggal n hari sebelum tanggal tertentu
    global_hari = ke_hari_global(hari, bulan, tahun)
    global_hari -= n
    if global_hari < 1:
        global_hari = 1
    return dari_hari_global(global_hari)

def setelah(hari, bulan, tahun, n):                #Menghitung tanggal n hari setelah tanggal tertentu
    global_hari = ke_hari_global(hari, bulan, tahun)
    global_hari += n
    return dari_hari_global(global_hari)


# Output
if fungsi == "sebelum":
    print_hari, print_bulan, print_tahun = sebelum(hari, bulan, tahun, n)
    print(f"{n} hari sebelumnya adalah {print_hari} {nama_bulan[print_bulan-1]} {print_tahun}")
elif fungsi == "setelah":
    print_hari, print_bulan, print_tahun = setelah(hari, bulan, tahun, n)
    print(f"{n} hari setelahnya adalah {print_hari} {nama_bulan[print_bulan-1]} {print_tahun}")