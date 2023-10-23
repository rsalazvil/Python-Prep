#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
x=3
print(x)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(x))




# 4) Crear una variable que contenga tu nombre

# In[2]:

y='Rafael'


# 5) Crear una variable que contenga un número complejo

# In[3]:
z=8j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

type(z)



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416



# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

l= True
m=True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(l))
print(type(m))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
k=3+3.5




# 11) Realizar una operación de suma de números complejos

# In[2]:

5j+6j



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
8+5j





# 13) Realizar una operación de multiplicación

# In[5]:
8*8





# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

d=27 / 4
print(d)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
int(d)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
27 % 4




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

int(d)*4 + 27%4 


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
x = 'hh'
y = '22'
x+y




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
2=='2'




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

2 == int('2')



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float('3.8')

#POrque está configurado el punto y no la coma para representar números flotantes

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
b=3
b-=1




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1 << 2
# 1 es igual a 0001 en binario y con la operaciòn 1<<2 queda 0100 que es 4. En el sistema de numeración binario los números se representan con ceros y unos



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
2+'2'


#porque los 2 y '2' son de diferente tipo. Si los operandos  son del mismo tipo los resultados pueden ser diferentes 2+2 es cuatro pero '2'+'2' es '22'


# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

2 + int('2')


# %%
