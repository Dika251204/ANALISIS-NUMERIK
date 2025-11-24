## METODE LAGRANGE##
import numpy as np
import matplotlib.pyplot as plt
# metode Interpolasi Lagrange
# Data titik
x = np.array([1.0, 2.0, 3.0])
y = np.array([3.0, 8.0, 15.0])
xp = 2.5

# Fungsi Interpolasi Lagrange
def lagrange(x, y, xp):
    p = 0.0
    n = len(x)
    for i in range(n):
        L = 1.0
        for j in range(n):
            if j != i:
                L *= (xp - x[j]) / (x[i] - x[j])
        p += y[i] * L
    return p

# hitung nilai f(2.5)
L_value = lagrange(x, y, xp)
print("Hasil Lagrange pada x=2.5 adalah: ", L_value)

# Membuat grafik
plt.figure(figsize=(8, 5))
plt.scatter(x, y, label='Data')
plt.plot(x, y, label='Grafik')
plt.scatter(xp, L_value, color='red', label='f(2.5)')
plt.title("Grafik Interpolasi Lagrange")
plt.legend()
plt.grid(True)
plt.show()
#======================================================================================================================================================================================================#
## METODE NEWTON##
import numpy as np
# metode interpolasi Newton
# Data titik
x = np.array([1.0, 2.0, 3.0])
y = np.array([3.0, 8.0, 15.0])
xp = 2.5

# Fungsi menghitung tabel divided difference
def divided_difference(x, y):
    n = len(x)
    coef = np.copy(y)

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])

    return coef

# Fungsi menghitung nilai interpolasi Newton
def newton_interpolation(x, coef, xp):
    n = len(x)
    p = coef[n-1]

    for i in range(n-2, -1, -1):
        p = p * (xp - x[i]) + coef[i]

    return p

# Hitung koefisien Newton
coef = divided_difference(x, y)

# Hitung nilai di xp
hasil = newton_interpolation(x, coef, xp)

print("Hasil Interpolasi Newton pada x = 2.5 adalah:", hasil)

# Membuat Grafik
plt.figure(figsize=(8, 5))
plt.scatter(x, y, label='Data')
plt.plot(x, y, label='Grafik')
plt.scatter(xp, L_value, color='red', label='f(2.5)')
plt.title("Grafik Interpolasi Newton")
plt.legend()
plt.grid(True)
plt.show()
