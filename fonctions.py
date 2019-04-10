#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

from pickle import *
from donnees import *
from random import randrange as rdr

def player_name():
    good = False
    while good is False:
        try:
            name = input("Enter player name: ")
            assert len(name) <= 8
        except AssertionError:
            print("Player name can't be superior at 8 characteres.")
        else:
            good = True
    return name

def check_file(filename):
    exist = True
    try:
        fd_file = open(filename, "r")
    except FileNotFoundError:
        fd_file = open(filename, "w")
        exist = False
    finally:
        fd_file.close()
    return exist

def player_score(name, add=0):
    if check_file("scores") == False:
        score = {name: 0 + add}
    else:
        fd_file = open("scores", "rb")
        file_unpick = Unpickler(fd_file)
        score = file_unpick.load()
        fd_file.close()
        if name in score:
            score[name] += add
        else:
            score[name] = add
    fd_file = open("scores", "wb")
    file_pick = Pickler(fd_file)
    file_pick.dump(score)
    fd_file.close()
    return score[name]

def init_pendu():
    name = player_name()
    score = player_score(name)
    print("Welcome {}, your actual score is {}.".format(name, score))
    print("you have {} lifes.".format(life))
    return name

def get_letter():
    good = False
    while good is False:
        try:
            letter = input("choose a letter: ")
            assert len(letter) == 1 and letter.isalpha() is True
        except AssertionError:
            print("You have not enter a letter.")
        else:
            good = True
    return letter

def put_letter(word, seek_word, letter):
        i = 0
        tmp_word = list(seek_word)
        while i < len(word):
            if word[i] == letter:
                tmp_word[i] = letter
            i += 1
        return "".join(tmp_word)

def pendu():
    game = True
    global life
    word = liste[rdr(len(liste))]
    seek_word = "".join(["*" for x in word])
    while life > 0 and game is True:
        print("word: {}".format(seek_word))
        letter = get_letter().upper()
        if letter in word:
            seek_word = put_letter(word, seek_word, letter)
            if seek_word == word:
                game = False
        else:
            life -= 1
            print("life left: {}.".format(life))
    if life == 0:
        print("you loose ! The word was {}.".format(word))

def end_pendu(name):
    global life
    score = player_score(name, add=life)
    print("Your score is {} !".format(score))
    good = False
    while good is False:
        try:
            retry = input("do you want retry ? [y/n]: ").lower()
            assert retry == 'y' or retry == 'n'
        except AssertionError:
            print("please enter 'y' or 'n'")
        else:
            good = True
    if retry == 'y':
        life = 8
        return True
    else:
        return False
