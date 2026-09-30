import random
import time

def lanzar_dados():
    print("==============================================")
    print("🎲 ¡Bienvenido al Simulador de  Dados! 🎲")
    print("==============================================")

    while True:
        # Pide presionar Enter para jugar, o escribir 'salir'
        entrada = input("\nPresiona [ENTER] para lanzar lod dados o escribe 'salir' para terminar: ").strip().lower()

        if entrada == 'salir':
            print("\n👋 ¡Gracias por jugar! Sigue practicando tu código.")
            break

        print("\n🎲 Agitnando los dados...")
        time.sleep(0.8) # Pausa de suspenso (casi 1 segundo)

        #Genera dos números aleatorios entre 1 y 6 
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma_total = dado1 + dado2

        # Muestra los resultados en pantalla
        print(f"🔷 Dado 1: {dado1}")
        print(f"🔷 Dado 2: {dado2}")
        print(f"📊 Suma total: {suma_total}")
        
        # Mensaje especial si saca dobles (un clásico de la robótica y juegos)
        if dado1 == dado2:
            print("🎉 ¡Vaya suerte! ¡Sacaste dobles!")
        print("-" * 30)

if __name__ == "__main__":
    lanzar_dados()
