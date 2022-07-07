import numpy as np
from turtle import *

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

def drawBasicSolution(solution):
  x0=-1
  y0=-1
  #Se determina cual es la posición inicial del agente
  for i in range(len(maze)):
    for j in range(len(maze)):
      if(maze[i][j]==2):
        print("X:" + str(i)+" Y:"+ str(j))
        x0=i
        y0=j
  screen_x=-250+(y0*50)
  screen_y=250-(x0*50)
  speed(6)
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
      #Ahi mismo borramos el avance
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
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
      else:
        fillcolor("white")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
      #Pintamos el avance del agente
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
      #Nos delplazamos en la matriz
      y0=y0-1
    elif i==1:
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
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
      else:
        fillcolor("white")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
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
      x0=x0-1
    elif i==2:
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
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
      else:
        fillcolor("white")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
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
      y0=y0+1
    elif i==3:
      pencolor("black")
      if maze[x0][y0]==0:
        fillcolor("white")
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
      else:
        fillcolor("white")
      begin_fill()
      goto(screen_x, screen_y-50)
      goto(screen_x, screen_y)
      goto(screen_x+50, screen_y)
      goto(screen_x+50, screen_y-50)
      goto(screen_x, screen_y-50)
      end_fill()
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
      x0=x0+1
  pencolor("black")
  fillcolor("blue")
  begin_fill()
  goto(screen_x, screen_y-50)
  goto(screen_x, screen_y)
  goto(screen_x+50, screen_y)
  goto(screen_x+50, screen_y-50)
  goto(screen_x, screen_y-50)
  end_fill()
  
