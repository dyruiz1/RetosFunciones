def calculatTemperatura():
    arraynumero = []
    suma= 0
    temperaturaPromedio = 0
    for i in range(3):
        num = int(input("Digite un número: "))
        arraynumero.append(num)

    for temperatura in arraynumero:
        suma += temperatura
        temperaturaPromedio = (suma/len(arraynumero))

    print (f"{suma} suma de las temperaturas")
    print (f"{temperaturaPromedio} temperatura promedio")
calculatTemperatura()