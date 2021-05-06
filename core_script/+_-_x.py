# Untuk Pertambahan (Angka Input X akan Di Tambahkan Angka Input Y)
def add(x, y):
    return x + y

# Untuk pengurangan (Angka Input X Akan Di Kurangi Angka Input Y)
def subtract(x, y):
    return x - y

# Untuk Perkalian (Angka Input X Akan Di Kali Angka Y)
def multiply(x, y):
    return x * y

# Untuk pembagian (Angka X akan Di Bagi Y)
def divide(x, y):
    return x / y


print("Apa Yang Ingin Kamu Kalkulasi ?")
print("1.Pertambahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

while True:
    choice = input("Pilih Antara : (1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Masukan Nomor Pertama :  "))
        num2 = float(input("Masukan Nomor kedua : "))

        if choice == '1':
            print(num1, "Ditambah", num2, "Hasilnya Adalah", add(num1, num2))

        if choice == '2':
            print(num1, "Dikurangi", num2, "Hasilnya Adalah", subtract(num1, num2))

        if choice == '3':
            print(num1, "Dikali", num2, "Hasilnya Adalah", multiply(num1, num2))

        if choice == '4':
            print(num1, "Dibagi", num2, "Hasilnya Adalah", divide(num1, num2))
