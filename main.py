from ast import operator
from DFS import dfsSolve
from GUI import maze, confLaberinto, GUI, drawBasicSolution
from BFS import bfsSolve

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
          solution = bfsSolve()
          if solution is not None:
            print("La búsqueda fue exitosa :)\nSe expandieron "+str(solution[1])+ " nodos.\nLa profundidad del arbol es "+str(solution[2])+"\nLa búsqueda terminó en "+solution[3]+"s")
            confLaberinto(maze)
            drawBasicSolution(solution)
          else:
            print("No se pudo encontrar una solución :(")
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
            confLaberinto(maze)
            drawBasicSolution(solution)
          else:
            print("No se pudo encontrar una solución :(")
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
