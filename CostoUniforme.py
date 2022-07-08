import numpy as np


def reading(dir):
  file=open(dir,"r")
  string1 = file.read()
  lineas = string1.splitlines()


  laberinto= [10]*10

  for i in range(len(laberinto)):
        aux=lineas[i]
        laberinto[i]=aux.split(' ')


  laberinto = np.array(laberinto,int)

  file.close()
  return laberinto
  

 
maze=reading("Prueba1.txt")


class CuNode():
  #Se define el método constructor
  def __init__(self, status, parent, operator, depth, cost):
    self.status = status
    self.parent = parent
    self.operator = operator
    self.depth = depth
    self.cost = self.status[0]

  #Método que recibe un entero entre 0 y 3, y mueve el agente en una dirección, 0=izquierda, 1=arriba, 2=derecha, 3=abajo 
  #y retorna el nuevo estado en el que se encuentra el agente
  def move(self, direction):
    newStatus=self.status.copy()
    #Se realiza el cambio en la posición de acuerdo al operador que se usa:
    if direction == 0:#izquierda
      newStatus[2]=self.status[2]-1
    if direction == 1:#arriba
      newStatus[1]=self.status[1]-1
    if direction == 2:#derecha
      newStatus[2]=self.status[2]+1
    if direction == 3:#abajo
      newStatus[1]=self.status[1]+1
    #Luego se verifican los demás posibles cambios en el estado
    #Primero se mira si la casilla a la que cayo es una vacio o es el inicio
    if(maze[newStatus[1]][newStatus[2]]==0 or maze[newStatus[1]][newStatus[2]]==2):
      newStatus[0]=self.status[0]+1
    if(maze[newStatus[1]][newStatus[2]]==3):
      newStatus[0]=self.status[0]+1
      newStatus[3]=10
      newStatus[4]=3
    if(maze[newStatus[1]][newStatus[2]]==4):
      newStatus[0]=self.status[0]+1
      newStatus[3]=20
      newStatus[4]=4
    if(maze[newStatus[1]][newStatus[2]]==5):
      newStatus[0] = self.status[0]+1
      #Se verifica los casos en los que llega a un item
    if (newStatus[5]==True and newStatus[6]==False): #Se mira si ya se tomó un objeto, entonces se va a tomar un segundo
      if not (newStatus[1]==newStatus[7] and newStatus[2]==newStatus[8]): #Si no está tratando de coger el objeto que ya había cogido
        if maze[newStatus[1]][newStatus[2]]==5:
          #Se dice que se tomó un primer objeto y se guarda sus coordenadas para evitar ciclos
          newStatus[6]=True

    if not (newStatus[5] and newStatus[6]): #Se mira si es el primer objeto que coge
      #Se dice que se tomó un primer objeto y se guarda sus coordenadas para evitar ciclos
      newStatus[5]=True
      newStatus[7]=newStatus[1]
      newStatus[8]=newStatus[2]    
    if(maze[newStatus[1]][newStatus[2]]==6):
      if(newStatus[3]>0):
        newStatus[0]=self.status[0]+1
      else:
        newStatus[0]=self.status[0]+4

    if newStatus[3]>0:
      newStatus[3]= newStatus[3] -1
    elif newStatus[4] != 0:
      newStatus[4] = 0

      
    
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

  def getCost(self):
    return self.cost

  #Método que retorna si se llegó a la meta o no
  def solution(self):
    if (self.status[5] == True and self.status[6] == True):
      return True
    else:
      return False

#Para la búsqueda preferente por profundidad, un estado será una lista de la siguiente manera:
#[costo,posición en x, posición en y,combustible(en caso de haber tomado una nave),numero de nave,tomoobjeto1,tomoonjeto2,posición en x obj1, posición en y obj1]
#se debe determinar cuál es el estado inicial para construir el nodo raíz:
def initStatus(maze):
  status=[0,0,0,0,0,False,False,-1,-1]
  for i in range(len(maze)):
    for j in range(len(maze)):
      if(maze[i][j]==2):
        status=[0,i,j,0,0,False,False,-1,-1]
  return status

