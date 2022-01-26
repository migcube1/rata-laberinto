# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:26:03 2017

@author: Miguel Leyva
"""

'''
---------------------------------------------------------------------------
                 PROYECTO DE LA RATA Y EL LABERINTO
---------------------------------------------------------------------------
                 ESTRUCTURAS DE DATOS Y ALGORITMOS I 
---------------------------------------------------------------------------
                 PROFESOR: GABRIEL CASTILLO HERNANDEZ
---------------------------------------------------------------------------
             GRUPO:  10                       SEMESTRE: 2017-2
---------------------------------------------------------------------------
AUTOR:  LEYVA BEJARANO MIGUEL ANGEL

'''

#Modulos importados:

import os,turtle,time
from turtle import *


#Variables Globales:

pila = []
visitados = []
obstaculos = []
vidaRaton = 0.00
columnas=0
renglones=0
respaldoVida=0
opcion=False

#======================================================>
# Funciones conforme al funcionamiento de laberinto:

def LeerLaberinto ():

    global renglones,columnas,vidaRaton,respaldoVida 

    #Abre el archivo .txt para leer el laberinto
    laberinto = open ("laberinto.txt","r")
   
    lista2=[]

    x=laberinto.readline()

    renglones=int(x[1:3])
    columnas=int(x[4:6])


    for linea in laberinto:
        
        i=0
        lista=[]
        
        #Crea una lista con los elementos de la primera linea del archivo
        while i != columnas:

            lista.append(linea[i]) 
            i+=1
         
        #Almacena la lista guardada, en otra lista y borra la primera lista   
        lista2.append(lista)
        del lista

    laberinto.close ()

    return lista2

laberinto = LeerLaberinto ()

def imprimeLaberinto (laberinto,raton,salida):

	global pila,vidaRaton,columnas,renglones

	#Se extraen las coordenadas del raton y la salida

	r,c =raton
	x,y =salida

	print("*****ENCUENTRA LA SALIDA*****")

	print ("\n------------------>")

	for i in range(0,renglones):

		lin=''

		for j in range(0,columnas):

			if raton != salida:

				#A las coordenadas del raton se la asigna la letra R

				if raton == (i,j):

					lin = lin + 'R'
				#A las coordenadas de la salida se la asigna la letra S

				elif salida == (i,j):

					lin = lin + 'S'
				#Si no se sigue imprimiendo lo diferente al raton y la salida
				else:

					lin= lin+laberinto[i][j]

			#En cuanto el raton llegue a la salida, la coordenda  se pinta con un #

			elif raton == salida:

				if raton == (i,j):

					lin = lin + '#'

				else:

					lin= lin+laberinto[i][j]

		print (lin)
	
	print ("------------------>\n")
	print ("Posición del raton: ",raton)
	print ("\n------------------>\n")
	print ("Vida del raton:",vidaRaton,"Puntos")
	print ("\n------------------>\n")
	"""print ("Pila:", pila)
	print ("\n------------------>\n")
	print ("Visitados:",visitados)
	print ("\n------------------>\n")"""

	return

#Saca un elemento de la pila   
def push (pila,p):

	pila.append(p)

	return
  
#Agrega un elemento a la pila
def pop (pila):
	try:
		pila.pop()

	except:

		return ()

#Regresa el último elemento introducido a la pila
def tos (pila):

	#Si Existen elemento en la lista retorna el ultimo elemento
	if len(pila) != 0:

		x=(len(pila))-1
		return pila[x]

	#Si no retorna una tupla vacia
	return ()

def visitado (pos):

	global visitados

	#si hay una coordenada que ya piso el raton devuelve un true 
	for elemento in visitados:

		if pos == elemento:

			return True
	#sino devuelve un false
	return False

def Salvandovida(raton,salida):
    
    global visitados
    puntos=[]
    distanciasp=[]
    #Como en movimiento considera todos los caminos  posibles y los guarda en puntos 
    
    derecha=(raton[0],raton[1]+1)
    arriba=(raton[0]-1,raton[1])
    izquierda=(raton[0],raton[1]-1)
    abajo=(raton[0]+1,raton[1])

    if camino(derecha)==True:
        if visitado(derecha)==False:
            puntos.append(derecha)
    if camino(arriba)==True:
        if visitado(arriba)==False:
            puntos.append(arriba)
    if camino(izquierda)==True:
        if visitado(izquierda)==False:
            puntos.append(izquierda)
    if camino(abajo)==True:
        if visitado(abajo)==False:
            puntos.append(abajo)
    #calcula y guarda la distancia de cada punto posible enocontrado 
    if len(puntos)!=0:
        for p in puntos:
            dis = (((p[0]-salida[0])**2)+((p[1]-salida[1])**2))**(0.5)
            distanciasp.append(dis)
   
    #obtiene el que tiene menor distancia y devuelve la coordenada
        mejor=min(distanciasp)
 
        for i in range(0,len(distanciasp)):
            if(distanciasp[i]==mejor):
                
                push(visitados,puntos[i])
                return puntos[i]
    else:
         return ()

def escojeAlgortimo ():

	global opcion, respaldoVida,vidaRaton

	x=0

	while x != 1 and  x != 2 :
		print("***ESCOJE ALGORITMO DE SIMULACIÓN***\n")
		print("1)Distancias\n")
		print ("2)Busqueda\n")
		
		x=int (input("Escoje una Opción:"))

		if x == 1:

			vidaRaton=((renglones*columnas)/10)
			respaldoVida=vidaRaton
			opcion = True

		if x == 2:

			vidaRaton=((renglones*columnas)/5)
			respaldoVida=vidaRaton
			opcion = False

		os.system("cls")

def camino(pos):

	global laberinto, obstaculos, renglones, columnas 
	
	caminos=[]

	for i in range (0,renglones):

		for j in range (0,columnas):

			#Genera una lista con las coordenadas donde el raton puede estar o pisar
			if  laberinto [i][j] != "X":

				caminos.append ((i,j))

			#Genera una lista con las coordenadas de los obstaculos del raton

			if laberinto [i][j] != "X" and laberinto [i][j] != " ":

				#if laberinto [i][j]!= "R" and laberinto [i][j]!= "S":

					obstaculos.append ((i,j))		

	
	#Si la coordenada que recibe esta función es una coordenada en donde puede estar el raton devuelve un true, si no un false
	for elemento in caminos:

		if pos == elemento:

			return True

	return False

def movimiento (raton):

	global visitados,laberinto,pila

	i,j=raton

	"""En esta función se revisa las coordenadas NORTE/SUR/ESTE/OESTE para determinar en cuales puede estar o avanzar
	el raton

	Ejemplo: El raton revisa el NORTE, para determinar si puede avanzar a esa coordenada, primero se verifica si la 
	coordenada a la que quiere avanzar es parte del camino, posterior se verifica si es un lugar  que ya visito, si 
	estas condiciones se cumplen, el raton puede avanzar y se agrega esa coordenada a la lista de visitado, si no 
	puede avanzar retorna una tupla vacia.

	"""

	#Norte
	if camino((i-1,j)) == True:

		if visitado ((i-1,j)) == False:

			raton = (i-1,j)
			push (visitados,raton)

			return raton

	#Este
	if camino((i,j+1)) == True:

		if visitado ((i,j+1)) == False:

			raton = (i,j+1)
			push (visitados,raton)

			return raton

	#Sur
	if camino((i+1,j)) == True:

		if visitado ((i+1,j)) == False:

			raton = (i+1,j)
			push (visitados,raton)

			return raton

	#Oeste
	if camino((i,j-1)) == True:

		if visitado ((i,j-1)) == False:

			raton = (i,j-1)
			push (visitados,raton)

			return raton
	
	return ()

#Determina la vida del raton
def vida (raton):

	global obstaculos, vidaRaton

	valoresObstaculos={'A':1.5,'L':3.5,'G':2,'F':4}

    #Si el raton pasa por algun obstaculo se lE bajan los puntos que anteriormente se le asignaron en el diccionario anteriormente
    #se verifica si las coordenadas del raton son igual al una coordenada del obstaculo
	if raton in obstaculos: 

		x,y=raton

		#se verifica que letra tiene esa obstaculo,  para determinar cuanta vida se le bajará al raton

		if laberinto[x][y] in valoresObstaculos:

			# se le resta la vida al raton

			vidaRaton-=valoresObstaculos[laberinto[x][y]]

	#Aqui se le baja 0.2 puntos por cada paso que pase en el laberinto
	else :

		vidaRaton-=0.2

	return vidaRaton

def algoritmoRecursivo (raton,salida):

	global laberinto,pila,visitados,respaldoVida,opcion

	vidaTotal = vida(raton)

	#se tomara una desicion dependiendo de la cantidad de vida del raton 
	if opcion == True and vidaTotal<=respaldoVida:

		movi=Salvandovida(raton,salida)

	elif opcion == False: 

	#Se obtiene una posible coordenada donde el raton puede estar   
		movi=movimiento (raton)


	#Si la vida del raton llega a 0 esté pues muere xD

	if vidaTotal <= 0:

		print ("¡El raton murió! :(")

		return

	#Si el raton no puede avanzar en las 4 coordenadas, este hace un back track, si y solo si existe una coordenada anterior a donde esta
	if movi == ():

		pop (pila)
		raton = tos (pila)

		#Si no existe Back track (retorno) se el raton esta en graves problemas, y el laberinto no tiene solucion

		if raton == ():

			print ("No existe Solución")

			return

		imprimeLaberinto (laberinto,raton,salida)

	
	#Entonces si existe una coordenada a la que el raton pueda moverse 
	elif movi != ():

		#el raton se mueve
		raton=movi
		#Se agrega el movimiento a la pila
		push (pila,raton)
		imprimeLaberinto (laberinto,raton,salida)


		#Cuando el raton llega a la salida 
		if salida == raton:
		
			print ("¡El raton llego a la salida!")

			return

	#input ("Presione una tecla para continuar...")
	time.sleep (0.5)
	os.system ("cls")

	algoritmoRecursivo (raton,salida)
#Se ingresan las coordenadas del raton
def coordRaton ():

	x=False

	while x == False:

		os.system("cls")

		print("*****COORDENADAS DEL RATON*****\n")

		print ("Coordenada del raton en x:")
		a=int (input ())
		print ("Coordenada del raton en y:")
		b=int (input ())

		x=camino ((a,b))

		if x == False:

			print("\n\n¡Esta coordenada no esta disponible, intenta con otra!")
			input ("Presiona una tecla para continuar...")
			os.system("cls")

	os.system("cls")
	return (a,b)
#Se ingresan las coordenadas del raton
def coordSalida ():

	x=False

	while x == False:

		os.system("cls")

		print("*****COORDENADAS DE LAS SALIDA*****\n")

		print ("Coordenada de la salida en x:")
		c=int (input ())
		print ("Coordenada de la salida en y:")
		d=int (input ())

		x=camino ((c,d))

		if x == False:

			print("\n\n¡Esta coordenada no esta disponible, intenta con otra!")
			input ("Presiona una tecla para continuar...")
			os.system("cls")

	os.system("cls")
	return (c,d)

#======================================================>
#Funciones conforme a la parte gráfica (turtle)

#Tamaño de la pantalla



def cuadrado ():
    
	begin_fill()

	for i in range(4):

		turtle.down()
		fd(20)
		rt(90)

	end_fill()

def graficaLaberinto(lista,Pila,raton,salida):
    
    global columnas,renglones

    title("Proyecto **La rata y el laberinto**- Estructuras de Datos y Algoritmos ")
    setup(1350,760,0,0)
    a = renglones*20
    b = columnas*20
    
    C = int(a/2)
    R = int(b/2)

    i=C

    up()
    penup()
    setposition(-R,i)
    shape("square")
    down()
    pendown()
    speed(1000000)

    entornoGrafico(raton)
    for r in range (0,renglones):
        for c in range (0,columnas):
            if lista[r][c] == 'X':
                fillcolor('gray')
                cuadrado()
            elif lista[r][c] == 'S':
                fillcolor('pink')
                cuadrado()
            elif lista[r][c] == 'L':
                fillcolor('yellow')
                cuadrado()
            elif lista[r][c] == 'A':
                fillcolor('blue')
                cuadrado()
            elif lista[r][c] == 'F':
                fillcolor('red')
                cuadrado()
            elif lista[r][c] == 'G':
                fillcolor('green')
                cuadrado()
            else:
                fillcolor('white')
                cuadrado()

            if raton == (r,c):
                fillcolor('brown')
                cuadrado()
            if salida == (r,c):
                fillcolor('black')
                cuadrado()
            fd(20)
        up()
        fd(20)
        rt(90)
        fd(20)
        rt(90)
        fd(220)
        rt(180)
        i-=20
        setposition(-R,i)
    
    penup()
    Caminar(Pila,R,C)

def PosicionRaton(R,C,rat):
    raton = pila[0]
    a = raton[0]*20
    b = raton[1]*20
    rat.setposition(-R+b+10,C-a-10)
        
    
    
def Caminar(Pila,R,C):

    i = 0
    raton = Pila[0]
    x,y=raton

    rat=turtle.Turtle()
    rat.setposition(0,0)
    rat.up()
    PosicionRaton(R,C,rat)
    rat.speed(0)
    rat.up()
    rat.shape("square")
    rat.pencolor('brown')
    rat.color('brown')
    rat.down()
    rat.pensize(5)
   
    for p in Pila:
        if len(Pila)-1 > i:
            
            i+=1
            raton = Pila[0+i]

        else:
            return

        if p[0] > raton[0]:

            rat.lt(90)
            rat.fd(20)
            rat.rt(90)

        elif p[0] < raton[0]:

            rat.rt(90)
            rat.fd(20)
            rat.lt(90)

        elif p[1] > raton[1]:
            
            rat.rt(180)
            rat.fd(20)
            rat.rt(180)

        elif p[1] < raton[1]:
            
            rat.fd(20)

        else:
            
            rat.rt(0)

        time.sleep(1)

def entornoGrafico (raton):

    global laberinto,vidaRaton,columnas,renglones
    a = renglones*20+200
    b = columnas*20+400
    setup(a,b,0,0)
    c = int(a/2)
    r = int(b/2)
    
	#Borde
    borde = turtle.Turtle()
    borde.speed(1000)
    borde.penup()
    borde.setposition(-c+50,-r+50)
    borde.pendown ()
    borde.pensize (3)

    for elemento in range (2):
        borde.forward (2*c)
        borde.left(90)
        borde.forward (2*r)
        borde.left(90)
        borde.hideturtle()

	#titulo

    borde.penup()
    borde.setposition(-50,320)
    borde.pendown ()
    borde.write ("PROYECTO DE LA RATA Y EL LABERINTO")

    borde.penup()
    borde.setposition(-50,280)
    borde.pendown ()
    borde.write ("Posición inicial del raton: ")
    borde.penup()
    borde.setposition(100,280)
    borde.pendown ()
    borde.write (raton)

#======================================================>	
def main():
    
    global laberinto,pila,visitados

    #Se le asignan coordenadas al raton y a la salida

    raton = coordRaton ()
    salida = coordSalida ()

    #Se escoje al algortimo con el que se moverá el raton

    escojeAlgortimo ()

    #se le asigna la coordenada inicial del raton a la pila
    push (pila,raton)

    imprimeLaberinto (laberinto,raton,salida)
    
    input("Presione una tecla para iniciar la simulación...")
    os.system("cls")

    algoritmoRecursivo (raton,salida)

    graficaLaberinto(laberinto,pila,raton,salida)
    
    done()
    
    input ("\nPresiona una tecla para continuar...")
    return 

main ()
