from operator import itemgetter
import numpy as np
import time
from GUI import reading

 ##############################################################################
 # IMPLEMENTACIÓN DE ALGORITMO DE BÚSQUEDA ÁVARA, POR EQUIPO DE DESARROLLO:   #                        
 ##############################################################################

 #Se carga el laberinto a la variable maze que se usa en todo lado
maze=reading("Prueba1.txt")

 #Se define la clase Greedy node, usada para implementar el algoritmo de búsqueda informada Ávara
class GreedyNode:
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

#Para la búsqueda Ávara un estado tiene la siguiente representación:
#[posición en X, posición en Y, cogió item1?, cogió item2?, coordenada X del item1, coordenada y del item1]
#se debe determinar cuál es el estado inicial para construir el nodo raíz:
def initStatus(maze):
  status=[0,0,False,False,-1,-1]
  for i in range(len(maze)):
    for j in range(len(maze)):
      if(maze[i][j]==2):
        status=[i,j,False,False, -1, -1]
  return status

def prepareHeuristic():
    count=0
    objects=[[-1,-1],[-1,-1]]
    for i in range(len(maze)):
        for j in range(len(maze)):
            if(maze[i][j]==5):
                if(count==0):
                    objects[0][0]=i
                    objects[0][1]=j
                    count+=1
                elif(count==1):
                    objects[1][0]=i
                    objects[1][1]=j
                    count+=1
                else:
                    return("Fatal error")
    return objects

def manhattan(x0,y0,x1,y1):
    distance=abs(x1-x0)+abs(y1-y0)
    return distance
#Definición de la función heurística que se explica en el informe anexo:
def h(n):
    objects = prepareHeuristic()
    i1=1
    i2=1
    #Item #1
    if(n.getStatus()[2]):
        i1=0
    #Item #2
    if(n.getStatus()[3]):
        i2=0
    estimatedCost = (manhattan(n.getStatus()[0], n.getStatus()[1], objects[0][0], objects[0][1])*i1) 
    + (manhattan(n.getStatus()[0], n.getStatus()[1], objects[1][0], objects[1][1])*i2)
    return estimatedCost

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

#Método que recibe un nodo y retorna una lista con los nodos que se generan al moverse en todas las direcciones
def expandNode(node):
  allowedMoves=radar(node.getStatus()) #Determinamos en qué direcciones debería poderse mover el agente
  children = [None, None, None, None]

  if allowedMoves[0]: #Miramos si se puede mover a la izquierda
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(0), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[0]=GreedyNode(node.move(0), node, 0, node.getDepth()+1)

  if allowedMoves[1]: #Miramos si se puede mover hacia arriba
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(1), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[1]=GreedyNode(node.move(1), node, 1, node.getDepth()+1)

  if allowedMoves[2]: #Miramos si se puede mover a la derecha
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(2), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[2]=GreedyNode(node.move(2), node, 2, node.getDepth()+1)

  if allowedMoves[3]: #Miramos si se puede mover abajo
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not thereIsCycle(node.move(3), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[3]=GreedyNode(node.move(3), node, 3, node.getDepth()+1)

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

#Función clave de ordenamiento por heurística
def heuristic(a):
    return a[1]

def greedySolve():
    #Contador de nodos expandidos
    startTime = time.time()
    expandedNodes = 0
    #Se crea la cola de prioridad
    greedyQueue = []
    #Se le añade el nodo raíz
    greedyQueue.append([GreedyNode(initStatus(maze), None, None, 0), h(GreedyNode(initStatus(maze), None, None, 0))])
    go = True
    #Se inicia un bucle que solo termina al encontrar solución o decir que no existe una
    while go:
        #Si no quedaron nodos a expandir y ninguno fue meta, se dice que no existe solución
        if len(greedyQueue)<=0:
            return None
        #Se guarda el nodo a revisar en n
        greedyQueue.sort(key=heuristic)
        n=greedyQueue[0][0]
        expandedNodes+=1
        greedyQueue.pop(0)
        
        if n.solution(): #Se determina si el nodo raíz es meta
            finishTime = str(time.time()-startTime)
            solution = [getPath(n), expandedNodes, n.getDepth(), finishTime]
            # #De ser así, se dice que existe solución
            return solution
        else:
            #Si no es meta, entonces se expande
            createdNodes = expandNode(n)
            if not createdNodes[3] is None:
                greedyQueue.append([createdNodes[3],h(createdNodes[3])])
            if not createdNodes[2] is None:
                greedyQueue.append([createdNodes[2],h(createdNodes[2])])
            if not createdNodes[1] is None:
                greedyQueue.append([createdNodes[1],h(createdNodes[1])])
            if not createdNodes[0] is None:
                greedyQueue.append([createdNodes[0],h(createdNodes[0])])
