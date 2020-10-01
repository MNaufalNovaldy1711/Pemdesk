def maxMin():
    banyak = int(input("Berapa banyak angka yang ingin dimasukkan: "))
    posisi = []
    first=0
    while first <= banyak-1:
        posisi.append(int(input("Angka ke-{0}: ".format(first))))
        first+=1
    posisi.sort()
    print(posisi)

    print("\nMinimal: ", posisi[0])
    print("Maximal: ", posisi[-1])
maxMin() 
