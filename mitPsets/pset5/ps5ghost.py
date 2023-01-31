# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
# problem set 5

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    #print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where thestringArrs are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def getNames():
    """
    -takes no inputs and generates an array of all players names
    Returns:
        list: a list of all players names
    """
    numPlayers = int(input("how many players want to play?: "))
    while type(numPlayers) != int or numPlayers <= 0:
        print("that is not a valid number, enter a number greater than or equal to one")
        numPlayers = int(input("how many players want to play?: "))
    
    nameArr = []
    for i in range(1,numPlayers + 1):
        name = input(f"player{i} what is your name?: ")
        nameArr.append(name)
    return nameArr

def isWordExactMatch(word):
    stringArr = load_words()
    if(word in stringArr and len(word) > 3): 
        return True
    return False

def isWordValid(target):
    stringArr = load_words()
    if(len(target) <= 3): return True
    for i in range(len(stringArr)-1):
        x = 0
        for j in range(len(target) + 1):
            if(x == len(target)): return True
            elif(len(target) > len(stringArr[i])): break
            elif(target[j] == stringArr[i][x]): x += 1
            else: break
    return False

def isValidChar(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char.lower()
    if(char == ""): return False
    elif(len(char) > 1 or type(char) != str): return False
    for i in alphabet:
        if(char == i):
            return True
    return False

def playGhost():
    nameList = getNames()
    string = ""
    hasGameEnded = False
    preEnd = False
    invalidChar = False
    i = 0
    print("ps if you get stuck you can enter a dot '.' to end the game")
    while hasGameEnded == False:
        if(i > len(nameList)-1):
            i = 0
        print(f"current string: {string}")
        char = input(f"{nameList[i]} add a character!: ")
        if(isValidChar(char.lower()) == False): invalidChar = True
        elif(isWordValid(string + char.lower()) == False): invalidChar = True
        while invalidChar:
            if(char == "."):
                preEnd = True
                break
            invalidChar = False
            print(f"{nameList[i]} that was an invalid character please try again")
            char = input(f"{nameList[i]} add a character!: ")
            if(isValidChar(char.lower()) == False): invalidChar = True
            elif(isWordValid(string + char.lower()) == False): invalidChar = True
        if(isWordExactMatch(string + char) or preEnd):
            print(f"Oh no! you lost...... {nameList[i]}")
            print(f"word you lost to '{string + char}'")
            hasGameEnded = True
        char = char.lower()
        string = string + char
        i += 1
        
def ghost():
    while True:
        cmd = input('Enter s to start a game, or e to end game: ')
        if cmd == 's':
           playGhost()
           print
        elif cmd == 'e':
           break
        else:
           print("Invalid command.")
ghost()