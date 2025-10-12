#step awal  input nilai
x_awal = 10000.0
# step  2
x_lanjutannnyaA =  0.0001
#Step 3: lakukan perulangan 5 kali
for _ in range(5):
    x_awal += x_lanjutannnyaA
print("hasil penjumlahan algoritma dari", x_awal)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

x_awalB =0.0001
total=0.0
x_lanjutannyaB = 10000.0
for _ in range(5):
  total += x_awal
x_awalB += x_lanjutannyaB
print("hasil penjumlahannya adalah:",x_awalB)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
ini tugas laporan pertama analisis numerik==>

    # Nilai sebenarnya
N_sebenarnya = 100001.0

# Algoritma 1
#step 1: Input nilai awal adalah angka yang paling besar
x_awalA = 100000.0
#Step 2: input nilai selanjutnya adalah angka yang kecil
x_selanjutnnyaA = 0.00001
# Step 3: Melakukan perulangan
for _ in range (100000):
  x_awal1 += x_selanjutnnyaA
# Cetak hasil

# Algoritma 2
total = 0
#step 1: Input nilai awal adalah angka yang paling kecil
x_awalB  = 0.00001
#Step 2: input nilai selanjutnya adalah angka yang besar
x_selanjutnnyaB = 100000.0
# Step 3: Melakukan perulangan
for _ in range (100000):
  total += x_awalB
total += x_selanjutnnyaB
# Cetak hasil
print ("Nilai yang sebenarnya       :",N_sebenarnya)
print ("Hasil algoritma A adalah    :",x_awalA)
print ("Hasil algoritma B adalah    :",total)
print ("Galat Algoritma A           :",x_awalA-N_sebenarnya)
print ("Galat Algoritma B           :",totaA-N_sebenarnya)
print ("Perbedaan A dan B           :",x_awalA-total)

