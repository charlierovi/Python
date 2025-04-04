import random #Se importa la librería random para que se genere un número aleatorio

num_aleatorio=random.randint(1,100) #Se declara la variable del número aleatorio donde el rango va de 1 a 100

intentos=0 #Se declara la variable de intentos para luego tener en cuenta el máximo de intentos posibles

while intentos<10: #Se crea el bucle while que se llevará a cabo mientras los intentos sean menos de 10 tal y como se pide en el enunciado
    intento_usuario = int(input("Introduce tu número entre el 1 y el 100: ")) #Se declara la variable intento usuario con un input para que el usuario introduzca el número que quiera.
    intentos+=1 #Se crea el contador con += para que no sea infinito

    if intento_usuario>num_aleatorio: #Se utiliza un primer condicional
        print("Prueba con un numero mas pequeño.")
    elif intento_usuario<num_aleatorio: #Se utiliza un segundo condicional
        print("Prueba con un numero más grande.")
    else: #Se introduce un else ya que no se cumplen los dos primeros condicionales
        break #Se introduce el break para salir del bucle
if intento_usuario==num_aleatorio: #Se introduce otro condicional para afirmar que el usuario ha acertado el numero aleatorio y por tanto ha ganado
    print(f"¡Felicidades! Has ganado, tu numero era el {num_aleatorio}.")
else: #Se usa un else ya que si no es igual y está fuera del bucle significa que el usuario ha perdido
    print(f"¡GAME OVER! Tu numero era el {num_aleatorio}.")



