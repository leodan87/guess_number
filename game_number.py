import random

def juego_adivinar():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("He pensado en un número entre 1 y 100.")

    while True:
        intento = input("Adivina el número: ")
        
        try:
            intento = int(intento)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("Más alto.")
        elif intento > numero_secreto:
            print("Más bajo.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    juego_adivinar()