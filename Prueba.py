import random
import os
import time
global posicion
global tabla

tabla=[]
class juegocarros:

    def __init__(self,nombre,ncarro,ncarriles):
        self.__ncarro=ncarro
        self.ncarriles=ncarriles
        self.distancia=1500
        self.nombre=nombre
        self.posicion=5

    def estado(self):
        print("Nombre de jugador: ",self.nombre,"\n numero de carril: ",self.ncarriles,"\n Carro: ",self.__ncarro,
        "\n Distancia : ",self.distancia,"m")

    def Dados(self):
            dado = random.randint(1, 6)
            recorrido=dado*100
            self.distancia=self.distancia-recorrido
            print("valor de dado",dado,"\nen metros ",recorrido,"m")
            print("Nueva distancia",self.distancia,"m")

   
def f_ganadores(tabla,nombre):
    f=tabla.count(nombre)
    print("El jugador ",nombre,"ha ganado",f,"veces")
    exit() 

def menu():
 a=1
 b=1
 c=1
 d=1
 e=1
 jugador1=juegocarros("Rafael","Honda","2")
 jugador2=juegocarros("Antonio","Susuki","3")
 jugador3=juegocarros("Marco","Hionda","4")
 jugador4=juegocarros("Julio","BMW","5")
 jugador5=juegocarros("Andrea","Renault","1")
 posicion=[]
 while(True):
     tirar=input("Para tirar los dados presione enter")
     if(a==1):
        jugador1.estado()
        jugador1.Dados()
             
        if(jugador1.distancia<=0):
            print("llegaste a la meta")
            posicion.append(jugador1.nombre)
            a=0
     print("siguiente jugador")    
     tirar=input("Para tirar los dados presione enter")
     if(tirar==""):
        if(b==1):
            jugador2.estado()
            jugador2.Dados()
            
            if(jugador2.distancia<=0):
                print("llegaste a la meta")
                posicion.append(jugador2.nombre)
                b=0
     print("siguiente jugador")    
     tirar=input("Para tirar los dados presione enter")
     if(tirar==""):
        if(c==1):
            jugador3.estado()
            jugador3.Dados()
            
            if(jugador3.distancia<=0):
                print("llegaste a la meta")
                posicion.append(jugador3.nombre)
                c=0
     print("siguiente jugador")    

     tirar=input("Para tirar los dados presione enter")
     if(tirar==""):
        if(d==1):
            jugador4.estado()
            jugador4.Dados()
            
            if(jugador4.distancia<=0):
                print("llegaste a la meta")
                posicion.append(jugador4.nombre)
                d=0

     print("siguiente jugador")    

     tirar=input("Para tirar los dados presione enter")
     if(tirar==""):
        if(e==1):
            jugador5.estado()
            jugador5.Dados()
            
            if(jugador5.distancia<=0):
                print("llegaste a la meta")
                posicion.append(jugador5.nombre)
                e=0
    

     time.sleep(3)
     os.system ("cls")
     print("siguiente ronda")
     if(len(posicion)>=3):
        print(" finalistas \n Primer lugar",posicion[0],"\n Segundo lugar",posicion[1],"\n Tercer lugar",posicion[2])
        tabla.extend(posicion)
        t=input("¿Quieres saber cuantas veces gano un jugador? \n si  \n no \n")
        if(t=="si"):
            jug =input("Ingrese el nombre del jugador: ")
            f_ganadores(tabla,jug)
        if(t=="no"):
            iniciar=input("¿Quieres jugar de nuevo? \n si  \n no \n")
            if(iniciar=="no"):
                 print("fin del juego")
                 exit() 
            elif(iniciar=="si"):
                menu() 
        

iniciar=input("iniciar juego \n si  \n no \n")
if (iniciar=="si"):
   
    menu()
elif(iniciar=="no"):
    print("fin del juego")
    




  










