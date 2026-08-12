
class Animal:
    # bu method miras verildiği sıfınta doldurulmak zorunda olacaktır.
    def speak(self):
        pass
    
    def suIc(self):
        return "Su İçer"
    
    
class Dog(Animal):
    def speak(self):
        sayi = 10
        if (sayi == 10):
            return "Dog Speak"
        else:
            return super().speak()


class Cat(Animal):
    def speak(self):
        return "Cat Speak"
    

class Deneme(Animal):
    """"""    
    
dog = Dog()
cat = Cat()

def call(obj: Animal):
    print( obj.speak() )
    
call(dog)
call(cat)    