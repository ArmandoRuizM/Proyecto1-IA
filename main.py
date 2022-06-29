from ast import operator
from multiprocessing import parent_process
from typing_extensions import Self
import numpy as np
from turtle import *
import time

# #Crear pen
# class Pen(turtle.Turtle):
#   def __init__(self):
#     turtle.Turtle.__init__(self)
#     self.shape("square")
#     self.color()
#     self.penup()
#     self.speed(0)
    
# #Diccionario de Colores
# Colores={
#   "0": "white",
#   "1": "brown",
#   "2": "blue",
#   "3": "green",
#   "4": "purple",
#   "5": "yellow",
#   "6": "red"
# }

##Función para configurar la pantalla que muestra el ambiente:
GUI = Screen()
GUI.bgcolor("Black")
GUI.title("ProyectoIA")
GUI.setup(500,500)
GUI.tracer(0)

def confLaberinto(Laberinto):
    for y in range(len(Laberinto)):
      for x in range(len(Laberinto[y])):
        speed(10)
        cuadro = Laberinto[y][x]
        screen_x = -250 + (x*50) 
        screen_y = 250 - (y*50)
        if cuadro == 0:
          fillcolor("white")
        elif cuadro == 1:
          fillcolor("brown")
        elif cuadro == 2:
          fillcolor("blue")
        elif cuadro == 3:
          fillcolor("green")
        elif cuadro == 4:
          fillcolor("purple")
        elif cuadro == 5:
          fillcolor("yellow")
        elif cuadro == 6:
          fillcolor("red")
        pencolor("black")
        begin_fill()
        goto(screen_x, screen_y-50)
        goto(screen_x, screen_y)
        goto(screen_x+50, screen_y)
        goto(screen_x+50, screen_y-50)
        goto(screen_x, screen_y-50)
        end_fill()
        

def prueba():
  pensize(1)
  pencolor("white")
  fillcolor("white")
  begin_fill()
  goto(-250, 250)
  goto(-250+50, 250)
  goto(-250+50, 250-50)
  goto(-250, 250-50)
  goto(-250, 250)
  end_fill()

def reading(dir):
  file = open(dir,"r")
  string1 = file.read()
  lineas = string1.splitlines()
  laberinto = [10]*10

  for i in range(len(laberinto)):
        aux=lineas[i]
        laberinto[i]=aux.split(' ')

  laberinto = np.array(laberinto,int)
  file.close()
  return laberinto
  
 #Se carga el laberinto a la variable maze que se usa en todo lado
maze=reading("Prueba1.txt")

def drawSolution(solution):
  x0=-1
  y0=-1
  #Se determina cual es la posición inicial del agente
  for i in range(len(maze)):
    for j in range(len(maze)):
      if(maze[i][j]==2):
        x0=i
        y0=j
  screen_x=-250+(x0*50)
  screen_y=250-(y0*50)
  speed(5)
  pencolor("black")
  fillcolor("white")
  begin_fill()
  goto(screen_x, screen_y-50)
  goto(screen_x, screen_y)
  goto(screen_x+50, screen_y)
  goto(screen_x+50, screen_y-50)
  goto(screen_x, screen_y-50)
  end_fill()
  solution[0].pop()
  for i in reversed(solution[0]):
    if i==0:
      screen_x=screen_x-50
      pencolor("black")
      fillcolor("blue")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_x=screen_x+50
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
      elif maze[x0][y0]==1:
        fillcolor("brown")
      elif maze[x0][y0]==2:
        fillcolor("white")
      elif maze[x0][y0]==3:
        fillcolor("green")
      elif maze[x0][y0]==4:
        fillcolor("purple")
      elif maze[x0][y0]==5:
        fillcolor("white")
      elif maze[x0][y0]==6:
        fillcolor("red")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_x=screen_x-50
      x0=x0-1
    elif i==1:
      screen_y=screen_y+50
      pencolor("black")
      fillcolor("blue")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_y=screen_y-50
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
      elif maze[x0][y0]==1:
        fillcolor("brown")
      elif maze[x0][y0]==2:
        fillcolor("white")
      elif maze[x0][y0]==3:
        fillcolor("green")
      elif maze[x0][y0]==4:
        fillcolor("purple")
      elif maze[x0][y0]==5:
        fillcolor("white")
      elif maze[x0][y0]==6:
        fillcolor("red")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_y=screen_y+50
      y0=y0-1
    elif i==2:
      screen_x=screen_x+50
      pencolor("black")
      fillcolor("blue")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_x=screen_x-50
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
      elif maze[x0][y0]==1:
        fillcolor("brown")
      elif maze[x0][y0]==2:
        fillcolor("white")
      elif maze[x0][y0]==3:
        fillcolor("green")
      elif maze[x0][y0]==4:
        fillcolor("purple")
      elif maze[x0][y0]==5:
        fillcolor("white")
      elif maze[x0][y0]==6:
        fillcolor("red")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_x=screen_x+50
      x0=x0+1
    elif i==3:
      screen_y=screen_y-50
      pencolor("black")
      fillcolor("blue")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_y=screen_y+50
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
      elif maze[x0][y0]==1:
        fillcolor("brown")
      elif maze[x0][y0]==2:
        fillcolor("white")
      elif maze[x0][y0]==3:
        fillcolor("green")
      elif maze[x0][y0]==4:
        fillcolor("purple")
      elif maze[x0][y0]==5:
        fillcolor("white")
      elif maze[x0][y0]==6:
        fillcolor("red")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      screen_y=screen_y-50
      y0=y0+1



 ##############################################################################################
 # IMPLEMENTACIÓN DE ALGORITMO DE BÚSQUEDA POR PROFUNDIDAD EVITANDO CICLOS, POR ARMANDO RUIZ: #                        
 ##############################################################################################
 #Implementación de un tipo de dato pila, para la implementación del algoritmo de búsqueda por profundidad (robado de internet)
