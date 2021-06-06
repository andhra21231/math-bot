import math


def hypotenuse_1(x, y):
    return math.sqrt((x * x) + (y * y))


def hypotenuse_2(x, y):
    return math.sqrt((x * x) - (y * y))


print("Apa Yang Ingin Kamu Kalkulasi ? ")
print("1. Hipotenusa (sisi miring)")
print("2. sisi a")
print("3. sisi b")

while True:
    choice = input("pilih antara (1/2/3) : ")
    if choice in ('1'):
        num1 = float(input("Masukan Sisi A:"))
        num2 = float(input("Masukan Sisi B:"))

    if choice == '1':
        print(num1, "dipangkat 2 Lalu Ditambah", num2, "pangkat 2 lalu di akar, sama dengan :", hypotenuse_1(num1, num2))

    if choice in ('2'):
        num1 = float(input("Masukan Sisi C :"))
        num2 = float(input("Masukan Sisi B :"))

    if choice == '2':
        print(num1, "dipangkat 2 lalu dikurangi", num2, "dipangkat 2 lalu diakar, sama dengan : ", hypotenuse_2(num1, num2))

    if choice in ('3'):
        num1 = float(input("Masukan Sisi C :"))
        num2 = float(input("Masukan Sisi A :"))

    if choice == '3':
        print(num1, "dipangkat 2 lalu dikurangi", num2, "dipangkat 2 lalu diakar, sama dengan : ",hypotenuse_2(num1, num2))

