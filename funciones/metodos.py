#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contadorascendente1(num):
    cont=0
    while cont <= num:
        print(cont)
        cont+=1
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def contadordesendente(num):
    while num >= 0:
        print(num)
        num-=1
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def suma(num):
    sum=0
    cont=0
    while cont <= num:
        sum+=cont
        cont+=1
    print(sum)

#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.
def factorial(num):
    if num < 0:
        print("No existe el factorial de un numero negativo")
        return 1
    elif num ==0:
        return 1
    else:
        fact = 1
        while(num>1):
            fact*=num
            num-=1
        return fact

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
import random
def adivinar(aleatorio):
    numero=0
    while numero != aleatorio:
        numero=int(input("Ingrese un valor: "))
        if numero>aleatorio:
            print("El numero ingresado es mayor al numero de adivinar")
        elif numero<aleatorio:
            print("El numero ingresado es menor al numero a adivinar")
        else:
            print(aleatorio,"Felicidades adivino el numero",numero)

#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def contador_vocales(vocales):
    cont=0
    vocales1="a,e,i,o,u"
    numero=0
    while numero < len(vocales):
        if vocales[numero] in vocales1:
            cont+=1
        numero+=1
    return cont

#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suma_de_numeros(num):
    suma=0
    e=0
    while e <= num:
        if e % 2 ==0:
            suma+=e
        e+=1
    return suma

#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def potencia(numero,exponente):
    resultado=1
    cont=1
    while cont <= exponente:
        resultado = resultado*numero
        cont+=1
    print(resultado)

#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def promedio(lista_numeros):
    suma=0
    cont=0
    while cont < len(lista_numeros):
        suma=suma+lista_numeros[cont]
        cont+=1
    return suma/len(lista_numeros)


#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def contador_palabras(cadena):
    cadena=cadena.split(" ")
    return len(cadena)