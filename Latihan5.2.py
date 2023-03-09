def ganjil(atas,bawah):
    if bawah < atas :
        bawah, atas = atas, bawah
    for i in range(atas, bawah+1):
        if i % 2 != 0:
            atas = 1
        
        if i % 2 !=0:
            if i == atas - 1:
                print(f"{i}.")
            else:
                print(i, end=",")

ganjil (10, 30)
ganjil (82, 97)