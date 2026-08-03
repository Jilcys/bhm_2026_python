# Tek satırlı açıklama
"""
Çok satırlı açıklama
bir açıklama bölümü
"""

# Değişken tanımlama
# değişken isimleri harf veya alt çizgi ile başlamalıdır ve harf, rakam veya alt çizgi içerebilir.

# String veri tipi
name = "Kemal" # String veri tipi
age = 30 # Integer veri tipi
status = True # Boolean veri tipi
ondalik = 30.5

# Geçersiz değişken ifadeleri
# 1name = "Kemal" # Geçersiz değişken ismi,
# name! = "Kemal" # Geçersiz değişken ismi,
# name@ = "Kemal" # Geçersiz değişken ismi,

sayi1 = 10
sayi2 = 20

# çoklu atama
a, b, c, d = 1, 2, 3, "Salı"

# aynı değere bir den fazla değişken atama
x = y = z = 100

# tuple veri tipi
my_tuple = (1, 2, 3, 4, 5)
a1, b1, c1, d1, e1 = my_tuple

print("Name:", name)
print("Age:", age)
print("Status:", status)
print("Ondalik:", ondalik)

# operatörler
x = 10
x += 5 # x = x + 5
x -= 3 # x = x - 3
x *= 2 # x = x * 2
x /= 4 # x = x / 4
print("x:", x)

# type check
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of status:", type(status))
print("Type of ondalik:", type(ondalik))

name1 = "Ahmet"
surname2 = "Yılmaz"
joined_name = name1 + " " + surname2
join = f"{name1} {surname2}"
print(join)

# String metotları
my_string = "Python programlama dili"
email = "   ali@mail.com   "
print(my_string.upper()) # Büyük harfe çevirir
print(my_string.lower()) # Küçük harfe çevirir
print(my_string.title()) # Her kelimenin ilk harfini büyük yapar
print(email.strip()) # Başındaki ve sonundaki boşlukları siler
print(my_string.replace("Python", "****")) # Belirtilen kelimeyi değiştirir
print(len(my_string)) # String uzunluğunu verir
print("dil" in my_string) # Belirtilen kelimenin string içinde olup olmadığını kontrol eder
stringArr = my_string.split(" ") # Stringi boşluklardan ayırır ve listeye çevirir
print(stringArr[0])
print(stringArr[1])
print(stringArr[2])

# String indexing
print(my_string[0]) # İlk karakteri verir
print(my_string[-1]) # Son karakteri verir
print(my_string[0:3]) # 0'dan 3'e kadar olan karakterleri verir
print(my_string[::-1]) # Stringi ters çevirir