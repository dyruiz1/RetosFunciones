ancho=int(input("Ingrese el ancho "))
altura=int(input("Ingrese la altura "))

def AreaCalcular(ancho,altura):
    area=ancho*altura
    print(area)
    

def PeriCalcular(ancho, altura):
    perimetro=(ancho*2)+(altura*2)
    print(perimetro)

def Graficar(ancho, altura):
    for i in range(altura):
          print(ancho*"*")
    
          

AreaCalcular(ancho,altura)
PeriCalcular(ancho, altura)
Graficar(ancho, altura)