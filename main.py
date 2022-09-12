import string
import random
from paquetes import bd_palabras
from paquetes import diagramas

def juego_ahorcado(palabra):
    print("=========================")
    print("¡Bienvenido al juego del Ahorcado!")
    print("=========================")
    
    letrasPorAdivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letrasAdivinadas =set()
    
    intentos = 7
    
    while len(letrasPorAdivinar) > 0 and intentos > 0:
        print(f"Te quedan {intentos} intentos y has usado estas letras: {''.join(letrasAdivinadas)}")
        
        palabraLista = [letra if letra in letrasAdivinadas else '-' for letra in palabra]
        print(diagramas.vidas[intentos])
        print(f"Palabra: {' '.join(palabraLista)}")
        letraUsuario = input("Digite una letra para la palabra: ").upper()
        if letraUsuario in abecedario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)
            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print('')
            
            else:
                intentos -= 1
                print(f"\n Tu letra, {letraUsuario} no se encuentra en la palabra")
                
        elif letraUsuario in letrasAdivinadas:
            print("\n Ya escogiste esa letra. Por favor escoge una letra nueva")
        
        else:
            print("\n Esta letra no es válida")
    
    if intentos == 0:
        print(diagramas.vidas[intentos])
        print(f"Moriste. La palabra era {palabra}")
    else:
        print(f"Excelente, ¡GANASTE! Adivinaste la palabra {palabra}")

palabra = random.choice(bd_palabras.bdPalabras).upper()

juego_ahorcado(palabra)
        