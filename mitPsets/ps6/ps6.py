# Problem Set 5: 6.00 Word Game
# Name: dominic denti
# Collaborators: none
# Time: 5:00

import time
import random
from itertools import combinations

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 
    'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    return wordlist
word_list = load_words()
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
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

def get_word_score(word):
    if(len(word) == HAND_SIZE): num = 50
    else: num = 0
    for i in range(len(word)):
        num += SCRABBLE_LETTER_VALUES[word[i].lower()]
    return num

def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    """
    pointDict = {}
    num = 0
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            num += SCRABBLE_LETTER_VALUES[word_list[i][j]]
        pointDict[word_list[i]] = num
        num = 0
    return pointDict
POINTS_DICT = get_words_to_points(load_words())

def timed_get_word_score(word,time,timeToAnswer):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    if(HAND_SIZE == len(word)):num = 50
    else: num = 0
    for i in range(len(word)):
        num += SCRABBLE_LETTER_VALUES[word[i].lower()]
    num = round(num / max(time,1),2)
    if(time > timeToAnswer):
        return 0
    return num

def get_time_limit(points_dict, k):
    """
     Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word)
    end_time = time.time()
    return (end_time - start_time) * k
timeLimit = get_time_limit(POINTS_DICT,20)

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    string = ""
    for i in hand:
        for j in range(hand[i]):
            string += i
    print(string)
    return string

def hand_to_str(hand):
    string = ""
    for i in hand:
        for j in range(hand[i]):
            string += i
    return string

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def is_valid_word_rearranged(word, hand, rearranged_dict):
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return word in rearranged_dict

def is_valid_word(word, hand, pointsDict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return word in pointsDict

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = dict(hand)
    for i in range(len(word)):
        if(word[i] in newHand):
            newHand[word[i].lower()] -= 1
    return newHand

def WordSort(str):
    return ''.join(sorted(str))

def get_word_rearrangements(word_list):
    d = {}
    for w in word_list:
        d[WordSort(w)] = w
    return d

REARRANGED_DICT = get_word_rearrangements(word_list)

def pick_best_word(hand, points_dict):
    """
     Return the highest scoring word from points_dict that can be made with the
     given hand.
     Return '.' if no words can be made with the given hand.
     O(len(wordlist)**len(wordlist))
    """
    arr = [0,""]
    tic = time.time()
    for word in word_list:
        if(is_valid_word(word, hand, points_dict)):
            if(arr[0] < get_word_score(word)): arr = [get_word_score(word),word]
    toc = time.time() - tic
    if(arr[1] == ""): arr[1] = "."
    return(arr[1],toc)

def rearrange_arr(hand):
    """
        takes an input of hand and returns all sub-multisets as an array
    Args:
        hand: dict
    """
    hand = WordSort(hand_to_str(hand))
    temp_str = ""
    for letter in hand: temp_str += f"{letter},"
    hand = temp_str[:len(temp_str)-1]
    iterable = hand.split(',')
    arr = []
    multisets = set()
    for r in range(1, len(iterable)+1):
        for comb in combinations(iterable, r):
            out = ','.join(comb)
            if out not in multisets:
                multisets.add(out)
                for letter in out:
                    if(letter == ","): continue
                    else: temp_str += letter
                arr.append(temp_str)
                temp_str = ""
    return(arr[1:])
# print(rearrange_arr(deal_hand(HAND_SIZE)))

def pick_best_word_faster(hand, rearrange_dict):
    """
     takes two inputs and returns the best possible word and the time 
     it takes to find it.
     Args:
        hand: is a dictonary of characters
        rearrange_dict: is a dict of all words in word list sorted
     O(len(rearrange_arr)**len(rearrange_dict))
    """
    tic = time.time()
    arr = [0,""]
    for word in rearrange_arr(hand):
        if(word in rearrange_dict):
            if(arr[0] < get_word_score(word)): arr = [get_word_score(word),rearrange_dict[word]]
    toc = time.time() - tic
    if(arr[1] == ""): arr[1] = "."
    return(arr[1],toc)
# print(pick_best_word_faster(deal_hand(HAND_SIZE),REARRANGED_DICT))
    
def test_pick_best_word_faster():
    """
    tests both pick best word functions and 
    prints out the faster function
    """
    for i in range(100):
        hand = deal_hand(HAND_SIZE)
        print(hand)
        pbw = pick_best_word(hand,POINTS_DICT)
        pbwf = pick_best_word_faster(hand,REARRANGED_DICT)
        print(f"pbw: {pbw}, pbwf: {pbwf}")
        if(pbw[1] > pbwf[1]): print(f"pbwf wins!!! time: {pbwf[1]}")
        elif(pbw[1] < pbwf[1]): print(f"pbw wins!!! time: {pbw[1]}")
        else: print("it's a tie")
# test_pick_best_word_faster()
def num_letters_in_hand(hand):
    """takes an input of hand and returns the total number of letters in hand
    Args:
        hand: dict
    Returns:
        num: an integer representing the number of letters in hand
    """
    num = 0
    for letter in hand:
        num += hand[letter]
    return num

def getWordTime(totalTime = 0):
    """times the user's input and returns the time it takes and word they typed
    Args:
        totalTime: the ammount of time the user(if any) has spent guessing
    """
    tic = time.time()
    word = input("input a word, or, a '.' to indicate you are finished: ")
    toc = round((time.time() - tic) + totalTime, 2)
    return(word, toc)

def play_hand(hand,word_list,score,timeToPlay):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      score: current player score type int
    """
    display_hand(hand)
    arr = pick_best_word_faster(hand,POINTS_DICT)
    while is_valid_word(arr[0],hand,POINTS_DICT) == False:
        if(arr[0] == "." or num_letters_in_hand(hand) < 1):
            print(f"====================\nfinal score: {score}")
            return score
        print("invalid word, please try again")
        arr = pick_best_word_faster(hand,POINTS_DICT)
    hand = update_hand(hand, arr[0])
    score += timed_get_word_score(arr[0],arr[1],timeToPlay)
    timeToPlay -= arr[1]
    print(f"total score:", score)
    print(f"it took you {round(arr[1],2)} to provide an answer")
    if(timeToPlay < 0):
        print(f"you've run out of time. You scored {round(score,2)} points.")
        return 1
    print(f"you have {round(arr[1],2)} seconds left")
    play_hand(hand,word_list,score,timeToPlay)
    
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if(cmd == 'e'):
            break
        timeToPlay = int(input("enter time limit(in seconds), for players: "))
        while timeToPlay <= 0:
            print(f"enter a positive value")
            timeToPlay = int(input("enter time limit(in seconds), for players: "))
        if cmd == 'n':
           score = 0
           hand = deal_hand(HAND_SIZE)
           play_hand(hand.copy(), word_list,score,timeToPlay)
           print
        elif cmd == 'r':
           score = 0
           play_hand(hand.copy(), word_list,score,timeToPlay)
           print
        else:
           print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)