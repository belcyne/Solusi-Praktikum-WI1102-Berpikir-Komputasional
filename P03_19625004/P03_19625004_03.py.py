# Program MenentukanPemenangPermainan

# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 31 Oktober 2025
# Deskripsi : Program untuk membantu Nona Sal menentukan pemenang dari permainan BINGO yang dimodifikasi

# Input
n = int(input("Masukkan besar angka n: "))

list_deb = [int(input(f"Masukkan angka ke-{i+1} Nona Deb: ")) for i in range(n)]
list_mik = [int(input(f"Masukkan angka ke-{i+1} Tuan Mik: ")) for i in range(n)]
list_vin = [int(input(f"Masukkan angka ke-{i+1} Nona Vin: ")) for i in range(n)]

aktif_list_deb = [True]*n
aktif_list_mik = [True]*n
aktif_list_vin = [True]*n

done = False
status_deb = status_mik = status_vin = False

# Proses
while not done:
    angka = int(input("Masukkan angka yang dipanggil: "))

    if angka < 0:
        done = True
    else:
        min_deb = min_mik = min_vin = float('inf')
        i_deb = i_mik = i_vin = -1

        for i in range(n):
            if aktif_list_deb[i]:
                selisih = abs(angka - list_deb[i])
                if selisih < min_deb:
                    min_deb = selisih
                    i_deb = i

        for i in range(n):
            if aktif_list_mik[i]:
                selisih = abs(angka - list_mik[i])
                if selisih < min_mik:
                    min_mik = selisih
                    i_mik = i

        for i in range(n):
            if aktif_list_vin[i]:
                selisih = abs(angka - list_vin[i])
                if selisih < min_vin:
                    min_vin = selisih
                    i_vin = i

        if min_deb <= min_mik and min_deb <= min_vin:
            aktif_list_deb[i_deb] = False
        elif min_mik <= min_deb and min_mik <= min_vin:
            aktif_list_mik[i_mik] = False
        else:
            aktif_list_vin[i_vin] = False

        sisa_deb = sum(aktif_list_deb)
        sisa_mik = sum(aktif_list_mik)
        sisa_vin = sum(aktif_list_vin)

        if sisa_deb == 0 or sisa_mik == 0 or sisa_vin == 0:
            done = True
            status_deb = (sisa_deb == 0)
            status_mik = (sisa_mik == 0)
            status_vin = (sisa_vin == 0)

# Output
pemenang = []
if status_deb:
    pemenang.append("Nona Deb")
if status_mik:
    pemenang.append("Tuan Mik")
if status_vin:
    pemenang.append("Tuan Vin")

print("\nPemenang dari permainan ini adalah:", ", ".join(pemenang))