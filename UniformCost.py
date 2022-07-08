from operator import itemgetter
import numpy as np
import time
#from GUI import reading

 ###########################################################################################
 # IMPLEMENTACIÓN DE ALGORITMO DE BÚSQUEDA POR COSTO UNIFORME, POR EQUIPO DE DESARROLLO:   #                        
 ###########################################################################################

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

 #Se define la clase Uniform Cost node, usada para implementar el algoritmo de búsqueda por costo uniforme
class UCNode:
  #Se define el método constructor
  def __init__(self, status, parent, operator, depth, cost):
    self.status = status
    self.parent = parent
    self.operator = operator
    self.depth = depth
    self.cost = cost

  #Método bobo
  def ImNode(self):
    return "Hola, soy un nodo"

  #Método que recibe un entero entre 0 y 3, y mueve el agente en una dirección, 0=izquierda, 1=arriba, 2=derecha, 3=abajo y retorna el nuevo estado en el que se encuentra el agente
  def move(self, direction):
    statusAndCost = [None,None]
    newCost=-1
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

    ##Se verifica todo el tema de las naves:
    ##Si va a coger la nave1
    if(maze[newStatus[0]][newStatus[1]]==3):
        #Si no ha cogido la nave1 ya
        if(not (self.status[6])):
            #Si no ha cogido la nave2
            if(not (self.status[10])):
                newStatus[6]=True
            else:
                #Miramos si se quedó sin gasolina
                if(self.status[13]<=0):
                    newStatus[6]=True
    
    ##Si va a coger la nave2
    if(maze[newStatus[0]][newStatus[1]]==4):
        #Si no ha cogido la nave2 ya
        if(not (self.status[10])):
            #Si no ha cogido la nave1
            if(not (self.status[6])):
                newStatus[10]=True
            else:
                #Miramos si se quedó sin gasolina
                if(self.status[9]<=0):
                    newStatus[10]=True

    #Se gasta la gasolina de la nave que tenga
    #Si tiene nave 1
    if(self.status[6]):
        #Si tiene gasolina
        if(self.status[9]>0):
            #Se reduce en uno la gasolina
            newStatus[9]=self.status[9]-1

    #Si tiene nave 2
    if(self.status[10]):
        #Si tiene gasolina
        if(self.status[13]>0):
            #Se reduce en uno la gasolina
            newStatus[13]=self.status[13]-1


    ##Se calcula el costo con respecto a qué casilla se hace el siguiente movimiento:
    if(maze[newStatus[0]][newStatus[1]]!=6):
        ##Siempre que no caiga en un aceite, el costo aumenta en 1
        newCost=self.cost+1
    else:
        ##Si cae en una casilla con aceite
        ##Caso en el que tiene las dos naves
        if(newStatus[6] and newStatus[10]):
            if(newStatus[9]>0):
                newCost=self.cost+1
            else:
                if(newStatus[13]>0):
                    newCost=self.cost+1
                else:
                    newCost=self.cost+4
        else:
            ##Caso en el que tiene nave1
            if(newStatus[6]):
                if(newStatus[9]>0):
                    newCost=self.cost+1
                else:
                    newCost=self.cost+4
            else:
                ##Caso en el que tiene nave2
                if(newStatus[10]):
                    if(newStatus[13]>0):
                        newCost=self.cost+1
                    else:
                        newCost=self.cost+4
                else:
                    newCost=self.cost+4
        
        
        

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
    
    statusAndCost[0]=newStatus
    statusAndCost[1]=newCost
    return statusAndCost

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

    #Getter del costo del nodo
  def getCost(self):
    return self.cost

  #Método que retorna si se llegó a la meta o no
  def solution(self):
    if (self.status[2] and self.status[3]):
      return True
    else:
      return False

#Para la búsqueda Ávara un estado tiene la siguiente representación:
#[posición en X, posición en Y, cogió item1?, cogió item2?, coordenada X del item1, coordenada y del item1,
#cogió nave1?, coordenada X nave1, coordenada Y nave1, gasolina nave1, cogió nave2?, coordenada X nave2, 
#coordenada Y nave2, gasolina nave2]
#se debe determinar cuál es el estado inicial para construir el nodo raíz:
def initStatus(maze):
  status=[0,0,False,False,-1,-1, False, -1, -1, -1, False, -1, -1, -1]
  for i in range(len(maze)):
    for j in range(len(maze)):
      if(maze[i][j]==2):
        aux=prepareStarShips()
        status=[i,j,False,False, -1, -1, False, aux[0][0], aux[0][1], 10, False, aux[1][0], aux[1][1], 20]
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

