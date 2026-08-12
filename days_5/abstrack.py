from abc import ABC, abstractmethod

class Memur(ABC):
    
    @abstractmethod
    def accountNumber(self) -> int:
        pass
    
    number = 0
    def havale(self):
        self.number = self.accountNumber()
        print(f"Havale Yapıldı:  + {self.number}")
        
    def eft(self):
        print(f"Eft Yapıldı:  + {self.number}")
    
    def hesap(self):
        if (self.number == 100):
            print("1000 Bakiye var")
        elif (self.number == 200):
                print("2000 Bakiye var")
        else:
            print("Tanımlı hesap yok!")    


class BankCustomer(Memur):
    
    def __init__(self, number: int):
        self.number = number
    
    def accountNumber(self):
        return self.number


customer = BankCustomer(100)
customer.havale()
customer.eft()
customer.hesap()    