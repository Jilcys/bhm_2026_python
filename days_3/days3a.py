# list kullanımı
users = ["Ahmet", "Mehmet", "Fatma", "Ayşe", "Zeynep", "Bengü"]

cities = []
cities.append("Istanbul")

users.sort()

# tersine çevirme
users.reverse()
print( users )

# tuple kullanımı
# değerlerin değiştirilemez olduğunu gösterir
print("================================")
cities = ("İstanbul", "Ankara", "Izmir", "Bursa", "Adana", "Antalya")
print( cities[0] )
tupleObj = (
    {"name": "Ahmet", "age": 30},
    {"name": "Mehmet", "age": 25},
    {"name": "Ayşe", "age": 20},
)
for city in cities:
    print(city)

for user in tupleObj:
    print(user)
    
print("================================")
days = ["Pazartesi", "Pazartesi", "Salı", "Çarşamba", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
print(days)

# set kullanımı
# benzersiz değerleri tutmak için kullanılır
# days_set = set() # boş set oluşturma
days_set_data = {"Pazartesi", "Pazartesi", "Salı", "Çarşamba", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"}
days_set_data.add("Pazartesi")
days_set_data.add("Salı")
print(days_set_data)

days_set_data_2 = set(days)
print(days_set_data_2)

print("================================")
# dictionary kullanımı
# key-value şeklinde veri tutmak için kullanılır
user = {
    "name": "Ahmet",
    "age": 30,
    "city": "Istanbul"
}

user1 = {
    "name": "Kemal",
    "age": 25,
    "city": "Ankara"
}

user2 = {
    "name": "Ayşe",
    "age": 20,
    "city": "Izmir"
}

user3 = {
    "name": "Fatma",
    "age": 35,
    "city": "Bursa"
}

# eleman ekleme
user["email"] = "ahmet@mail.com"
user["name"] = "Mehmet"
print(user)

users_dict = dict(name = "Ahmet", age = 30, city = "Istanbul")

dic_arr = [user, user1, user2, user3]
print(dic_arr)
print("================================")
for item in dic_arr:
    print(item["name"], item["age"], item["city"])
    
print(user.keys())
for key in user.keys():
    print(key, user[key])
    
print("================================")      
print(user.values())
print(len(user))

# anahtar kontrolü
print("name" in user)

# Dictionary Güncelleme
user.update({"name": "Ahmet", "age": 35, "address": "Kadıköy"})
print(user)