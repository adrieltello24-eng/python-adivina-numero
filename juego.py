import random

def jugar():
    # La coomputadora elige un número secreto entre 1 y 50
    numero_secreto = random.randint(1,50)
    intentos_maximos = 5
    intentos_realizados = 0

    print("===============================================")
    print("¡Bienvenido al juego de Adivina el Número!")
    print("He pensado un número entre 1 y 50.")
    print(f"Tienes un máximo de {intentos_maximos} intentos para adivinarlo.")
    print("===============================================")

    #Bucle principal del juego
    while intentos_realizados < intentos_maximos:
        #Calculamos cuántos intentos le quedan al usuario
        intentos_restantes = intentos_maximos - intentos_realizados
        print(f"\nTe quedan {intentos_restantes} intentos.")

        # try/except evita que el programa se cierre  si el usuario escribe una letra por error
        try:
            intento = int(input("Introduce tu número: "))
        except ValueError:
            print("✖️ Por favor, introduce un número válido (entero).")
            continue

        intentos_realizados += 1

        # Condicionales para evaluar el número ingresado
        if intento < numero_secreto:
            print("📈 El número secreto es MÁS ALTO.")
        elif intento > numero_secreto:
            print("📉 El número secreto es MÁS BAJO.")
        else:
            print(f"\n🎊 ¡Excelente! Adivinaste el número en {intentos_realizados} intentos.")
            return # Termmina la función porque ya ganó

    # Si se agotan los intentos y no acertó, se ejecuta esto:
    print(f"\n😢 Se agotaron tus intentos. El número secreto era el {numero_secreto}.")

# Ejecuta el juego
if __name__ == "__main__":
    jugar()


