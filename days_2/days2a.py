# Karar kontrol yapıları
# if, elif, else
# if koşul:
    # koşul doğru ise çalıştırılacak kodlar
    
age = 17
status = age >= 18
if status:
    # koşul doğru ise çalıştırılacak kodlar
    print("Ehliyet alabilirsiniz")
else:
    # koşul yanlış ise çalıştırılacak kodlar
    print("Ehliyet alamazsınız")
    
if True:
    print("Koşul doğru")
    
    
username = input("Kullanıcı adınızı giriniz: ")
password = input("Şifrenizi giriniz: ")    

if len(username) < 3:
    print("Kullanıcı adı en az 3 karakter olmalıdır.")
else:
    if username == "ali01" and password == "123456":
        print("Giriş başarılı")
    else:
        print("Giriş başarısız, Tekrar deneyiniz.")
        
        

uname = "ali01"
uemail = "ali@mail.com"
upassword = "123456"

if uname == "":
    print("Kullanıcı adı boş bırakılamaz.")
elif uemail == "":
    print("E-posta boş bırakılamaz.")
elif upassword == "":
    print("Şifre boş bırakılamaz.")
else:
    print("Kayıt başarılı")    
            

# Not sistemi
score = 85
grade = ""
if score >= 90:
    grade = "AA"
elif score >= 80:
    grade = "BA"
elif score >= 70:
    grade = "BB"
elif score >= 60:
    grade = "CB"
elif score >= 50:
    grade = "CC"
else:
    grade = "FF"
print(f"Notunuz -> {grade}")