class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0

    def showStack(self):
        print(self.elements)

#Se define la clase Depth first search node, usada para implementar el algoritmo de búsqueda preferente por profundidad
class DfsNode:
  #Se define el método constructor
  def __init__(self, status, parent, operator, depth):
    self.status = status
    self.parent = parent
    self.operator = operator
    self.depth = depth

  #Método bobo
  def ImNode(self):
    return "Hola, soy un nodo"

  #Método que recibe un entero entre 0 y 3, y mueve el agente en una dirección, 0=izquierda, 1=arriba, 2=derecha, 3=abajo y retorna el nuevo estado en el que se encuentra el agente
  def move(self, direction):
    newStatus=self.status.copy()
    #Se realiza el cambio en la posición de acuerdo al operador que se usa:
    if direction == 0:#izquierda
      newStatus[1]=self.status[1]-1
    if direction == 1:#arriba
      newStatus[0]=self.status[0]-1
    if direction == 2:#derecha
      newStatus[1]=self.status[1]+1
    if direction == 3:#abajo
      newStatus[0]=self.status[0]+1
    #Luego se verifican los demás posibles cambios en el estado
    #Se verifica los casos en los que llega a un item
    if (newStatus[2]==True and newStatus[3]==False): #Se mira si ya se tomó un objeto, entonces se va a tomar un segundo
      if not (newStatus[0]==newStatus[4] and newStatus[1]==newStatus[5]): #Si no está tratando de coger el objeto que ya había cogido
        if maze[newStatus[0]][newStatus[1]]==5:
          #Se dice que se tomó un primer objeto y se guarda sus coordenadas para evitar ciclos
          newStatus[3]=True

    if not (newStatus[2] and newStatus[3]): #Se mira si es el primer objeto que coge
      #Se verifica si cayó en un item y lo toma
      if maze[newStatus[0]][newStatus[1]]==5:
        #Se dice que se tomó un primer objeto y se guarda sus coordenadas para evitar ciclos
        newStatus[2]=True
        newStatus[4]=newStatus[0]
        newStatus[5]=newStatus[1]
    
    return newStatus

  #Getter del estado del nodo
  def getStatus(self):
    return self.status

  #Getter del padre del nodo
  def getParent(self):
    return self.parent

  #Getter de la profundidad del nodo
  def getDepth(self):
    return self.depth

  #Getter del operador del nodo
  def getOperator(self):
    return self.operator

  #Método que retorna si se llegó a la meta o no
  def solution(self):
    if (self.status[2] and self.status[3]):
      return True
    else:
      return False
  

#Para la búsqueda preferente por profundidad, un estado será una lista de la siguiente manera:
#[posición en X, posición en Y, cogió item1?, cogió item2?, coordenada X del item1, coordenada y del item1]
#se debe determinar cuál es el estado inicial para construir el nodo raíz:
def initStatus(maze):
  status=[0,0,False,False,-1,-1]
  for i in range(len(maze)):
    for j in range(len(maze)):
      if(maze[i][j]==2):
        status=[i,j,False,False, -1, -1]
  return status

