class Customer:
    """Customer class"""
    
    def __init__(self, name: str):
        self.name = name
    
    def userLogin(self):
        print("Hoş Geldiniz :" + self.name)
        
    def userLogout(self,):
        print("Çıkış Yaptınız: " + self.name)