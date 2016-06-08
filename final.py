import re

easy_text = """A common first thing to do in a language is display 

'Hello __1__!'  In __2__ this is particularly easy; all you have to do 
is type in: 
__3__ "Hello __1__!" 
Of course, that isn't a very useful thing to do. However, it is an 
example of how to output to the user using the __3__ command, and 
produces a program which does something, so it is useful in that capacity. 

It may seem a bit odd to do something in a Turing complete language that 
can be done even more easily with an __4__ file in a browser, but it's 
a step in learning __2__ syntax, and that's really its purpose."""
m
medium_text = """A __1__ is created with the def keyword.  You specify the inputs a 
__1__ takes by adding __2__ separated by commas between the parentheses. 
__1__s by default returns __3__ if you don't specify the value to retrun. 
__2__ can be standard data types such as string, integer, dictionary, tuple, 
and __4__ or can be more complicated such as objects and lambda functions."""

hard_text = """When you create a __1__, certain __2__s are automatically 
generated for you if you don't make them manually. These contain multiple 
underscores before and after the word defining them.  When you write 
a __1__, you almost always include at least the __3__ __2__, defining 
variables for when __4__s of the __1__ get made.  Additionally, you generally 
want to create a __5__ __2__, which will allow a string representation 
of the method to be viewed by other developers. 

You can also create binary operators, like __6__ and __7__, which 
allow + and - to be used by __4__s of the __1__.  Similarly, __8__, 
__9__, and __10_ allow __4__s of the __1__ to be compared 
(with <, >, and ==)."""

blank_list = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__", "__9__", "__10_",]

easy_map = {
    "__1__" : "world",
    "__2__" : "python",
    "__3__" : "print",
    "__4__" : "html"
}

medium_map = {
    "__1__" : "function",
    "__2__" : "arguments",
    "__3__" : "none",
    "__4__" : "list"
}

hard_map = {
    "__1__" : "class",
    "__2__" : "method",
    "__3__" : "__init__",
    "__4__" : "instance",
    "__5__" : "__repr__",
    "__6__" : "__add__",
    "__7__" : "__sub__",
    "__8__" : "__lt__",
    "__9__" : "__gt__",
    "__10_" : "__eq__"
}


def choose_difficulty():

    #Takes user input to define difficulty
    #Accepts the values only in valid_inputs list 
    #Triggers play_game function with respective string and key map
    #Provides necessary instructions to user


    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    user_input = raw_input().lower()
    valid_inputs = ["easy", "medium", "hard"]

    while user_input not in valid_inputs:
        print "That's not an option!"
        print "Please select a game difficulty by typing it in!"
        print "Possible choices include easy, medium, and hard."
        user_input = raw_input().lower()

    if user_input == "easy":
        print "You've chosen " + user_input + "!"
        return play_game(easy_text, easy_map)
    elif user_input == "medium":
        print "You've chosen" + user_input + "!"
        return play_game(medium_text, medium_map)
    else:
        print "You've chosen" + user_input + "!"
        return play_game(hard_text, hard_map)



def play_game (text, key_map):

    #Takes the string and key map related to chosen difficulty
    #Provides instructions to user
    #Displays the string 
    #Splits the text into a list and strips all the punctuation by using a regular expression method
    #Runs a for loop, and if encounters a word in blank_list array, triggers the validator function to validate the answer    

    print "You will get 5 guesses per problem"
    print ""
    print "The current paragraph reads as such:"
    print ""
    print text
    print ""
    
    text = re.findall(r"[\w']+|[.,!?;]", text)
        
    for word in text:

        if word[0:5] in blank_list:

            validator(word, key_map, text)

    return "You won! You little beast. I like you."



def validator (word, key_map, text):

    #Declares an integer to count failed attempts
    #Declares a boolean to restart while loop if the answer is not correct
    #Prompts the question for user input if question not answered correctly and failed attempts are less than 5 
    #Checks if the answer matches with the value in key map
    #If answer is correct, prompts success message and triggers the blank_filler function to fill the blank with correct answer
    #Joins the list into a string
    #Places punctuation properly by using a regular expression method
    #If answer is not correct, adds 1 to fail_counter, and displays number of remaining trials
    #If failed more than 5 times, finishes the game

    fail_counter = 0
    success = False

    while fail_counter < 5 and success != True:

        answer = raw_input("What should be substituted in for " + word[0:5] + "?").lower()
        answer_text = []
        
        if answer == key_map[word[0:5]]:
   
            success = True

            print ""
            print "Correct!"
            
            blank_filler(word,text,answer)

            answered_text = " ".join(text)     
            print re.sub(" ([,.!?:;'\)])", lambda m: m.group(1), answered_text)
            print ""
            
        else:
            fail_counter += 1
            print "Sorry, wrong answer. You have " + str(5 - fail_counter) + " trials left." 
            
    while fail_counter >= 5:
        return "You failed too many times.. Game over"


def blank_filler (word, text, answer):
    
    #Works only if answer is correct
    #Takes the word from for loop in play_game function, game string (which is converted into a list) and user answer as input
    #Runs a for loop, and if encounters the blank under question, replaces it with the correct answer
    #Uses a counter to detect the position of the blank to be replaced in the list
    #Takes affixes into consideration 

    counter = 0
    for to_replace in text:
        if word[0:5] == to_replace[0:5]:
            text[counter] = answer + to_replace[5:]
        counter += 1        
    
    

print choose_difficulty()    # fill-in-the-blanks
# fill-in-the-blanks
