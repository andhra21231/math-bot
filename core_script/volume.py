def cube(x):
    return x * x * x


def balok(x, y, z):
    return x * y * z


def tri_prism_alas(x, y):
    return x * y / 2

def tri_prism_hasil(x, y, z):
    return tri_prism_alas(x, y) * z


def silinder(x, y):
    return 22/7 * x * x * y


def silinder_2(x, y):
    return 3.14 * x * x * y


def pyramid(x, y):
    return 1/3 * x * y


def sphere(x):
    return 4/3 * 3.14 * x * x * x


def sphere_b(x):
    return 4/3 * 22/7 * x * x * x


print("Apa Yang Ingin Kamu Kalkulasi ? ")
print("1. Kotak")
print("2. Balok")
print("3. Prisma Segitiga")
print("4. Silinder Dengan Phi : 22/7 (Kelipatan 7)")
print("5. silinder Dengan Phi : 3.14")
print("6. Piramida")
print("7. bola Dengan Phi : 22/7 (Kelipatan 7)")
print("8. bola Dengan Phi : 3.14")


while True:
    choice = input("Pilih Antara : (1/2/3/4/5/6/7/8) : ")

    if choice in ('1'):
        num1 = float(input("Masukan Sisi Kotak :"))

    if choice == '1':
        print(num1, "Dipangkat 3 Sama Dengan :", cube(num1))

    if choice in ('2'):
        num1 = float(input("Masukan Panjang Balok :"))
        num2 = float(input("Masukan Lebar Balok : "))
        num3 = float(input("Masukan Tinggi Balok :"))

    if choice == '2':
        print(num1, "Dikali", num2, "Dikali", num3, "Sama Dengan", balok(num1, num2, num3))

    if choice in ('3'):
        num1 = float(input("Masukan Panjang Alas :"))
        num2 = float(input("Masukan Tinggi Alas :"))
        num3 = float(input("Masukan Tinggi Prisma :"))

    if choice == '3':
        print("Luas alas =", num1, "dikali", num2, "dibagi 2 hasilnya", tri_prism_alas(num1, num2))
        print("Volume prisma =", tri_prism_hasil(num1, num2, num3))

    if choice in ('4'):
        num1 = float(input("masukan Radius Silinder (Bisa Didapat Di Area Calculation) : "))
        num2 = float(input("Masukan Tinggi Silinder : "))

    if choice == '4':
        print(num1, "Dikali", num2, "Sama Dengan", silinder(num1, num2))

    if choice in ('5'):
        num1 = float(input("masukan Radius Silinder (Bisa Didapat Di Area Calculation) : "))
        num2 = float(input("Masukan Tinggi Silinder : "))

    if choice == '5':
        print(num1, "Dikali", num2, "Sama Dengan", silinder_2(num1, num2))

    if choice in ('6'):
        num1 = float(input("masukan dasar dari piramidanyanya : "))
        num2 = float(input("masukan tinggi dari piramidnya : "))

    if choice == '6':
        print("1/3 dikalikan", num1, "dikali",num2, "sama dengan", pyramid(num1, num2))

    if choice in ('7'):
        num1 = float(input("masukan radius :"))

    if choice == '7':
        print("4/3 dikali dengan pi dikali", num1, "pangkat 3 sama dengan", sphere(num1))

    if choice in ('8'):
        num1 = float(input("masukan radius :"))

    if choice == '8':
        print("4/3 dikali dengan pi dikali", num1, "pangkat 3 sama dengan", sphere_b(num1))
       
