#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:


def esprimo(numero):
    i=2
    esprimo = True
    while i < numero:
        if numero%i == 0:
            esprimo = False
        i+=1
    return esprimo




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def devuelveprimos(lista):
    listaprimos = []
    for numero in lista:
        if esprimo(numero):
            listaprimos.append(numero) 
    return listaprimos


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def devuelvemasrepetido(lista):
    cuentarep = []
    cuentarep2= []
    for i,e in enumerate(lista):
        cuentarep.insert(i,0)
        for j in lista:
            if e == j:
                cuentarep[i] = cuentarep[i]+1
                cuentarep2.insert(i,e)
    max = 0
    index = 0
    for j,c in enumerate(cuentarep):
        if c > max:
            max = c
            index = j
    return [max,cuentarep2[index]]
            


# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def conviertegrados(valor,origen,destino):
    if origen == 'Celsius' and  destino == 'Farenheit':
        return (valor*9/5) +32
    else:
        if origen == 'Celsius' and  destino == 'Kelvin':
            return valor + 273.15
        else:
            if origen == 'Farenheit' and  destino == 'Celsius':
                return (valor - 32)*(5/9)
            else:
                if origen == 'Farenheit' and  destino == 'Kelvin':
                    return (valor - 32)*(5/9) + 273.15
                else:
                    if origen == 'Kelvin' and  destino == 'Celsius':
                        return valor - 273.15
                    else:
                        if origen == 'Kelvin' and  destino == 'Farenheit':
                            return ((valor - 273.15)*9/5)+32
             
# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

Lista = [30,'Celsius','Farenheit',30,'Celsius','Kelvin',86,'Farenheit','Celsius',86,'Farenheit','Kelvin',303.15,'Kelvin','Celsius',303.15,'Kelvin','Farenheit']
i=0
while i < len(Lista)-2:
    print (conviertegrados(Lista[i],Lista[i+1],Lista[i+2]))
    i+=3

# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def factorial(numero):
    i = numero
    valor = 1
    while i > 0:
        valor = valor * i
        i-=1
    return valor



# %%
