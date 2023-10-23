#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
x=5
if (x > 0):
    print('Mayor que 0')
elif(x < 0):
    print ('Menor que 0')




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
x=5
y=6
if (type(x) == type(y)):
    print('Son mismo tipo de dato')





# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1,20):
    if (i % 2 == 0):
        print (str(i)+' es par')
    else:
        print (str(i)+' es impar')



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(0,5):
    print(i**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
n=5
for n in range(0,n):
    print (n)




# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
fact = 5
if (type(fact) == int):
    if (fact > 0):
         x=fact-1
         while (x > 0):
            fact = fact * x
            x-=1
         print('El factorial es', fact)
    else:
            print('no es mayor que 0')
else:
    print('no es entero')




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
x=5
while (x > 0):
    for i in range(0,5):
        x-=1
        print(x)



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
x=5
for i in range(0,5):
    while (x > 0):
        x-=1
        print(x)





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
primo = True
for i in range(0,30):
    for j in range(2,i):
        if (i % j == 0):
           primo = False 
    if (primo):
        print (i,'es primo')
    primo = True





# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
primo = True
for i in range(0,30):
    for j in range(2,i):
        if i%j == 0:
           primo = False
           break 
    if primo:
        print (i,'es primo')
    primo = True





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
ciclos_sin_break = 0
primo = True
for i in range(0,30):
    for j in range(2,i):
        ciclos_sin_break += 1
        if (i % j == 0):
           primo = False 
    if primo:
        print (i,'es primo')
    primo = True
print (ciclos_sin_break)


# In[57]:
ciclos_con_break = 0
primo = True
for i in range(0,30):
    for j in range(2,i):
        ciclos_con_break += 1
        if (i % j == 0):
           primo = False
           break 
    if primo:
        print (i,'es primo')
    primo = True
print (ciclos_con_break)
print ((ciclos_con_break/ciclos_sin_break)*100)



# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
n=99
topefin=300
while (n <= topefin):
    n += 1
    if (n % 12 != 0):
            continue
    print(n)
    




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
y = input('Enter number')
x = int(y)
primo = True
siguiente = True
while (siguiente):
    if (type(x) == int):
        for j in range(2,x):
            if (x % j == 0):
                primo = False
        if primo:
            print (x,'primo')
        else:
            print(x,'no es primo')
        primo=True
    else:
        print(x,'El número no es entero')
    s = input ('siguiente? S/N')
    if (s == 's' or s == 'S'):
        siguiente = True
    else:
        siguiente = False


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

n=99
topefin=300
while (n <= topefin):
    n += 1
    if ((n % 6 != 0) and (type (n / 6)) != int):
            continue
    print(n) 


# %%
