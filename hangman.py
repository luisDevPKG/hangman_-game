import random
import os

# realizar la lectura del archivo con las palabras para el juego
def read_data(file_text="./archivos/data.txt"):
    words = []
    with open(file_text, "r", encoding="utf-8") as f:
        for each_word in f:
            # agrego cada palabra al arreglo llamado words,
            # elimino sus espacios al incio o final y
            # convierto toda la palabra en mayúscula
            words.append(each_word.strip().upper())
    return words
        # print(words)

def main():
    random_word = read_data(file_text="./archivos/data.txt")
    # se escoje una palabra aleatoria del archivo data.txt
    chosen_word = random.choice(random_word)
    # se recorre la palabra letra por letra con un list comprehensions
    each_letter = [letter for letter in chosen_word]
    # "oculto cada letra" de la palabra aleatoria
    each_letter_underscore = ["_"]*len(each_letter)
    
    # se crea un diccionario vacio
    letter_index_dict = {}
    # itero por cada indice y letra de la palabra aleatoria
    for index, letter in enumerate(chosen_word):
        # verifico si la letra está o no en el diccionario
        if not letter_index_dict.get(letter):
            # si No está, creo un nuevo item en el diccionario con la letra como keyword
            letter_index_dict[letter] = []
        # si SI está, accedo al item del diccionario
        letter_index_dict[letter].append(index)
    print(letter_index_dict)

    # creacion del ciclo para el juego
    while True:
        # limpio la pantalla del la terminal de comandos
        os.system("cls")
        print("""
        ¡ B I E N V E N I D O !

        Este es el juego del ahorcado ☠ ☠


        Instrucciones:
        1. Tienes que adivinar la palabra secreta
        2. Puedes intentarlo cuantas veces requieras!


        *** D I V I E R T E T E ***
        
        By. Luis Fernando Mosquera Imbachi
        """)

        # defino espacios entre las letras que conforman la palabra aletoria
        for element in each_letter_underscore:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        # realizar la comprobacion si es de tipo alfabetico (manejo de error)
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in each_letter:
            for index in letter_index_dict[letter]:
                each_letter_underscore[index] = letter
        
        if "_" not in each_letter_underscore:
            os.system("cls")
            print("F E L I C I D A D E S ¡Ganaste! La palabra era", chosen_word)
            break



if __name__ == '__main__':
    main()
    