print("Huevo frito")
print("-----------------------------------------")
print("¿Necesitas un huevo para empezar ¿tienes? (si) o (no)?")

tengo = input("-").strip().lower()

if tengo == "si":
    print("muy bien")
elif tengo == "no":
    print("necesitas un huevo para continuar")
    print("ve y compra un huevo")
    print("reiniciar consola para continuar")
    print("fin")
    quit()  
else:
    print("¿ para comprar el huevo eleige (si) o (no)?")
    print("reiniciar consola")
    quit()
print("-----------------------------------------")

print("¿rompe el huevo para verterlo en el sarten con aceite ya lo hiciste (si) o (no)?")

rompo = input("-").strip().lower()

if rompo == "si":
    print("vamos bien ")
elif rompo == "no":
    print("como lo vas a fritar si no lo rompes")
    print("fin")
    quit()
else:
    print("elige (si) o (no) para verterlo en el sarten")
    print("reiniciar consola")
    quit()
    
print("----------------------------------------------")

print("¿ pon sarten con el huevo con la estufa prendida ya lo hiciste: (si) o (no)?")

pongo = input("-").strip().lower()

if pongo == "si":
    print("muy bien")
elif pongo == "no":
    print("entonces no se fritaria")
    print("fin")
    quit()
else:
    print("elige (si) o (no) para fritarlo")
    print("reiniciar consola")
    quit()
    
print("-------------------------------------------")
print("mira qeu este en el punto retiralo y apaga la estufa")
print("¿ya lo hiciste ? (si) o (no)")

saco = input("-").strip().lower()

if saco == "si":
    print("ya terminarias de fritar el huevo echale sal")
elif saco == "no":
    print("se te quemaria el huevo y podria hacerse un incendio si no apagas la estufa") 
    print("fin")
    quit()
else:
    print("elige (si) o (no) para terminar de fritar el huevo")   
    print("reiniciar consola")
    quit()