#Método que recibe un estado y con base en este determina en qué direcciones se podría mover el agente
def radar(status):
  allowedMoves=[False, False, False, False]
  if not status[1]==0:#no se encuentra en la primera columna, se examina el movimiento hacia la izquierda
    if maze[status[0]][status[1]-1]!=1:#Si no es un muro
      allowedMoves[0]=True #Se puede mover hacia la izquierda
  if not status[0]==0:#no se encuentra en la fila de arriba, se examina ese movimiento
    if maze[status[0]-1][status[1]]!=1:#Si no es un muro
      allowedMoves[1]=True#Se puede mover hacia arriba
  if not status[1]==9:#No se encuentra en la última columna, se examina el movimiento hacia la derecha
    if maze[status[0]][status[1]+1]!=1:#Si no es un muro
      allowedMoves[2]=True#Se puede mover hacia la derecha
  if not status[0]==9:#no se encuentra en la fila de abajo, se examina ese movimiento
    if maze[status[0]+1][status[1]]!=1:#Si no es un muro
      allowedMoves[3]=True#Se puede mover hacia abajo
  return allowedMoves

#Método que recibe un estado y un nodo, para compararlos y determinar si el agente ya se ha encontrado en ese estado antes, es decir, hay un ciclo
def thereIsCycle(status, node):
  auxNode=node
  #Empezamos suponiendo que no hay un ciclo
  cycle = False
  if node.getParent() is None: #Si el nodo no tiene padre
    #No hace falta verificar jaja
    control = False
  else: #Si el nodo tiene padre
    #Puede existir un ciclo, toca verificar
    control = True

  while control:
    auxNode=auxNode.getParent() #Setteamos el nodo auxiliar como el padre del nodo
    if status==auxNode.getStatus(): #Revisamos si el estado que se verifica es igual al estado del nodo auxiliar
      #Decimos que hay un ciclo
      cycle = True
      control = False

    if auxNode.getParent() is None: #Revisamos si el nodo aún tiene un padre o ya se acabaron
      #Si ya se acabaron, se termina el while
      control = False

  return cycle

#Método que recibe un nodo y METE SUS HIJOS A LA PILA, esto es después de verificar que el nodo no era una meta
def expandNode(node):
  allowedMoves=radar(node.getStatus()) #Determinamos en qué direcciones debería poderse mover el agente
  children = [None, None, None, None]

  if allowedMoves[0]: #Miramos si se puede mover a la izquierda
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(0), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[0]=DfsNode(node.move(0), node, 0, node.getDepth()+1)

  if allowedMoves[1]: #Miramos si se puede mover hacia arriba
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(1), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[1]=DfsNode(node.move(1), node, 1, node.getDepth()+1)

  if allowedMoves[2]: #Miramos si se puede mover a la derecha
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(2), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[2]=DfsNode(node.move(2), node, 2, node.getDepth()+1)

  if allowedMoves[3]: #Miramos si se puede mover abajo
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(3), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[3]=DfsNode(node.move(3), node, 3, node.getDepth()+1)

  return children

def getPath(node):
  auxNode=node
  #Empezamos creando un arreglo para guardar los movimientos en orden
  path = []
  if node.getParent() is None: #Si el nodo no tiene padre
    #No hace falta verificar jaja
    control = False
  else: #Si el nodo tiene padre
    #Puede existir un ciclo, toca verificar
    control = True

  while control:
    path.append(auxNode.getOperator())
    if auxNode.getParent() is None: #Revisamos si el nodo aún tiene un padre o ya se acabaron
      #Si ya se acabaron, se termina el while
      control = False
    auxNode=auxNode.getParent() #Setteamos el nodo auxiliar como el padre del nodo

  return path

def dfsSolve():
  #Contador de nodos expandidos
  startTime = time.time()
  expandedNodes = 0
  #Se crea la pila
  dfsTree = Stack()
  #Se le añade el nodo raíz
  dfsTree.push(DfsNode(initStatus(maze),None,None,0))
  go = True
  #Se inicia un bucle que solo termina al encontrar solución o decir que no existe una
  while go:
    #Si no quedaron nodos a expandir y ninguno fue meta, se dice que no existe solución
    if dfsTree.is_empty():
      return None
    #Se guarda el nodo raíz en n
    n=dfsTree.peek()
    #Se saca el nodo raíz de la pila
    dfsTree.pop()
    expandedNodes+=1
    if n.solution(): #Se determina si el nodo raíz es meta
      finishTime = str(time.time()-startTime)
      solution = [getPath(n), expandedNodes, n.getDepth(), finishTime]
      #De ser así, se dice que existe solución
      return solution
    else:
      #Si no es meta, entonces se expande
      createdNodes = expandNode(n)
      if not createdNodes[3] is None:
        dfsTree.push(createdNodes[3])
      if not createdNodes[2] is None:
        dfsTree.push(createdNodes[2])
      if not createdNodes[1] is None:
        dfsTree.push(createdNodes[1])
      if not createdNodes[0] is None:
        dfsTree.push(createdNodes[0])


