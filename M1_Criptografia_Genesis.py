
# Mi programa de criptografía - Módulo 1

print("¡Bienvenido al programa de criptografía!")

# Esta funcion cifra un mensaje usando el metodo Cesar.
# Cada letra se desplaza una cantidad de posiciones en el alfabeto.
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            base = ord('A') if caracter.isupper() else ord('a')
            posicion = ord(caracter) - base
            nueva_posicion = (posicion + desplazamiento) % 26
            nueva_letra = chr(nueva_posicion + base)
            resultado += nueva_letra

        else:
            resultado += caracter

    return resultado
# Esta funcion descifra un mensaje cifrado con el metodo Cesar.
# Utiliza un desplazamiento negativo para recuperar el mensaje original.
def descifrado_cesar(texto_cifrado, desplazamiento):
    return cifrado_cesar(texto_cifrado, -desplazamiento)

# Esta funcion cifra un mensaje usando el metodo Vigenere.
# Utiliza una palabra clave para determinar el desplazamiento de cada letra.
def cifrado_vigenere(texto, clave):
    resultado = ""
    clave = clave.upper()

    if clave == "":
        return "Error: la clave no puede estar vacía."

    indice_clave = 0
    
    for caracter in texto:
        if caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            base = ord('A') if caracter.isupper() else ord('a')
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord('A')
            posicion = ord(caracter) - base
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado += chr(nueva_posicion + base)
            indice_clave += 1
        else:
            resultado += caracter

    return resultado

# Esta funcion descifra un mensaje cifrado con el metodo Vigenere.
# Resta el desplazamiento indicado por cada letra de la palabra clave.
def descifrado_vigenere(texto, clave):
    resultado = ""
    clave = clave.upper()

    if clave == "":
        return "Error: la clave no puede estar vacía."

    indice_clave = 0
    
    for caracter in texto:
        if caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            base = ord('A') if caracter.isupper() else ord('a')
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord('A')
            posicion = ord(caracter) - base
            nueva_posicion = (posicion - desplazamiento) % 26
            resultado += chr(nueva_posicion + base)
            indice_clave += 1
            
        else:
            resultado += caracter

    return resultado

# Este ciclo mantiene el menu activo hasta que el usuario elija salir.
while True:
    print("1. Cifrar y descifrar con Cesar")
    print("2. Cifrar y descifrar con Vigenere")
    print("3. Salir")

    # Guarda la opcion que selecciona el usuario.
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        mensaje = input("Escribe el mensaje que deseas cifrar: ")
        desplazamiento = int(input("Escribe el desplazamiento: "))

        cifrado = cifrado_cesar(mensaje, desplazamiento)
        descifrado = descifrado_cesar(cifrado, desplazamiento)

        print("Mensaje original:", mensaje)
        print("Mensaje cifrado:", cifrado)
        print("Mensaje descifrado:", descifrado)

    elif opcion == "2":
        mensaje = input("Escribe el mensaje que deseas cifrar: ")
        clave = input("Escribe la palabra clave: ")

        if not clave.isalpha() or not clave.isascii():
             print("Error: la clave debe contener solamente letras de la A a la Z.")
        else:
            cifrado = cifrado_vigenere(mensaje, clave)
            descifrado = descifrado_vigenere(cifrado, clave)

            print("Mensaje original:", mensaje)
            print("Mensaje cifrado:", cifrado)
            print("Mensaje descifrado:", descifrado)

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Intenta de nuevo.")

# Ejemplo de uso - Cifrado Cesar
# Mensaje original: Hola
# Desplazamiento: 3
# Mensaje cifrado: Krod
# Mensaje descifrado: Hola

# Ejemplo de uso - Cifrado Vigenere
# Mensaje original: Hola
# Clave: Sol
# Mensaje cifrado: Zcws
# Mensaje descifrado: Hola
