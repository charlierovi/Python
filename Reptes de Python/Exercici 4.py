palabra1 = input("Introdueix una paraula: ")
palabra2 = input("Introdueux una altre paraula: ")
es_diferent = False

if len(palabra1)!=len(palabra2):
    print("Les paraules no són les mateixes")
else:
    for i in range(0,len(palabra1)):
        if palabra1[i]!=palabra2[i]:
            print("No són les mateixes paraules")
            es_diferent = True
            break

if es_diferent == False:
    print("Són les mateixes paraules")


