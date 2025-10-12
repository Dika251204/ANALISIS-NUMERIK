# Menyelesaikan Persamaan Non Linear x^3+x^2-3x-3 dengan Metode bisection 

# Mengimport library yang digunakan --> PR
import matplotlib.pyplot as plt
from time import perf_counter as pc
import numpy as np

# Mendefinisikan fungsi  
def f(x): 
    return x**3 + x**2 - 3*x - 3
 
# Metode Bisection 
def bisection(a, b, tol=1e-6, max_iter=100): 
    fa, fb = f(a), f(b) 
    if fa * fb > 0: 
        raise ValueError("f(a) dan f(b) harus berlawanan tanda. Pilih interval lain.") 
    history = [] 
    start = pc() 
    for i in range(1, max_iter+1): 
        c = (a + b) / 2.0 
        fc = f(c) 
        history.append((i, a, b, c, fc)) 
        print(f"Iter {i:2d}: a={a:.8f}, b={b:.8f}, c={c:.8f}, f(c)={fc:.8e}") 
        if abs(fc) < tol or (b - a)/2.0 < tol: 
            end = pc() 
            print(f"\nAkar diperkirakan di x = {c:.12f}") 
            print(f"f(c) = {fc:.12e}") 
            print(f"Iterasi = {i}, waktu = {(end-start):.6f} s") 
            return c, history 
        if fa * fc < 0: 
            b = c 
            fb = fc 
        else: 
            a = c 
            fa = fc 
    end = pc() 
    print("\nMetode tidak konvergen dalam batas iterasi.") 
    return c, history 

# Menjalankan metode pada interval [1, 2] 
akar, hist = bisection(1, 2, tol=1e-6, max_iter=100) 
 
# Visualisasi fungsi dan titik-titik mid tiap iterasi --> PR
x_vals = np.linspace(-3, 3, 200)
y_vals = f(x_vals)
plt.figure(figsize=(6,4))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='gray', linestyle='--')
plt.scatter([h[3] for h in hist], [h[4] for h in hist], color='red', label='Iterasi (c)')
plt.title("Visualisasi Metode Bisection")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

# Menampilkan ringkasan akhir --> PR
print("\n Ringkasan Akhir Metode Bisection")
print(f"Akar akhir ≈ {akar:.8f}")
print(f"Jumlah iterasi: {len(hist)}")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Menyelesaikan Persamaan Non Linear x^3+x^2-3x-3 dengan Metode Newton-Raphson 
# Mengimport library yang digunakan --> PR 
import matplotlib.pyplot as plt
from time import perf_counter as pc
import numpy as np

# Mendefinisikan fungsi dan turunannya 
def f(x): 
    return x**3 + x**2 - 3*x - 3 
 
def f_prime(x): 
    return 3*x**2 + 2*x - 3 
 
# Metode Newton-Raphson 
def newton_raphson(x0, tol=1e-6, max_iter=100): 
    print("Iterasi\t   x\t\t   f(x)") 
    nilai_x = [] 
    start = pc()
    for i in range(max_iter): 
        fx = f(x0) 
        fpx = f_prime(x0) 
        if fpx == 0: 
            print("Turunan nol, metode berhenti.") 
            break 
        x1 = x0 - fx / fpx 
        print(f"{i+1}\t{x0:.6f}\t{fx:.6f}") 
        nilai_x.append(x1) 
        if abs(x1 - x0) < tol: 
            end = pc()
            print("\nAkar ditemukan pada x =", x1) 
            print(f"Waktu eksekusi = {(end-start):.6f} s")
            return x1, nilai_x 
        x0 = x1 
    print("\nMetode tidak konvergen.") 
    return None, nilai_x 
 
# Menjalankan metode dengan tebakan awal 
akar, nilai_x = newton_raphson(3) 
 
# Visualisasi hasil --> PR 
x_vals = np.linspace(-3, 3, 200)
y_vals = f(x_vals)
plt.figure(figsize=(6,4))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='gray', linestyle='--')
plt.scatter(nilai_x, [f(x) for x in nilai_x], color='orange', label='Titik iterasi')
plt.title("Visualisasi Metode Newton-Raphson")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Menyelesaikan Persamaan Non Linear x^3 + x^2 - 3x - 3 dengan Metode Secant

# Mengimport library yang digunakan
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter as pc

# Mendefinisikan fungsi
def f(x):
    return x**3 + x**2 - 3*x - 3

# Metode Secant
def secant(x0, x1, tol=1e-6, max_iter=100):
    print("Iterasi\t   x0\t\t   x1\t\t   x2\t\tf(x2)")
    nilai_x = []
    start = pc()
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)

        if f1 - f0 == 0:
            print("Error: karena pembagian dengan nol")
            break

        # Rumus metode Secant
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)
        print(f"{i+1}\t{x0:.6f}\t{x1:.6f}\t{x2:.6f}\t{f2:.6f}")

        nilai_x.append(x2)

        if abs(f2) < tol:
            end = pc()
            print(f"\nAkar ditemukan pada x = {x2:.8f}")
            print(f"Iterasi = {i+1}, waktu = {(end-start):.6f} s")
            return x2, nilai_x

        # Perbarui nilai
        x0, x1 = x1, x2

    print("\nMetode tidak konvergen.")
    return None, nilai_x

# Menjalankan metode dengan tebakan awal
akar, nilai_x = secant(2, 3)

# Visualisasi hasil
x_vals = np.linspace(-3, 3, 200)
y_vals = f(x_vals)
plt.figure(figsize=(7,5))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='gray', linestyle='--')
plt.scatter(nilai_x, [f(x) for x in nilai_x], color='orange', label='Titik iterasi')
plt.title("Visualisasi Metode Secant")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
