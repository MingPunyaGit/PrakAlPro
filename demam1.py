# suhu = float(input("Masukan Suhu Badan: "))
# if suhu <= 32:
#     print("Meniggal")
# elif suhu  < 36: 
#     print("Bahaya hiportemia")
# elif suhu < 38:
#     print("Normal")
# elif suhu < 40:
#     print("demam")
# else :
#      print ("Meninggal")


#multiples code 
# multiples = int(input("Masukan Sebuah bilangan: "))

# satuan = multiples % 10
# if satuan == 0 or satuan == 1 or satuan == 2 or satuan == 8 or satuan == 9:
#     print("true")
# else :
#     print("fales")


# ubin1 = int(input("Masukan jumlah ubin 1: "))
# ubin5 = int(input("Masukan Jumlah Ubin 2: "))
# panjang = int(input("Masukan Panjang lantainya : "))

# if panjang <= (ubin1 *  + ubin5 * 5):
#     if (panjang // 5) <= ubin5 and (panjang % 5 ==0):
#         print("bisa")
#     elif (panjang % 5) <= ubin1:
#         print("bisa")
#     else:
#         print("tidak bisa")
# else:
#     print("Tidak Bisa")



# nama1 = str(input('Masukan nama: '))
# nama2 = str(input('Masukan nama: '))
# nama3 = str(input('Masukan nama: ')) 
# nama = [nama1,nama2,nama3]
# terpanajng = ''
# for x in nama : 
#     if len(x) > len(terpanajng):
#         terpanjang = x 
#         print(x)


a = int(input('Masukan a: '))
b = int(input('Masukan b: '))
c = int(input('Masukan c: '))

total =0 

if a != b != c:
    total = a + b + c 
    print(total)

elif a == b and a == c and b == c:
    total = 0
elif a == b:
    total = c
elif a == c:
    total = b
else:
    total = a

print(total)