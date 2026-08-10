# Tüm math modülü import etme
#import math

# Alias kullanımı
import math as m
import numpy

from days_4.user import UserClass

# mevcut klasör içinden çalıştırma
from days_4.days4 import print_hello, nameJoinSurname, dizi

# farklı klasör içinde çalışma
from days_1.days1 import email

from math import sqrt, pi


print(sqrt(49))
print(pi)

print(m.sqrt(16))  # Karekök alma

print_hello()
nameJoinSurname("Kemal", "Bilmem")
print(email)
print(dizi[0](5))

# Nesne Üretim
userObj = UserClass() # new UserClass()
loginStatus = userObj.login("ali@mail.com", "12345")
print(loginStatus)