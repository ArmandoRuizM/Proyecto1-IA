from typing_extensions import Self
import numpy as np
import turtle

wn= turtle.Screen()
wn.bgcolor("black")
wn.title("ProyectoIA")
wn.setup(700,700)

#Crear pen
class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color()
    self.penup()
    self.speed(0)
    
#Diccionario de Colores
Colores={
  "0": "white",
  "1": "brown",
  "2": "blue",
  "3": "green",
  "4": "purple",
  "5": "yellow",
  "6": "red"
}

#Crear instancia de pen
pen = Pen()

def confLaberinto(Laberinto):
    for y in range(len(Laberinto)):
      for x in range(len(Laberinto[y])):
        cuadro = Laberinto[y][x]
        screen_x = -288 + (x * 24)
        screen_y =  288 - (y * 24)
        if cuadro == 0:
          pen.goto(screen_x,screen_y)
          pen.color(Colores["0"])
          pen.stamp()
        elif cuadro == 1:
          pen.goto(screen_x,screen_y)
          pen.color(Colores["1"])
          pen.stamp()
        elif cuadro == 2:
          pen.goto(screen_x,screen_y)
          pen.color(Colores["2"])
          pen.stamp()
        elif cuadro == 3:
          pen.goto(screen_x,screen_y)
          pen.color(Colores["3"])
          pen.stamp()
        elif cuadro == 4:
          pen.goto(screen_x,screen_y)
          pen.color(Colores["4"])
          pen.stamp()
        elif cuadro == 5:
          pen.goto(screen_x,screen_y)
          pen.color(Colores["5"])
          pen.stamp()
        elif cuadro == 6:
          pen.goto(screen_x,screen_y)
          pen.color(Colores["6"])
          pen.stamp()
        







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
confLaberinto(maze)
  
 
while True:
  pass
