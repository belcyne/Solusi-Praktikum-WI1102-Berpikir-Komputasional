# Program MengecekPemenangPeperanganVideoGim

# Identitas
# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 17 Oktober 2025
# Deskripsi : Program untuk membantu Tuan Vin menentukan pemenang dari peperangan di video gim 

# Kamus
# moral_pasukan : float
# jumlah_prajurit_wei, jarak_tempuh_wei : int
# jumlah_prajurit_wu, jarak_tempuh_wu : int
# pp_awal_wei, pp_awal_wu : float
# pp_wei, pp_wu : float

# Input
moral_pasukan = float(input("Masukkan moral pasukan: "))
jumlah_prajurit_wei = int(input("Masukkan banyak prajurit kerajaan Wei: "))
jarak_tempuh_wei = int(input("Masukkan jarak tempuh kerajaan Wei: "))
jumlah_prajurit_wu = int(input("Masukkan banyak prajurit kerajaan Wu: "))
jarak_tempuh_wu = int(input("Masukkan jarak tempuh kerajaan Wu: "))

# Proses
pp_awal_wei = (jumlah_prajurit_wei*(moral_pasukan + 0.05))/jarak_tempuh_wei
pp_awal_wu = (jumlah_prajurit_wu*moral_pasukan)/jarak_tempuh_wu

pp_wei = pp_awal_wei
pp_wu = pp_awal_wu

if (jarak_tempuh_wei < jarak_tempuh_wu):
    pp_wei += 800

if (pp_awal_wei > pp_awal_wu):
    pp_wu += 1500

# Pengecekkan kondisi & Output
if (pp_wei > pp_wu):
    print(f"Kerajaan Wei menang dari Kerajaan Wu dengan selisih sebesar {pp_wei - pp_wu} PP")
else:
    print(f"Kerajaan Wu menang dari Kerajaan Wei dengan selisih sebesar {pp_wu - pp_wei} PP")