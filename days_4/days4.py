# Fonksiyonlar, belirli bir görevi yerine getiren kod bloklarıdır. 
# Python'da fonksiyonlar, `def` anahtar kelimesi ile tanımlanır ve genellikle bir isim ve parametreler alır. 
# Fonksiyonlar, kodun tekrar kullanılabilirliğini artırır ve programın daha düzenli olmasını sağlar.

def print_hello():
    print("Hello, World! - ")

print("Fonksiyon çağrıldı.")    

# Fonksiyon tetiklenmesi
print_hello()  # Fonksiyon çağrısı yapılıyor
print_hello()
print_hello()
print_hello()

# Parametreli fonksiyonlar
def nameJoinSurname(name: str, surname: str):
    join = name.title() + " " + surname.title()
    print(join)
    
nameJoinSurname("ali", "Bilmem")
nameJoinSurname("Ayşe", "yılmaz")

# Returnlü fonksiyonlar
def sum(a: int, b: int) -> int:
    return a + b

sm = sum(599, 1012)
if (sm > 1000):
    print("Toplam 1000'den büyük")
else: 
    print("Toplam 1000'den küçük")

def userInfo(name: str, email: str, city: str = "İstanbul") -> str:
    return f"Name: {name.title()}, Email: {email}, City: {city.title()}"

info = userInfo("ali", "ali@mail.com")
print(info)

# lambda fonksiyonları
square = lambda x, y, z : f"{x ** 2 + z ** 2} {y.title()}"
result = square(2, "ali", 4)
print(result)

dizi = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4
]
result0 = dizi[0](2)
result1 = dizi[1](5)
result2 = dizi[2](3)
print(result0, result1, result2)