def area_cilindro(altura,radio):
    return radio**2*3.14*altura

radio=int(input("Introduce el radio"))
altura=int(input("Introduce la altura"))

print("El volumen del cilindro es:")
print(area_cilindro(radio,altura))