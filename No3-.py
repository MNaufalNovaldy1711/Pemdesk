print("PROGRAM BODY MASS INDEX")
berat = float(input("Masukkan Berat Badan Anda(cm): "))
tinggi = float(input("Masukkan Tinggi Badan Anda(kg): "))
a = berat / tinggi**2
print("Hasil Perhitungan: ", a)
if a < 18.5:
    print("Berat Badan Kurang")
elif a <= 22.9:
    print("Berat Badan Normal")
elif a >= 29.9:
    print("Berat Badan Berlebih (Cenderung Obesitas)")
elif a >= 30:
    print("Obesitas")
