
import random
import os

def Ahorcado():
        data = SeleccionarData()
        chosen_word = random.choice(data)
        word_list = [letter for letter in chosen_word ]
        word_underscore = len(word_list)*"_"
        print("Bienvenidos al Juego del Ahorcado \n Adivina la siguiente palabra")
        print(word_underscore)

def SeleccionarData ():
    words = [ ]
    with open ("/Users/steffyperilla/Documents/Platzi/Ahorcado/archivos/data.txt","r", encoding="utf-8") as f: 
        for line in f:
            words.append(line.strip().upper())
    return words 

def GuessWords ():
    letter = input("Ingresa una letra: ").strip().upper()
    assert letter.isalpha(), "Solo puedes ingresar letras"
    return letter 

if __name__ == '__main__':
    Ahorcado()