###################################################
# CONTROL DE FLUJO DEL PROYECTO, POR ARMANDO RUIZ:#
###################################################
#variable que permite al programa saber si sigue o para
firstMenu = True

while(firstMenu):
  print("Bienvenido al proyecto #1 de Introduccion a la inteligencia artificial, a continuacion ingrese la opcion deseada:\n1. Mostrar ambiente inicial.\n2. Resolver con algoritmo de busqueda no informada.\n3. Resolver con algoritmo de busqueda informada.\n4. Terminar ejecucion.")
  menu1 = input("Esperando opcion...\n")
  if menu1 == "1":
    secondMenu = True
    while(secondMenu):
      confLaberinto(maze)
      #prueba()
      print("Mostrando ambiente inicial.\n1. Regresar al menu principal.\n2. Terminar ejecución.")
      menu2 = input("Esperando opcion...\n")
      if menu2 == "1":
        GUI.clear()
        GUI.reset()
        secondMenu = False
      elif menu2 == "2":
        secondMenu = False
        firstMenu = False
      else:
        print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
  elif menu1 == "2":
    secondMenu = True
    while(secondMenu):
      print("Seleccione uno de los siguientes algoritmos de busqueda no informada:\n1. Amplitud.\n2. Costo uniforme.\n3. Profundidad evitando ciclos.\n4. Regresar al menu principal.\n5. Terminar ejecución.")
      menu2 = input("Esperando opcion...\n")
      if menu2 == "1":
        thirdMenu = True
        while(thirdMenu):
          print("Mostrando solución por amplitud.\n1. Regresar al menu anterior.\n2. Terminar ejecución.")
          menu3 = input("Esperando opcion...\n")
          if menu3 == "1":
            thirdMenu = False
          elif menu3 == "2":
            thirdMenu = False
            secondMenu = False
            firstMenu = False
          else:
            print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
      elif menu2 == "2":
        thirdMenu = True
        while(thirdMenu):
          print("Mostrando solución por costo uniforme.\n1. Regresar al menu anterior.\n2. Terminar ejecución.")
          menu3 = input("Esperando opcion...\n")
          if menu3 == "1":
            thirdMenu = False
          elif menu3 == "2":
            thirdMenu = False
            secondMenu = False
            firstMenu = False
          else:
            print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
      elif menu2 == "3":
        thirdMenu = True
        while(thirdMenu):
          solution = dfsSolve()
          if solution is not None:
            print("La búsqueda fue exitosa :)\nSe expandieron "+str(solution[1])+ " nodos.\nLa profundidad del arbol es "+str(solution[2])+"\nLa búsqueda terminó en "+solution[3]+"ms")
          else:
            print("No se pudo encontrar una solución :(")
          confLaberinto(maze)
          drawSolution(solution)
          print("Mostrando solución profundidad evitando ciclos.\n1. Regresar al menu anterior.\n2. Terminar ejecución.")
          menu3 = input("Esperando opcion...\n")
          if menu3 == "1":
            thirdMenu = False
          elif menu3 == "2":
            thirdMenu = False
            secondMenu = False
            firstMenu = False
          else:
            print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
      elif menu2 == "4":
        secondMenu = False
      elif menu2 == "5":
        secondMenu = False
        firstMenu = False
      else:
        print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
  elif menu1 == "3":
    secondMenu = True
    while(secondMenu):
      print("Seleccione uno de los siguientes algoritmos de busquedainformada:\n1. Avara.\n2. A*.\n3. Regresar al menu principal.\n4. Terminar ejecucion.")
      menu2 = input("Esperando opcion...\n")
      if menu2 == "1":
        thirdMenu = True
        while(thirdMenu):
          print("Mostrando solución por busqueda Avara.\n1. Regresar al menu anterior.\n2. Terminar ejecución.")
          menu3 = input("Esperando opcion...\n")
          if menu3 == "1":
            thirdMenu = False
          elif menu3 == "2":
            thirdMenu = False
            secondMenu = False
            firstMenu = False
          else:
            print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
      elif menu2 == "2":
        thirdMenu = True
        while(thirdMenu):
          print("Mostrando solución por A*.\n1. Regresar al menu anterior.\n2. Terminar ejecución.")
          menu3 = input("Esperando opcion...\n")
          if menu3 == "1":
            thirdMenu = False
          elif menu3 == "2":
            thirdMenu = False
            secondMenu = False
            firstMenu = False
          else:
            print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
      elif menu2 == "3":
        secondMenu = False
      elif menu2 == "4":
        secondMenu = False
        firstMenu = False
      else:
        print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
  elif menu1 == "4":
    firstMenu = False
  else:
    print('No se ha reconocido la orden seleccionada, por favor intentelo de nuevo')
