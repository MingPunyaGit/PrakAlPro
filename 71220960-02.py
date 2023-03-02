from datetime import date

def selisih_hari(tanggal1,bulan1,tanggal2,bulan2):
        



    date1 = date(2023, bulan1, tanggal1)
    date2 = date(2023, bulan2, tanggal2)

    delta = date1 - date2

    print("Selisih hari antara tanggal {0} dan tanggal {1} adalah {2} hari".format(date1, date2, delta.days))

tanggal1 = int(input("Masukan tanggal pertama: "))
bulan1 = int(input("Masukan bulan pertama: "))
tanggal2 = int(input("Masukan tanggal kedua: "))
bulan2 = int(input("Masukan bulan kedua: "))    

selisih_hari(tanggal1,bulan1,tanggal2,bulan2)