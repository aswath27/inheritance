class Calculation1:  
    def add(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiply(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.add(10,20))  
print(d.Multiply(10,20))  
print(d.Divide(10,20))