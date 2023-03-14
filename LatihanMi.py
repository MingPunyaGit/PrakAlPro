def pagar_vertikal(n):
    for i in range (1, n+1):
        print("#")
    print()

def pagar_horizontal(n):
    print("Pagar Horizontal")
    for i in range (1, n+1):
        print("#", end="")
    print()

def persegi(n):
    print("Pagar Persegi")
    for baris in range (n):
        for kolom in range(n):
            print("#", end="")
        print()
    print()

def persegi_bolong(n):
    print("Persegi Bolong")
    for baris in range (1, n+1):
        if baris == 1 or baris == n:
            for kolom in range(n):
                print("#", end= "")
        else:
            spasi = n-2 
            print("#", end= "")
            for i in range (sapsi):
                print("", end="")
            print("#", end= "")
        print()
    print()

def huruf_x(n):
    print("Pagar huruf X")
    for baris in range (1, n+1):
        for kolom in range (1, n+1):
            if baris == kolom:
                print("#", end= "")
            elif baris + kolom == n+1:
                print("#", end= "")
            else :
                print("", end="")
        print()
    print()

def huruf_z(n):
    print('Huruf z')
    for i in range (5):
        for j in range(5):
            if i == 0 or i == 4:
                print('#', end='')
            elif i + j == 4:
                print('#', end='')
            else:
                print('', end='')
        print()

def huruf_n(n):
    for i in range (1, n+1):
        for j in range(1, n+1):
            if i == 1 or i == n:
                print('#', end='')
            elif i == j:
                print('#', end='')
            else:
                print('', end='')

def plus(n):
    tengah = 1 + (n//2)
    for baris in range(1, n+1):
        for kolom in range(1, n+1):
            if baris == tengah or kolom == tengah:
                print('#', end='')
            else:
                print('', end='')
        print()
    print()                        

def segitiga_kiri(n):
    for baris in range (1, n+1):
        for kolom in range (1, baris+1):
            print('#', end='')
        print()
    print()

def segitiga_kanan(n):
    for baris in range (1, n+1):
        pagar = baris 
        spasi = n - pagar
    for kolom in range(spasi):
        print('', end='')
    for kolom in range(pagar):
        print('#', end='')
    print()
print()

def segitiga_tengah(n):
    for baris in range(1, n+1):
        spasi = n - baris
        pagar = 2 * bsris - 1 
    for i in range(spasi):
        print('', end='')
    for i in range(pagar):
        print('#', end='')
    print()
print()

def zigzag(n):
    for baris in range (1, n+1):
        for kolom in range(1, n+1):
            if baris % 2 == 1:
                print("#", end="")
            elif baris % 4 == 0:
                print("#", end="")
                break
            else:
                if kolom == n:
                    print("#", end="")
                else:
                    print("", end="")
                    



n = int(input("Masusan n: "))
segitiga_tengah(n)