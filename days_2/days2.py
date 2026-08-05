# Karşılaştırma operatörleri
# Uygulama karar verme aşamasında kullanılır
# ==, !=, >, <, >=, <=

x, y = 10, 5

# == -> sol taraftaki değer ile sağ taraftaki değer eşit mi?
status = x == y
print(f"x == y {status}")

status = x != y
print(f"x != y {status}")

status = x > y
print(f"x > y {status}")

status = x < y
print(f"x < y {status}")

status = x >= y
print(f"x >= y {status}")

status = x <= y
print(f"x <= y {status}")

email = "ali@mail.com"
password = "123456"

status = email == "ali@mail.com"
print(f"email -> {status}")

status = password == "123456"
print(f"password -> {status}")

# Mantıksal operatörler
# and, or, not
# and -> her iki koşul da doğru ise True döner
status = (x > y) and (y > 10)
print(f"status and -> {status}")
status = (email == "ali@mail.com") and (password == "123456")
print(f"status and -> {status}")

# or -> herhangi bir koşul doğru ise True döner
status = (x > y) or (y > 10)
print(f"status or -> {status}")

# not -> koşulun tersini döner
status = not (x > y)
print(f"status not -> {status}")
# açık / kapalı butonu
button = True
button = not button
button = not button
button = not button
button = not button
print(f"button not -> {button}")

# Tür dönüşümleri
# str to int, float, bool
ageStr = "18"
age = int(ageStr)
status = age >= 18
print(f"age -> {age}")
ageFloat = float(ageStr)
print(f"ageFloat -> {ageFloat}")

strData = "100"
intData = int(strData)
print(f"intData -> {intData}")

boolData = bool("True")
print(f"boolData -> {boolData}")

floatData = 135.890
intFloat = int(floatData)
print(f"intFloat -> {intFloat}")


# try - except
stAgeData = "Ahmet"
try:
    # hata olma olasığı olan kodlar buraya yazılır
    age = int(stAgeData)
    print(f"age -> {age}")
except ValueError:
    # Hata olduğunda çalışacak kodlar buraya yazılır
    print("Hata oluştu, lütfen sayısal bir değer giriniz.")
    
print("Program çalışmaya devam ediyor...")

# Kullanıcıdan veri alma
sayi1 = input("Lütfen sayı-1 giriniz: ")
sayi2 = input("Lütfen sayı-2 giriniz: ")
try:
    sum = int(sayi1) + int(sayi2)
    print(f"Toplam -> {sum}")
except ValueError:
    print("Hata oluştu, lütfen sayısal bir değer giriniz.")
