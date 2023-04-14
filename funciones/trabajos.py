print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Jennifer Illescas")
print("Fecha: 13/04/2023\n")
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
from metodos import*

opcion=1
while opcion>=0 and opcion <=10:
    print("MENU DE OPCIONES")
    print("1. Contador Ascendente")
    print("2. Contador Descendente")
    print("3. Suma de Numeros")
    print("4. Factorial")
    print("5. Adivinar un Numero")
    print("6. Contador de Vocales")
    print("7. Suma de Numeros Pares")
    print("8. Calculo de Potencia")
    print("9. Calculo de Promedio")
    print("10. Contador de Palabras")
    print("0. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==0:
        print("Ha seleccionado salir")
    elif opcion==1:
        print("Ha seleccionado la opcion 1. Contador Ascendente")
        num=int(input("Ingresar un valor: "))
        contadorascendente1(num)
    elif opcion==2:
        print("Ha seleccionado la opcion 2. Contador Descendente")
        num=int(input("Ingresar un valor: "))
        contadordesendente(num)
    elif opcion==3:
        print("Ha seleccionado la opcion 3. Suma de Numeros")
        num=int(input("Ingrese un valor: "))
        suma(num)
    elif opcion==4:
        print("Ha seleccionado la opcion 4. Factorial")
        num=int(input("Ingrese un valor: "))
        print(factorial(num))
    elif opcion==5:
        print("Ha seleccionado la opcion 5. Adivinar un Numero")
        aleatorio=random.randint(1,10)
        print("El numero que se genero es: ",str(aleatorio))
        adivinar(aleatorio)
    elif opcion==6:
        print("Ha seleccionado la opcion 6. Contador de Vocales")
        vocales=input("Ingresar una cadena de texto")
        print(contador_vocales(vocales))
    elif opcion==7:
        print("Ha seleccionado la opcion 7. Suma de Numeros Pares")
        num=int(input("ingresar un valor: "))
        print("La suma de los numeros pares desde cero hasta",num,"es",suma_de_numeros(num))
    elif opcion==8:
        print("Ha seleccionado la opcion 8. Calculo de Potencia")
        num=int(input("ingresar un valor: "))
        exponente=int(input("ingresar un exponente: "))
        potencia(num,exponente)
    elif opcion==9:
        print("Ha seleccionado la opcion 9. Calculo de Promedio")
        num=input("ingresar una lista separado por comas: ")
        num_list=[int(num)for num in num.split(",")]
        print(promedio(num_list))
    elif opcion==10:
        print("Ha seleccionado la opcion 10. Contador de Palabras")
        palabras=input("Ingrese una frase: ")
        print(contador_palabras(palabras))