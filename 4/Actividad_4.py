lista=[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

#Expresion normal
for i in lista:
    print(max(i))

#Expresion comprimida
print([max(i) for i in lista])

lista2=[3, 4, 8, 5, 5, 22, 13]

#definimos funcion que comprueba si un numero es primo o no
def primo(n):
    for i in range(2, int(n ** 0.5) + 1):
        if (n%i) == 0:
            return False
    return n

""" usamos la funcion filter para crear una lista que pasa cada uno de los valores
de la lista2 por la funcion primo. Si es primo, devuelve True y lo mete en la lista 
primos, en caso contrario, lo deja fuera """

primos=list(filter(primo,lista2))

print (primos)