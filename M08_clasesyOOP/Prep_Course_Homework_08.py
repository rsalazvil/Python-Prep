#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor


# In[1]:

class Vehículo:
    def __init__(self,Color,Tipo,Cilindrada):
        self.Color = Color
        self.Tipo = Tipo
        self.Cilindrada = Cilindrada   
    


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:

class Vehículo:
    def __init__(self,Color,Tipo,Cilindrada):
        self.Color = Color
        self.Tipo = Tipo
        self.Cilindrada = Cilindrada
    
    def Acelerador(self):
        print("acelerando")
    
    def Frenar(self):
        print("frenando")

    def Doblar(self):
        print("doblando")
        



# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
vehículo1 = Vehículo('amarillo','taxi',1300)
vehículo2 = Vehículo('Negro','limo',2000)
vehículo3 = Vehículo('plata','moto',500)

vehículo1.Acelerador()
vehículo2.Frenar()
vehículo3.Doblar()




# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

class Vehículo:
    def __init__(self,Color,Tipo,Cilindrada,Velocidad,Dirección,):
        self.Color = Color
        self.Tipo = Tipo
        self.Cilindrada = Cilindrada
        self.Velocidad = Velocidad
        self.Dirección = Dirección
    
    def Acelerador(self):
        print("acelerando")
    
    def Frenar(self):
        print("frenando")

    def Doblar(self):
        print("doblando")
    
    def Estado(self):
        print("Velocidad",self.Velocidad,"Dirección",self.Dirección)
    
    def Descripción(self):
        print("Color ",self.Color,"Tipo ",self.Tipo, "Cilindrada ", self.Cilindrada)
        
    




# In[13]:

vehículo1 = Vehículo('amarillo','taxi',1300,'50Km/h','Norte')
vehículo2 = Vehículo('Negro','limo',2000,'60km/h','Sur')
vehículo3 = Vehículo('plata','moto',500,'30Km/h','Occidente')

vehículo1.Acelerador()
vehículo1.Descripción()
vehículo1.Estado()
vehículo2.Frenar()
vehículo2.Descripción()
vehículo2.Estado()
vehículo3.Doblar()
vehículo3.Descripción()
vehículo3.Estado()




# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:
class Utilizarmodulo7:
    def __init__(self)-> None:
        pass
        
    def esprimo(self,numero):
        i=2
        esprim = True
        while i < numero:
            if numero%i == 0:
                esprim = False
            i+=1
        return esprim  
    
    def devuelvemasrepetido(self,lista):
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
    
    def conviertegrados(self,valor,origen,destino):
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
    
    def factorial(self, numero):
        i = numero
        valor = 1
        while i > 0:
            valor = valor * i
            i-=1
        return valor

# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:
U = Utilizarmodulo7()
print (U.esprimo(7))
print (U.devuelvemasrepetido([1,10,1,10,2,2,2,3]))
print (U.conviertegrados(18,'Celsius','Kelvin'))
print (U.factorial(10))

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:
class Utilizarmodulo7:
    def __init__(self,lista):
        self.lista = lista

    def esprimo(self):
        for k in self.lista:
            if self.__esprim(k):
                print(k, "Es primo")
            else:
                print(k, "No es primo")

    def conviertegrados(self,origen,destino):
        for k in self.lista:
            print(self.__conviertegrados1(k,origen,destino))
    
    def factorial(self):
        for k in self.lista:
            print(self.__factorial1(k))
        
    def __esprim(self,numero):
        i=2
        espri = True
        while i < numero:
            if numero%i == 0:
                espri = False
            i+=1
        return espri
  
    
    def devuelvemasrepetido(self):
        cuentarep = []
        cuentarep2= []
        for i,e in enumerate(self.lista):
            cuentarep.insert(i,0)
            for j in self.lista:
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
    
    def __conviertegrados1(self,valor,origen,destino):
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
    
    def __factorial1(self, numero):
        i = numero
        valor = 1
        while i > 0:
            valor = valor * i
            i-=1
        return valor
    
# In[56]
u = Utilizarmodulo7([1,10,1,10,2,2,2,3])

# In[57]

u.esprimo()

# In[58]

u.conviertegrados('Celsius','Kelvin')

# In[60]

u.devuelvemasrepetido()


# In[61]

u.factorial()

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:

from utilizarmodulo7 import *

# In[2]

u = Utilizarmodulo7([1,10,1,10,2,2,2,3,4,4,4,4])

# In[3]

u.esprimo()
u.conviertegrados("Celsius","Farenheit")
u.factorial()

# In[4]

u.devuelvemasrepetido()

# %%
