print("Rutina diaria")
print("-------------------------------------------------------------------")
print("¿bañarme (si) o (no)?")

bañarme = input("-").strip().lower()

if bañarme == "si":
    print("excelente")
elif bañarme == "no":
    print("seria antihigienico")
    print("fin") 
    quit() 
else: 
    print("elige si te vas a bañar (si) o (no)") 
    print("reiniciar consola") 
    quit()
print("-------------------------------------------------------------------")   
print("sepillarme (si) o (no)?")

sepillarme = input("-").strip().lower()

if sepillarme == "si":
    print("excelente")
elif sepillarme == "no":
    print("quedaria con los dientes sucios ademas de causarles enfermedades por falta de higiene")
    print("fin") 
    quit() 
else: 
    print("elige si te vas a sepilar (si) o (no)") 
    print("reiniciar consola")
    quit() 
    
print("-------------------------------------------------------------------")   
print("desayunar (si) o (no)?")

desayunar = input("-").strip().lower()

if desayunar == "si":
    print("excelente")
elif desayunar == "no":
    print("no pasa nada")
    print("fin")
    quit()
else: 
    print("elige  vas a desayunar (si) o (no)") 
    print("reiniciar consola")
    quit() 
    
print("-------------------------------------------------------------------") 
print("organizar y decidir que hago con mi vida")

print("-------------------------------------------------------------------") 
print("elije un numero:")
print("1-seguir buscando trabajo")
print("2-estudiar autodidacta")
print("3-hacer un curso")

seguir = input("-").strip().lower()

if seguir == "1":
    print(" todavia no he encontrado")
    print("fin")
    quit()
    
elif seguir == "2":
    print("masomenos me ha ido bien")
    print("fin")
    quit()
    
elif seguir == "3":
    print("elegi hacer el curso y me ha ido muy bien")
    print("fin")
    quit()
else: 
    print("elegir las opciones recomendadas")
    print("reiniciar consola")
    quit()




