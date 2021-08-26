# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    n=0
   
    Word = []
    Word = list(secret_word)
    for i in Word :
        for j in letters_guessed :
            if i == j :
                n +=1
    if n == len(secret_word):
        return True
    else :
        return False
    
    
    
            
            


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    l =[]
    l=list(secret_word)
    m=[]
    flag =False
    for i in l:
        for j in letters_guessed:
            if i == j:
                m.append(i)
                flag = True
               
            if flag == False and j == letters_guessed[len(letters_guessed)-1]:
                m.append("_")
                
        flag =False
    if "_" in m :
            h=' '.join(m)
    else :
            h=''.join(m)
    return h


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    n=string.ascii_lowercase
    h=list(n)
    for i in letters_guessed:
        if i in h:
            h.remove(i)
    return ''.join(h)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    users =[]
    print ("Welcome to the game hungman!")
    print ("I am thinking of a word that is",len(secret_word),"letters long")
    print("You have 3 warnings left.")
    print("------------")
    w =3
    j=6
    while j !=0:
        if is_word_guessed(secret_word, users):
            print("Congratulations ,you win!")
            print("Your total score for this game is:",j*len(set(secret_word)))
            break
        else :   
            print ("You have",j,"guesses left.")
            print ("Avaliable letters:",get_available_letters(users))
            inp = input("please guess a letter:")
            if inp in users :
                w =w-1
                if w>=0:
                    print("You have already guessed that letter. You have",w,"warnings left.")
                else :
                    j =j-1
                    print ("You have no warnings left.so you will lose one guess.")
                print(get_guessed_word(secret_word,users))
            else :
                
               if str.isalpha(inp):
                    users.append(str.lower(inp))
                    if inp in secret_word :
                        print ("Good guess:",get_guessed_word(secret_word,users))
                    else :
                        if inp in ["e","o","u","i","a"]:
                            if j==1:
                                j=0   
                            else:
                                j=j-2
                        else :
                            j=j-1
                        print ("Oops! That letter is not in my word:",get_guessed_word(secret_word,users)) 
               
               else :
                   w =w-1
                   if w == 0:
                       j =j-1
                   print("Oops! this is not a valid input.You have",w,"warnings left.",get_guessed_word(secret_word,users))
            print ("------------")
    if j ==0:
        print("Sorry, you ran out of guesses. The word was",secret_word)
        
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    myword = my_word.replace(" ","")
    word = list(myword)
    hint=list(other_word)
    #print (word,hint)
    l=word[:]
    h=hint[:]
    c=l.count("_")
    n=0
    if len(word) == len(hint):
        for i in word:
            if i == "_":
                x=l.index("_")
                k=h[x]
                if not k in word :
                    n=n+1
                  
                if c !=1:
                    l.pop(x)
                    h.pop(x)
                    c=c-1
        if "_" in l :
            s=l.index("_")
            l.pop(s)
            h.pop(s)
           #print (l==h)
        if l == h:
            n=n+len(l)
        if  n==len(word):
            return True
        
        else:
            #print("hi")
            return False
    else:
        #print("hello")
        return False 
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    n=0
    p=[]
    for i in wordlist :
        if match_with_gaps(my_word,i ):
            p.append(i)    
            n=n+1
    if n ==0:
        print("No matches found")
    if n!=0:
        g=' '.join(p)
        print("possible word matches are:",g)
    
    


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    users =[]
    print ("Welcome to the game hungman!")
    print ("I am thinking of a word that is",len(secret_word),"letters long")
    print("You have 3 warnings left.")
    print("------------")
    w =3
    j=6
    while j !=0:
        if is_word_guessed(secret_word, users):
            print("Congratulations ,you win!")
            print("Your total score for this game is:",j*len(set(secret_word)))
            break
        else :   
            print ("You have",j,"guesses left.")
            print ("Avaliable letters:",get_available_letters(users))
            inp = input("please guess a letter:")
            if inp in users :
                w =w-1
                if w>=0:
                    print("You have already guessed that letter. You have",w,"warnings left.")
                else :
                    j =j-1
                    print ("You have no warnings left.so you will lose one guess.")
                print(get_guessed_word(secret_word,users))
            else :
                
               if str.isalpha(inp):
                    users.append(str.lower(inp))
                    if inp in secret_word :
                        print ("Good guess:",get_guessed_word(secret_word,users))
                    else :
                        if inp in ["e","o","u","i","a"]:
                            if j==1:
                                j=0   
                            else:
                                j=j-2
                        else :
                            j=j-1
                        print ("Oops! That letter is not in my word:",get_guessed_word(secret_word,users)) 
               
               else :
                   if inp == "*":
                      #print (get_guessed_word(secret_word,users))
                      show_possible_matches(get_guessed_word(secret_word,users)) 
                   else:   
                       w =w-1
                       if w == 0:
                           j =j-1
                       print("Oops! this is not a valid input.You have",w,"warnings left.",get_guessed_word(secret_word,users))
        print ("------------")
    if j ==0:
        print("Sorry, you ran out of guesses. The word was",secret_word)
        
    #print (wordlist)


# When you've completed your hangman_with_hint function, comment the two similar
#lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
  # choose_word(wordlist)
   # secret_word =  
   # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
  
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
