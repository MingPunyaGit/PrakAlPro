matkul=1
bannyak_matkul = int(input("Jumlah Mata Kuliah:"))
nilai_matkul = 0
list_nilai=[]
while matkul<bannyak_matkul+1:
    print(f"Nilai Mata Kuliah {matkul}:",end=" ")
    matkul=matkul+1
    nilai=input("")
    nilai.upper()
    if nilai=="a":
        
        nilai_matkul=nilai_matkul+4
    elif nilai=="b":
       
        nilai_matkul=nilai_matkul+3
    elif nilai=="c":
       
        nilai_matkul=nilai_matkul+2
    elif nilai=="d":
       
        nilai_matkul=nilai_matkul+1
        
print(f"Nilai IPS anda semester ini {nilai_matkul/bannyak_matkul:.2f}")