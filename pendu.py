#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

from fonctions import *

def main():
    game = True
    name = init_pendu()
    while game is True:
        pendu()
        game = end_pendu(name)

if __name__ == "__main__":
    main()
