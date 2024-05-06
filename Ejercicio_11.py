
# CODE:28
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Comience por generar el bucle While True
- Dentro del bucle imprima con prints el menú
  de opciones en consola.

- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada operacion
  para almacenar la operación que se desea efectuar
  ingresada por consola con la función input
  Los valores que puede tomar la variable operacion van
  del "1" al "5", su programa no debe explotar si se ingresa
  otro texto distinto.

IMPORTANTE: Dentro del bucle primero debe solicitar al usuario
el ingreso de los dos números (numero_1 y numero_2) y luego
debe solicitar el ingreso de la operación a realizar
(debe respetar ese orden)

- Armar una serie de condicionales para evaluar
  que operación efectuar. Deberá guardar el resultado
  de la operación en una variable llamada resultado

- Si el usuario ingresa la operación de SALIR (opcion 5),
  deberá finalizar el bucle con la sentencia break.

- Si el usuario ingresa una opción fuera del rango
  solicitado de opciones, el programa no deberá 
  estallar, no deberá hacer nada permitiendo
  que el bucle While vuelva a realizar la consulta
  en la próxima iteración.
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:
    print('mune de operaciones: ')
    print('1. suma')
    print('2. resta')
    print('3. multiplicacion')
    print('4. division')
    print('5. salir ')

    numero_1 = float(input('Ingrese el primer numero: '))
    numero_2 = float(input('Ingrese el segundo numero: '))
    operacion = input('Ingrese la operacion a realizar (1 al 5):')

    if operacion == '1':
        resultado = numero_1 + numero_2
        print(f'el resultado de la suma es :{resultado}')
    elif operacion == '2':
        resultado = numero_1 - numero_2
        print(f'El resultado de la resta es: {resultado}')
    elif operacion =='3':
        resultado = numero_1 * numero_2
        print(f'El resultado de la multiplicacion es: {resultado}')
    elif operacion == '4':
        if numero_2 != 0:
            resultado = numero_1 / numero_2
            print("El resultado de la división es:", resultado)
        else:
            print("Error: No se puede dividir entre cero.")
    elif operacion == '5':
        print("Saliendo del programa...")
        break
