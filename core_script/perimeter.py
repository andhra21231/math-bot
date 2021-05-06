def square(x):
    return x * 4

def rectangle(x, y):
    return 2 * (x + y)

def triangle(x, y, z):
    return x + y + z

def circle_multiples_of_7_with_radius(x):
    return 2 * 22/7 * x

def circle_multiples_of_7_with_diameter(x):
    return 22/7 * x

def circle_not_multiples_of_7_with_radius(x):
    return 2 * 3.14 * x

def circle_not_multiples_of_7_with_diameter(x):
    return 3.14 * x

def diamond(x):
    return x * 4

def kite(x, y):
    return 2 * x + 2 * y

print("Apa Yang Ingin Kamu Kalkulasi ? ")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran kelipatan 7 dengan jari jari")
print("5. Lingkaran kelipatan 7 dengan diameter")
print("6. Lingkaran bukan kelipatan 7 dengan jari jari")
print("7. Lingkaran bukan kelipatan 7 dengan diameter")
print("8. belah ketupat")
print("9. Layang-Layang")

while True:
    choice = input("Pilih Antara : (1/2/3/4/5/6/7/8/9) : ")

    if choice in ('1'):
        num1 = float(input("Masukkan Panjang Sisi :"))

    if choice == '1':
        print(num1, "dikali 4, hasilnya", square(num1))

    if choice in ('2'):
        num1 = float(input("Masukkan Panjang :"))
        num2 = float(input("Masukkan lebar :"))

    if choice == '2':
        print(num1, "dikali", num2, "dikali 2, hasilnya", rectangle(num1, num2))

    if choice in ('3'):
        num1 = float(input("Masukkan panjang sisi 1 :"))
        num2 = float(input("Masukkan panjang sisi 2 :"))
        num3 = float(input("Masukkan panjang sisi 3 :"))

    if choice == '3':
        print(num1, "ditambah", num2, "ditambah", num3, "hasilnya", triangle(num1, num2, num3))

    if choice in ('4'):
        num1 = float(input("Masukkan panjang jari-jari :"))

    if choice == '4':
        print("2 dikali 22/7 dikali", num1, "hasilnya", circle_multiples_of_7_with_radius(num1))

    if choice in ('5'):
        num1 = float(input("Masukkan panjang diameter :"))

    if choice == '5':
        print("22/7 dikali", num1, "hasilnya", circle_multiples_of_7_with_diameter(num1))

    if choice in ('6'):
        num1 = float(input("Masukkan panjang jari-jari :"))

    if choice == '6':
        print("2 dikali 3.14 dikali", num1, "hasilnya", circle_not_multiples_of_7_with_radius(num1))

    if choice in ('7'):
        num1 = float(input("Masukkan panjang diameter :"))

    if choice == '7':
        print("3.14 dikali", num1, "hasilnya", circle_not_multiples_of_7_with_diameter(num1))

    if choice in ('8'):
        num1 = float(input("Masukkan panjang sisi :"))

    if choice == '8':
        print(num1, "dikali 4 hasilnya", diamond(num1))

    if choice in ('9'):
        num1 = float(input("Masukkan sisi 1 :"))
        num2 = float(input("Masukkan sisi 2 :"))

    if choice =='9':
        print(num1, "ditambah", num2, "dikali 2 hasilnya", kite(num1, num2))
