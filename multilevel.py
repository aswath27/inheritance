class bike:  
    def speak(self):  
        print("super bikes")  

class Dog(bike):  
    def motorcycle(self):  
        print("mid bikes")  

class DogChild(Dog):  
    def fuel(self):  
        print("petrol")  
d = DogChild()  
d.motorcycle()  
d.speak()  
d.fuel()  