

class OperasBas:
    #Declaracion de propiedades de clases

    num1= 0
    num2= 0
    res = 0

    #Declaracion del constructor de la clase 

    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    #Declaracion de los metodos de la clase 

    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: {}" .format(self.res))
    

def main():
        obj=OperasBas(3,5)
        obj.suma()
    
if __name__=="__main__":
        main()
       

    