# Poema en Python: "Quiero ser una banana"

def banana_deseos():
    colgada = True
    drama = False
    ganas = False

    print("Quiero ser una banana,")
    if colgada:
        print("dormir colgada en la rama,")
    if not drama:
        print("tomar el sol sin drama")
    if not ganas:
        print("y vivir sin tanta gana.")

def banana_estilo():
    color = "amarillo"
    estilo = "curvas de buen estilo"
    mirada = "cariño"
    exigencias = False

    print("\nQuiero vestir de", color + ",")
    print("con", estilo + ",")
    print("que me miren con", mirada)
    if not exigencias:
        print("y no me pidan un hilo.")

def banana_reinado():
    reina = True
    pelada_con_calma = True
    orgullo = True

    print("\nQuiero ser una banana,")
    if reina:
        print("¡la reina de la mañana!")
    if pelada_con_calma:
        print("Que me pelen sin apuro")
    if orgullo:
        print("y me rían con orgullo.")

def banana_destino():
    destino = "desayuno"
    alegria = True
    sabor = "siempre puro"

    print("\nY cuando llegue el destino,")
    print("ser parte del", destino + ",")
    if alegria:
        print("dar alegría en silencio")
    print("con un sabor", sabor + ".")

# Recitar el poema
def ser_banana():
    banana_deseos()
    banana_estilo()
    banana_reinado()
    banana_destino()

ser_banana()
