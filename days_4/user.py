class UserClass:
    
    """Kullanıcı Sınıfı"""
    
    def login(self, email: str, password: str):
        if (email == "ali@mail.com" and password == "12345"):
            return True
        else:
            return False
        
    def profile(self) -> str :
        return "Ali Bilmem"    