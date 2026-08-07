# Diziler - collections
# collections modülü, Python'da veri yapıları ve koleksiyonlar için ek işlevsellik sağlar. 
# Bu modül, listeleri barındırır.

users = ["Ali", "Veli", "Ayşe", "Fatma", "Mehmet"]

# index -> dizi üyesine erişim sağlanmak için kullanılır.
print( users[0] )  # Ali

# len() -> dizinin uzunluğunu döndürür.
print( len(users) )  # 5

print( users )

# dizi elemen ekleme
users.append("Ahmet")
print( users )

# dizi içerisine index ile eleman ekleme
users.insert(2, "Zeynep")
print( users )

# dizi eleman silme
users.remove("Fatma")
print( users )
# dizi eleman silme (index ile)
del users[1]
print( users )

# dizi eleman güncelleme
users[0] = "Kemal"
print( users )

# dizi elemanlarını temizleme
# users.clear()
# print( users )  # []

# loop ile dizi elemanlarını yazdırma
# dizi elemanlarını yazdırmak için for döngüsü kullanabiliriz.
for item in users:
    print(item)
    
# Range ile for loop
for i in range(5):
    print(i)

# Dizi içinde object kullanımı
cities = [
    {"name": "Istanbul", "population": 15000000, "area": 5461},
    {"name": "Ankara", "population": 5500000, "area": 2512},
    {"name": "Izmir", "population": 4300000, "area": 1234},
    {"name": "Bursa", "population": 3000000, "area": 1050},
]

for city in cities:
    print(f"City: {city['name']}, Population: {city['population']}, Area: {city['area']} km²")

# break - continue
# break -> döngüyü sonlandırmak için kullanılır.
for i in range(10):
    if i == 5:
        break
    print(i)
    
print("=========================")
for item in users:
    print(item)
    if item == "Ayşe":
        print("Ayşe bulundu")
        
print("=========================")        
for i in range(10):
    if i == 5:
        continue
    print(i)
    
print("=========================")    
# While loop
# while döngüsü, belirli bir koşul doğru olduğu sürece çalışır.
count = 0
while count < 5:
    print(count)
    count += 1
    
# pass kullanımı
# henüz bir işlem yapılmayacaksa, pass ifadesi kullanılır.
if len(users) > 100:
    pass  # Henüz bir işlem yapılmayacak

for i in range(10):
    pass  # Henüz bir işlem yapılmayacak

print("=========================") 
for i in range(5,10):
    print(i)