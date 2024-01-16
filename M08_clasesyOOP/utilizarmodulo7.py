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
        print([max,cuentarep2[index]])
    
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