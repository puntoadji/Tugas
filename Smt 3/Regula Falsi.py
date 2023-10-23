import numpy as np

def f(x) :
    return x * x - np.exp(x) + 1

def regulaFalsi (f,a,b, tol = 1e-7):
    iterasi = 0
    roots = [] #untuk menyimpan akar
    while True :
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        roots.append(c) #untuk menambahkan akar dalam array akar

        if abs(f(c)) < tol :
            return roots
        
        if f(c) * f(a) < 0 :
            b = c
        else : 
            a = c

            iterasi += 1
    
a = float(input("Masukkan Batas Bawah(a) : "))
b = float(input("Masukkan Batas Atas(b) : "))

roots = (regulaFalsi(f, a, b))

if roots is not None :
    print('Akar yang ditemukan : ')
    for i, root in enumerate(roots):
        print(f'Iterasi- {i + 1}: {root}')

else : 
    print('Hasil Tidak Konvergen') 