def prepareStarShips():
    ships=[[-1,-1],[-1,-1]]
    for i in range(len(maze)):
        for j in range(len(maze)):
            if(maze[i][j]==3):
                ships[0][0]=i
                ships[0][1]=j
    
    for i in range(len(maze)):
        for j in range(len(maze)):
            if(maze[i][j]==4):
                ships[1][0]=i
                ships[1][1]=j
    
    return ships

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
    aux0=node.move(0)
    if not thereIsCycle(aux0[0], node):
        #Creamos un nuevo nodo y lo guardamos en children
        children[0]=UCNode(aux0[0], node, 0, node.getDepth()+1, aux0[1])

  if allowedMoves[1]: #Miramos si se puede mover hacia arriba
    aux1=node.move(1)
    if not thereIsCycle(aux1[0], node):
        #Creamos un nuevo nodo y lo guardamos en children
        children[1]=UCNode(aux1[0], node, 1, node.getDepth()+1, aux1[1])

  if allowedMoves[2]: #Miramos si se puede mover a la derecha
    aux2=node.move(2)
    if not thereIsCycle(aux2[0], node):
        #Creamos un nuevo nodo y lo guardamos en children
        children[2]=UCNode(aux2[0], node, 2, node.getDepth()+1, aux2[1])

  if allowedMoves[3]: #Miramos si se puede mover abajo
    aux3=node.move(3)
    if not thereIsCycle(aux3[0], node):
        #Creamos un nuevo nodo y lo guardamos en children 
        children[3]=UCNode(aux3[0], node, 3, node.getDepth()+1, aux3[1])

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


def isIn(node, list):
    inside = False
    for i in range(len(list)):
        if(node.getStatus()==list[i][0].getStatus()):
            inside = True
    return inside
    
#Función clave de ordenamiento por costo
def cost(a):
    return a[1]

def uniformSolve():
    #Contador de nodos expandidos
    startTime = time.time()
    expandedNodes = 0
    #Se crea la cola de prioridad
    uniformQueue = []
    #Se le añade el nodo raíz
    uniformQueue.append([UCNode(initStatus(maze), None, None, 0, 0), 0])
    #print(uniformQueue[0][0].getCost())
    go = True
    #Se inicia un bucle que solo termina al encontrar solución o decir que no existe una
    while go:
        #Si no quedaron nodos a expandir y ninguno fue meta, se dice que no existe solución
        if len(uniformQueue)<=0:
            return None
        #Se guarda el nodo a revisar en n
        uniformQueue.sort(key=cost)
        n=uniformQueue[0][0]
        #print(n.getStatus())
        #print(n.getCost())
        expandedNodes+=1
        uniformQueue.pop(0)
        
        if n.solution(): #Se determina si el nodo raíz es meta
            print(n.getCost())
            finishTime = str(time.time()-startTime)
            solution = [getPath(n), expandedNodes, n.getDepth(), finishTime]
            # #De ser así, se dice que existe solución
            return solution
        else:
            #Si no es meta, entonces se expande
            createdNodes = expandNode(n)
            if not createdNodes[3] is None:
                if not (isIn(createdNodes[3], uniformQueue)):
                    uniformQueue.append([createdNodes[3],createdNodes[3].getCost()])
            if not createdNodes[2] is None:
                if not (isIn(createdNodes[2], uniformQueue)):
                    uniformQueue.append([createdNodes[2],createdNodes[2].getCost()])
            if not createdNodes[1] is None:
                if not (isIn(createdNodes[1], uniformQueue)):
                    uniformQueue.append([createdNodes[1],createdNodes[1].getCost()])
            if not createdNodes[0] is None:
                if not (isIn(createdNodes[0], uniformQueue)):
                    uniformQueue.append([createdNodes[0],createdNodes[0].getCost()])

print(uniformSolve())
