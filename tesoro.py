print("bienvenidos ala isla tu mision sera encontra el tesoro")

print("¿derecha, izquierda o atajo?")


direccion = input().strip().lower()

if direccion == "derecha":
    print("caiste en un agujero Game Over")
    print("fin")
    quit()
elif direccion == "atajo":
    print("pasas al siguiente nivel")
    
elif direccion == "izquierda":
    print("estas avanzando")
else:
    print("elige una de las direciones propuestas para que funcione ")
    print("fin")
    quit()
    
print("---------------------------------------------------------------")
print(" elige una opcion:")
print("nadar")
print("esperar")
print("probar suerte")

opcion = input().strip().lower()

if opcion == "probar suerte":
    print("ganaste")
    print("fin")
    quit()
elif opcion == "nadar":
    print("Atacado por una tribu Game Over")
    print("fin")
    quit()
elif opcion == "esperar":
    print("¿cual puerta? elige una: ")
    print("rojo")
    print("azul")
    print("amarillo")
    print("cualquier otra opcion")
else:
    print("elige una de las puestas o la otra opcion")
    print("fin")
    quit()
    
    
color_otra = input().strip().lower()

if color_otra =="rojo":
    print("eres quemado Game Over")
    print("fin")
    print("quit")
elif color_otra == "azul":
    print("Devorado por bestias Game Over")
    print("fin")
    quit()
elif color_otra == "amarillo":
    print("haz ganado")
    print("fin")
    quit()
elif color_otra == "cualquier otra opcion": 
    print("cualquier otra opcion")
    print("Game Over")
    print("fin")
    print("reiniciar consola")
    quit()
else:
    print("elige una de las puertas propuestas")
    print("reiniciar consola")
    quit()
    
