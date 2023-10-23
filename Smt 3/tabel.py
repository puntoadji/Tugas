import numpy as np

def f(x) :
    return x * x - np.exp(x) + 1


def  tabel ( n = 10, tol = 1e-7):
    a = float(input("Masukkan Batas Bawah(a) : "))
    b = float(input("Masukkan Batas Atas(b) : "))
    h = (b - a ) / n 
    selesai = False

    while not selesai:
        print(h, '\n')
        hasil = 0
        b_new = 0
        a_new = 0 
        e = None

        for i in range (n+1):
            x = a + i * h
            #x_lama = a + (i-1) * h
            formatted_x = "{:.7f}".format(x)
            formatted_fx = "{:.7f}".format(f(x))
            print(f"{formatted_x}\t\t{formatted_fx}\t")

            if f(x) == 0:
                print(f"Akar penyelesaian adalah : {x}")
                selesai = True
            

print(tabel())