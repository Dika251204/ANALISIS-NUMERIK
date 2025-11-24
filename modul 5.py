##metode regresi
import numpy as np
x = np.array([10, 20, 30, 40]) # aplikasi (MB)
y = np.array([2.5, 4, 5, 6.5]) # waktu muat (detik)

#hitung parameter regresi
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

#rumus slope (b1) dan intercept (b0)
b1 = np.sum((x  - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
b0 = y_mean - b1 * x_mean

#cetak hasil
print("persamaan regresi: y  ={:.4f}x + {:.4f}". format(b1, b0))

#contoh  perrrredicsi (misalnya 25 MB)
X_prediction = 25
y_prediction = b0 + b1 * X_prediction
print("waktu muat untuk ukuran 25MB =",y_prediction)


