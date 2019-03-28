#Mision 07. Ciclos while.
#JOSE LUIS MACIAS VAZQUEZ GRUPO 03
#Matricula: A01655713



def dividir(dividendo,divisor):

    cociente = 0

    while dividendo >= divisor:

        dividendo = dividendo - divisor

        cociente = cociente + 1

    print("El cociente es:", cociente)

    print ("El residuo es: ", dividendo)





def encontrarMayor():

    numero = int(input("Escribe un número positivo [teclea -1 para salir]: "))

    mayor = numero

    while numero != -1:

        numero = int(input("Escribe un número positivo [teclea -1 para salir]: "))

        if numero > mayor:

                mayor = numero

    if mayor == -1:

        print ("No hay mayor")

    else:

        print ("El mayor es ", mayor)




def main():

    salir = False

    while not salir:


        opcion = int(input(print (" 1. Calcular divisiones \n 2. Encontrar el mayor \n 3. Salir \n Teclea tu opción: ")))


        if opcion == 1:

            dividendo = int(input("Escribe el valor del dividendo: "))

            divisor = int(input("Escribe el valor del divisor: "))

            dividir(dividendo, divisor)

        elif opcion == 2:

            encontrarMayor()

        elif opcion == 3:

            salir = True

            print ("Gracias por usar este programa regresa pronto ")

        elif opcion > 3 or opcion < 1:

            print ("Si busca salir digite 3 o escoja un número dentro de las opciones : ")

            opcion = int(input(print(" 1. Calcular divisiones \n 2. Encontrar el mayor \n 3. Salir \n Teclea tu opción: ")))




main()

