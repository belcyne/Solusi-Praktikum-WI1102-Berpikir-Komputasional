# Program MengecekKelayakanDonorDarah

# Identitas
# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 17 Oktober 2025
# Deskripsi : Program untuk membantu Nona Sal mengecek kelayakan donor darah

# Kamus
# usia, berat_badan : int
# sudah_makan, donor_terakhir : bool

# Input
usia = int(input("Masukkan usia: "))  # Input usia
berat_badan = int(input("Masukkan berat badan (kg): "))  # Input berat badan

sudah_makan_input = input("Sudah makan dalam 4 jam terakhir? (Ya/Tidak): ")
sudah_makan = True if sudah_makan_input == "Ya" else False

donor_terakhir_input = input("Donor dalam 2 bulan terakhir? (Ya/Tidak): ")
donor_terakhir = True if donor_terakhir_input == "Tidak" else False

# Pengecekkan kondisi & Output
if not (17 <= usia <= 60):
    print("Tidak layak donor. Alasan: Usia tidak memenuhi syarat.")
elif berat_badan < 45:
    print("Tidak layak donor. Alasan: Berat badan tidak memenuhi syarat.")
elif not sudah_makan:
    print("Tidak layak donor. Alasan: Belum makan.")
elif not donor_terakhir:
    print("Tidak layak donor. Alasan: Sudah donor darah dalam 2 bulan terakhir.")

else:
    if berat_badan > 70:
        print("Layak donor darah. Jenis donor: Donor double (disarankan).")
    else:
        print("Layak donor darah. Jenis donor: Donor reguler.")