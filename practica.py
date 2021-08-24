#Erickson Vásquez

#1.	ESCRIBIR UN PROGRAMA PARA SUMAR DOS NÚMEROS LEÍDOS POR TECLADO Y ESCRIBIR EL RESULTADO.

def sum(a, b):
    return (a + b)

a = int(input('Escribe el primer numero: '))
b = int(input('Escribe el segundo numero: '))

print(f'La suma de {a} y {b} es {sum(a, b)}')

#2.	ESCRIBIR UN PROGRAMA QUE PERMITA LEER 2 NÚMEROS DIFERENTES Y NOS DIGA CUÁL ES EL MAYOR DE LOS 2 NÚMEROS.

def nums(a, b):
    if a.isnumeric() and b.isnumeric():
         
         if a>b:
             print('El primer valor es mayor que el segundo')
        # TODO: write code...
         elif b>a:
             print('El segundo valor es mayor que el primero')
         else:
             print('Ambos valores son iguales')
    else:
        print('Ambos numeros deben ser valores numericos para poder hacer la comparativa')
    
    return 0

a = input('Escribe el primer numero: ')
b = input('Escribe el segundo numero: ')
nums(a,b)



#3.	CREAR UN PROGRAMA EN PYTHON EN EL QUE SE ALMACENEN 3 NÚMEROS EN 3 VARIABLES A, B Y C. EL PROGRAMA DEBE DECIDIR CUÁL ES EL MAYOR Y CUÁL ES EL MENOR.

def nums(va, vb, vc):
    if va.isnumeric() and vb.isnumeric() and vc.isnumeric():
        numeros = [int(va),int(vb),int(vc)]
        numeros.sort(reverse = False)
        print(f'El valor mas alto es {numeros[2]} y el menor es {numeros[0]}')
    else:
        print('Todos los valores deben ser númericos para poder hacer la comparativa')
    
    return 0

a = input('Escribe el primer numero: ')
b = input('Escribe el segundo numero: ')
c = input('Escribe el tercer numero: ')
nums(a,b,c)


#4.	REALIZAR UN PROGRAMA PARA QUE NOS CALCULE LA HIPOTENUSA DE UN TRIÁNGULO RECTÁNGULO, CONOCIDOS SUS DOS CATETOS.
import math
a=float(input("Ingrese el valor de un cateto\n"))
b=float(input("Ingrese el valor del otro cateto\n"))
c=math.sqrt((a*a+b*b))
print('LA HIPOTENUSA ES:')
print(str(c))

#5.	ESCRIBIR UN PROGRAMA EN PYTHON PARA SUMAR 10 NÚMEROS LEÍDOS POR TECLADO.

a=float(input("Ingrese el primer valor"))
b=float(input("Ingrese el segundo valor"))
c=float(input("Ingrese el tercer valor"))
d=float(input("Ingrese el cuarto valor"))
e=float(input("Ingrese el quinto valor"))
f=float(input("Ingrese el sexto valor"))
g=float(input("Ingrese el septimo valor"))
h=float(input("Ingrese el octavo valor"))
i=float(input("Ingrese el noveno valor"))
j=float(input("Ingrese el decimo valor"))

print('LA SUMA DE TODOS LOS VALORES ES:')
print(a+b+c+d+e+f+g+h+i+j)

#6.	MODIFICAR EL PROGRAMA ANTERIOR PARA QUE PERMITA SUMAR N NÚMEROS. EL VALOR DE N SE DEBE LEER PREVIAMENTE POR TECLADO.
total=0;
cantidad_de_numeros=int(input("¿Cúantos números deseas sumar?"))
print('\n\n\n')
for i in range(1,cantidad_de_numeros+1):
    numero_a_sumar=float(input("Inserte el valor # "+str(i)))
    total=total+numero_a_sumar;
print('La suma total de los números es ' +str(total))



#7.	HACER UN PROGRAMA QUE PERMITA ESCRIBIR LOS 10 PRIMEROS PARES INGRESADOS POR TECLADO.
print('\n\n\n')
for i in range(1,10+1):
    valor=int(input("Inserte el valor # "+str(i)))
    if valor % 2 == 0:
        print('El número', valor, 'es par.')
    else:
        print('El número', valor, 'es impar.')


#8.	ESCRIBIR UN PROGRAMA PARA SUMAR LOS N PRIMEROS IMPARES. REALIZAR DESPUÉS UNO QUE HAGA LO MISMO CON LOS PARES Y OTRO CON LOS MÚLTIPLOS DE 3.
#7.	HACER UN PROGRAMA QUE PERMITA ESCRIBIR LOS 10 PRIMEROS PARES INGRESADOS POR TECLADO.
cuantos_pares=int(input("¿Cúantos números pares como máximo quieres sumar?"))
cuantos_impares=int(input("¿Cúantos números impares como máximo quieres sumar?"))
cuantos_multiplo=int(input("¿Cúantos números múltiplos de 3 como máximo quieres sumar?"))

contador_pares = 0
contador_impares = 0
contador_multiplo = 0
    
sumador_pares = 0
sumador_impares = 0
sumador_multiplo = 0

print('\n\n\n')
for i in range(1,11):
    if i % 3 == 0:
        if contador_multiplo < cuantos_multiplo:
            contador_multiplo = contador_multiplo + 1
            sumador_multiplo = sumador_multiplo+i
    if i % 2 == 0:
        if contador_pares < cuantos_pares:
            contador_pares = contador_pares + 1
            sumador_pares = sumador_pares+i
    else:
        if contador_impares < cuantos_impares:
            contador_impares = contador_impares + 1
            sumador_impares = sumador_impares+i
        
print('LA SUMA DE LOS PARES ES: \n')
print(sumador_pares)
print(' \n')

print('LA SUMA DE LOS IMPARES ES: \n')
print(sumador_impares)
print(' \n')

print('LA SUMA DE LOS MULTIPLOS DE 3 ES: \n')
print(sumador_multiplo)
print(' \n')



#9.	HACER UN PROGRAMA QUE LEA N NÚMEROS, CALCULE Y ESCRIBA LA SUMA DE LOS PARES Y EL PRODUCTO DE LOS IMPARES.
cuantos=int(input("¿Cúantos números deseas calcular?"))

sumador_pares = 0
producto_de_impares = 1

print('\n\n\n')
for i in range(1,cuantos+1):
 
    if i % 2 == 0:
        sumador_pares =sumador_pares+i
    else:
       producto_de_impares=producto_de_impares*i
        
print('LA SUMA DE LOS PARES ES: \n')
print(sumador_pares)
print(' \n')

print('EL PRODUCTO DE LOS IMPARES ES: \n')
print(producto_de_impares)
print(' \n')



#10. CALCULAR EL MÁXIMO DE N NÚMEROS LEÍDOS DESDE TECLADO.
#10. CALCULAR EL MÁXIMO DE N NÚMEROS LEÍDOS DESDE TECLADO.
cuantos = int(input('¿Cúantos números quieres insertar en pantalla?'))
numeros = []
for i in range(1,cuantos+1):
    b = int(input('Escribe el  numero # ' + str(i)))
    numeros.append(b)

numeros.sort(reverse = False)
print('El número más alto es '+ str(numeros[cuantos-1]))

