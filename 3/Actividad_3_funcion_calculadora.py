class calculadora:
    """La clase calculadora permite hacer algunas operaciones matematicas sencillas
    : Acepta dos parametros numericos enteros a y b
    : Las operaciones a realizar son 
    :suma
    :resta
    :multiplicacion
    :division

    para generar la documentación con la librería Pydoc debemos lanzar
    el siguiente comando en la terminal:
    pydoc -w <nombredelmodulo>
    esto genera un archivo html con mismo nombre en el mismo directorio
    con la documentación marcada como docstrings en el script

    """
    num1=int(input('Introduce el primer numero: '))
    num2=int(input('Introduce el segundo numero: '))

    def sumar():
        """Con esta funcion podemos sumar 2 valores,
        ambos valores deben estar en formato numerico
        y python automaticamente los convierte a numeros enteros"""
        a=calculadora.num1
        b=calculadora.num2
        suma=a+b        
        print(f'La suma de {a} y {b} es {suma}')
    
    def restar():
        """Con esta funcion podemos restar 2 valores,
        ambos valores deben estar en formato numerico
        y python automaticamente los convierte a numeros enteros"""
        a=calculadora.num1
        b=calculadora.num2
        resta=a-b
        print(f'La resta de {a} menos {b} es {resta}')

    def multiplicar():
        """Con esta funcion podemos multiplicar 2 valores,
        ambos valores deben estar en formato numerico
        y python automaticamente los convierte a numeros enteros"""
        a=calculadora.num1
        b=calculadora.num2
        mul=a*b
        print(f'La multiplicación de {a} por {b} es {mul}')
         
    def dividir():
        """
        Con esta funcion podemos dividir dos valores numericos. 
        Antes de realizar la operación Python valida que el denominador 
        no es igual a 0, en caso de que sea 0 nos devolverá un error.
        """
        a=calculadora.num1
        b=calculadora.num2
        if b==0:
            print('No se puede dividir entre 0')
        else:
            a/b
            print(f'La division de {a} entre {b} es {a/b}')

    def aplicacion():
        """Con esta funcion inicializamos la aplicacion:
        se inicializará un bucle con 5 opciones, cada una de ellas llamará a una función
        mientras que la numero 5 detendra el bucle y saldra de el, finalizando la aplicacion"""     
        salir=False

        while salir==False:
                print('''¿Que operación quieres realizar?
                1 - sumar
                2 - restar
                3 - multiplicar
                4 - dividr
                5 - exit''')
                
                operacion=int(input())


                if operacion==1:
                    calcular=calculadora()
                    calculadora.sumar()
                elif operacion==2:
                    calcular=calculadora()
                    calculadora.restar()
                elif operacion==3:
                    calcular=calculadora()
                    calculadora.multiplicar()
                elif operacion==4:
                    calcular=calculadora()
                    calculadora.dividir()
                elif operacion==5:
                    print('Has salido del programa')
                    salir=True
                else:
                    print('Debes introducir una opcion valida')


