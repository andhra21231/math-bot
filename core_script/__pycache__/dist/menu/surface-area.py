import math


def cube(x):
    return 6 * x * x


def cylinder(x, y):
    return 2 * 22/7 * x * (x + y)


def cylinder_2(x, y):
    return 2 * 3.14 * x * (x + y)


def balok(x, y, z):
    return (2 * x * y) + (2 * x * z) + (2 * y * z)


def sphere(x):
    return 4 * 3.14 * x * x


def sphere_2(x):
    return 4 * 22 / 7 * x * x


def cone(x, y):
    return (3.14 * x * x) + (3.14 * x * (math.sqrt((y * y) + (x * x))))


def cone_1(x, y):
    return (22 / 7 * x * x) + (22 / 7 * x * (math.sqrt((y * y) + (x * x))))


def pyramid(x, y, z):
    return (x * x) + (2 * y * z)


print("Apa Yang Ingin Kamu Kalkulasi ? ")
print("1. Kotak")
print("2. silinder Dengan 22/7")
print("3. Silinder Dengan 3.14")
print("4. balok")
print("5. bola 3.14")
print("6. bola 22 / 7")
print("7. cone 3.14")
print("8. cone 22 / 7")
print("9. piramida")

while True:
    choice = input("Masukan Antara : (1/2/3/4/5/6/7/8/9):")

    if choice in ('1'):
        num1 = float(input("Masukan Sisi Kotaknya : "))

    if choice == '1':
        print("6 x", num1, "pangkat 2 sama dengan", cube(num1))

    if choice in ('2'):
        num1 = float(input("Masukkan radius alas : "))
        num2 = float(input("Masukkan tinggi silinder :"))

    if choice == '2':
        print("2 x 22/7 x", num1, "x (", num1, "+", num2, ") hasilnya", cylinder(num1, num2))

    if choice in ('3'):
        num1 = float(input("Masukkan radius alas : "))
        num2 = float(input("Masukkan tinggi silinder :"))

    if choice == '3':
        print("2 x 3.14 x", num1, "x (", num1, "+", num2, ") hasilnya", cylinder_2(num1, num2)) 

    if choice in ('4'):
        num1 = float(input("Masukan Panjang :"))
        num2 = float(input("Masukan Lebar : "))
        num3 = float(input("Masukan Tinggi : "))    

    if choice == '4':
        print("2 x ", num1, "x", num2, "+", "2 x ", num1, "x", num3, "+ 2 x ",num2, "x", num3, "=", balok(num1, num2, num3))

    if choice in ('5'):
        num1 = float(input("Masukan Radius Bola :"))

    if choice == '5':
        print("4 x 3.14 x", num1, "Pangkat 2 = ", sphere(num1))

    if choice in ('6'):
        num1 = float(input("Masukan Radius Bola :"))

    if choice == '6':
        print("4 x 22 / 7 x", num1, "Pangkat 2 = ", sphere_2(num1))

    if choice in ('7'):
        num1 = float(input("Masukan Radius Dasar Cone :"))
        num2 = float(input("Masukan tinggi Cone : "))

    if choice == '7':
        print("3.14 x", num1, "pangkat 2 + 3.14 x", num1, "x", num2, "Dipangkat 2 +", num1, "Dipangkat 2 Lalu Diakar 2 = ", cone(num1, num2))

    if choice in ('8'):
        num1 = float(input("Masukan Radius Dasar Cone :"))
        num2 = float(input("Masukan tinggi Cone : "))

    if choice == '8':
        print("3.14 x", num1, "pangkat 2 + 3.14 x", num1, "x", num2, "Dipangkat 2 +", num1, "Dipangkat 2 Lalu Diakar 2 = ", cone_1(num1, num2))

    if choice in '9':
        num1 = float(input("Masukan panjang Dari Dasar piramidanya : "))
        num2 = float(input("Masukan Tinggi Dari Piramidanya :"))
        num3 = float(input("Masukan Tinggi Miring Dari piramidanya : "))

    if choice == '9':
        print(num1, "Dipangkat 2 + 2 x", num1, "x", num3)