#Método que recibe un estado y con base en este determina en qué direcciones se podría mover el agente
def radar(status):
  allowedMoves=[False, False, False, False]
  if not status[2]==0:#no se encuentra en la primera columna, se examina el movimiento hacia la izquierda
    if maze[status[1]][status[2]-1]!=1:#Si no es un muro
      allowedMoves[0]=True #Se puede mover hacia la izquierda
  if not status[1]==0:#no se encuentra en la fila de arriba, se examina ese movimiento
    if maze[status[1]-1][status[2]]!=1:#Si no es un muro
      allowedMoves[1]=True#Se puede mover hacia arriba
  if not status[2]==9:#No se encuentra en la última columna, se examina el movimiento hacia la derecha
    if maze[status[1]][status[2]+1]!=1:#Si no es un muro
      allowedMoves[2]=True#Se puede mover hacia la derecha
  if not status[1]==9:#no se encuentra en la fila de abajo, se examina ese movimiento
    if maze[status[1]+1][status[2]]!=1:#Si no es un muro
      allowedMoves[3]=True#Se puede mover hacia abajo
  return allowedMoves



#Método que recibe un estado y un nodo, para compararlos y determinar si el agente ya se ha encontrado en ese estado antes, es decir, hay un ciclo
def repeticionAnterior(status, node):
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
    if not repeticionAnterior(node.move(0), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[0]=CuNode(node.move(0), node, 0, node.getDepth()+1,node.getCost())

  if allowedMoves[1]: #Miramos si se puede mover hacia arriba
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not repeticionAnterior(node.move(1), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[1]=CuNode(node.move(1), node, 1, node.getDepth()+1,node.getCost())

  if allowedMoves[2]: #Miramos si se puede mover a la derecha
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not repeticionAnterior(node.move(2), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[2]=CuNode(node.move(2), node, 2, node.getDepth()+1,node.getCost())

  if allowedMoves[3]: #Miramos si se puede mover abajo
    #De ser posible, miramos si el estado resultante no sería un ciclo
    if not repeticionAnterior(node.move(3), node):
      #En caso de no existir ciclo, creamos un nuevo nodo y lo guardamos en children
      children[3]=CuNode(node.move(3), node, 3, node.getDepth()+1,node.getCost())

  return children


def costo(a):
    return a[0]


def prueba():
  nodo = CuNode(initStatus(maze),None,None,0,0)
  frontier = []
  frontier.append((nodo.getCost(),nodo))
  explored = []
  expandedNode = 0
  go = True
  while go:
    if len(frontier) == 0:
      return ("La búsqueda falló :(")
    frontier.sort(key=costo)
    nodo=frontier[0][1]
    print(nodo.getStatus())
    expandedNode+=1
    frontier.pop(0)
    if nodo.solution():
      return ("La búsqueda fue exitosa :)\nSe expandieron "+str(expandedNode)+ " nodos.\nLa profundidad del arbol es "+str(nodo.getDepth())+"\nel costo fue de "+str(nodo.getCost()))
    explored.append(nodo)
    createdNodes = expandNode(nodo)
    if not createdNodes[3] is None:
        if createdNodes[3] not in explored:
          if createdNodes[3] not in frontier:
           frontier.append((createdNodes[3].getCost(),createdNodes[3]))
    if not createdNodes[2] is None:
       if createdNodes[2] not in explored:
          if createdNodes[2] not in frontier:
           frontier.append((createdNodes[2].getCost(),createdNodes[2]))
    if not createdNodes[1] is None:
       if createdNodes[1] not in explored:
          if createdNodes[1] not in frontier:
           frontier.append((createdNodes[1].getCost(),createdNodes[1]))
    if not createdNodes[0] is None:
       if createdNodes[0] not in explored:
          if createdNodes[0] not in frontier:
           frontier.append((createdNodes[0].getCost(),createdNodes[0]))
    


      

      
print(prueba())
          
    















