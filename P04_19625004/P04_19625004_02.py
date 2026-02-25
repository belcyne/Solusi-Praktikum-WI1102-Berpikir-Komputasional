# NIM/Nama  : 19625004/Christabelcyne Costan
# Tanggal   : 14 November 2025
# Deskripsi : Program untuk menentukan apakah suatu kata tergolong dalam Bahasa Vin atau bukan

# Kamus
# kata = string
# vokal, huruf = string
# vokal_ada, konsonan_ada, bersebelahan, palindrom, sama = boolean

# Input
kata = str(input("Masukkan kata: "))

def cek_vokal(kata):            #Definisi fungsi mengecek adanya vokal atau tidak
    vokal = "aiueoAIUEO"        #Deklarasi vokal dalam bentuk string
    vokal_ada = False           #Inisiasi boolean penanda vokal di awal
    for huruf in kata:          #Cek setiap huruf pada kata
        if huruf in vokal:
            vokal_ada = True
    return vokal_ada

def cek_konsonan(kata):        #Definisi fungsi mengecek adanya konsonan atau tidak
    vokal = "aiueoAIUEO"
    konsonan_ada = False       #Inisiasi boolean penanda konsonan di awal
    for huruf in kata:         #Cek setiap huruf pada kata
        if huruf not in vokal: #Persyaratan huruf konsonan menjadi ada
            konsonan_ada = True
    return konsonan_ada

def cek_bersebelahan(kata):    #Definisi fungsi mengecek apakah ada dua huruf berurutan yang sama
    bersebelahan = False
    for i in range(len(kata)-1):
        if kata[i] == kata[i+1]:
            bersebelahan = True
    return bersebelahan

def cek_palindrom(kata):      #Definisi fungsi mengecek apakah dibaca sama dari depan atau belakang
    palindrom = False
    sama = True
    bagi_kata = len(kata)//2
    for i in range(bagi_kata):
        kiri = kata[i]
        kanan = kata[len(kata)-1-i]

        if kiri != kanan:
            sama = False
        if sama:
            palindrom = True
    
    return palindrom

#Panggil fungsi awal dan simpan hasil
vokal_ada = cek_vokal(kata)
konsonan_ada = cek_konsonan(kata)
bersebelahan = cek_bersebelahan(kata)
palindrom = cek_palindrom(kata)


# Output
if vokal_ada and konsonan_ada and not bersebelahan and palindrom:
    print("Kata tersebut termasuk dalam Bahasa Vin")
else:
    print("Kata tersebut tidak termasuk dalam Bahasa Vin")