#step awal  input nilai
x_awal = 10000.0
# step  2
x_lanjutannnya1 =  0.0001
#Step 3: lakukan perulangan 5 kali
for _ in range(5):
    x_awal += x_lanjutannnya1
print("hasil penjumlahan algoritma dari", x_awal)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

x_awal2 =0.0001
total=0.0
x_lanjutannya2 = 10000.0
for _ in range(5):
  total += x_awal
x_awal2 += x_lanjutannya2
print("hasil penjumlahannya adalah:",x_awal2)
