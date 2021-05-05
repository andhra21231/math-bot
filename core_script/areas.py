def square(x, y):
    return x * y


def rectangle(x, y):
    return x * y


def triangle(x, y):
    return x * y / 2


def layang(x, y):
    return x * y / 2


def trapezoid(x, y, z):
    return (x + y) / 2 * z


def poligon(x, y):
    return (x / 2) * y


def circle_perimeter(x):
    return x / 2


def circle(x):
    return 22 / 7 * x * x

def circle_3_14(x):
    return 3.14 * x * x
print("Apa Yang Ingin Kamu Kalkulasi ?")
print("Pilih Antara Pilihan Ini :")
print("1. Persegi")
print("2. Segi panjang")
print("3. segitiga")
print("4. layang-layang")
print("5. Trapezoid")
print("6. polygon")
print("7. Perimeter Lingkaran (Perimeter = Diameter)")
print("8. Luas Lingkaran (Rekomendasi Lakukan No.7 Dahulu)")
print("9. Luas Lingkaran (Khusus Untuk Bilangan Yang Menggunakan PI 3.14)")

while True:
    choice = input("Pilih Antara : (1/2/3/4/5/6/7/8/9) :")

    if choice in ('1', '2'):
        num1 = float(input("Masukan Sisi 1 : "))
        num2 = float(input("Masukan Sisi 2 :"))

    if choice == '1':
        print(num1, "Dikali", num2, "Hasilnya Adalah", square(num1, num2))

    if choice == '2':
        print(num1, "Dikali", num2, "Hasilnya Adalah", rectangle(num1, num2))

    if choice in ('3'):
        num1 = float(input("masukan Dasar Dari Segitiganya : "))
        num2 = float(input("MASUKAN Tinggi Dari Segitiganya :"))
    if choice == '3':
        print(num1, "Dikali", num2 , "dibagi 2", "Hasilnya Adalah", triangle(num1, num2))
    if choice in ('4'):
        num1 = float(input("Masukan Diagonal A : "))
        num2 = float(input("Masukan Diagonal B : "))
    if choice == '4':
        print(num1, "Dikali Dengan", num2,  "Lalu Dibagi Dengan 2", "Sama Dengan", layang(num1, num2))
    if choice in ('5'):
        num1 = float(input("Masukan Sisi Yang Besar :"))
        num2 = float(input("Masukan Sisi Yang Kecil : "))
        num3 = float(input("Masukan Tinggi Dari Trapezoid  :"))
    if choice == '5':
        print(num1, "Ditambah", num2, "dibagi 2", "Dikali", num3,"Sama Dengan", trapezoid(num1, num2, num3))

    if choice in ('6'):
        num1 = float(input("Masukan Perimeter : "))
        num2 = float(input("Masukan apothem : "))
    if choice == '6':
        print(num1, "Dibagi Dengan 2 Lalu Dikali Dengan", num2, "Sama Dengan", poligon(num1, num2))

    if choice in ('7'):
        num1 = float(input("Masukan Radius Lingkaran : "))

    if choice == '7':
        print(num1, "Dibagi Dengan 2","Sama Dengan", circle_perimeter(num1))
    if choice in ('8'):
        num1 = float(input("Masukan Diameter / Perimeter (Bisa Didapatkan Dari No.7)"))
    if choice == '8':
        print("π Dikali", num1, "Pangkat 2 Sama Dengan", circle_3_14(num1))

    if choice in ('9'):
        num1 = float(input("Masukan Diameter / Perimeter (Bisa Didapatkan Dari No.7)"))
    if choice == '9':
        print("π Dikali", num1, "Pangkat 2 Sama Dengan", circle_3_14(num1))
