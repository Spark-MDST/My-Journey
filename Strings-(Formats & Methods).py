name = 'Spark'                                  #This is a variable for name, It will print what is in the quotes

goal = 'working to inspire and teach others'    #This is another variable but this one is a goal, It will print what is in the quotes.

msg = f"My name is {name}, and I'm {goal} "     #This is another varible named 'msg'. It is formatted to use the text within the quotes to pair with the 2 other variables given. Essentially like filling in the blanks 



#_____________________________________________________________________________________________________________________



####           -------          NOTES           --------       ####

##        (A method is a way to manipulate the variable to do certain actions)          ##



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



##        - The (len) function is used to count the number of characters in a string.

print(len(msg))     # This program is: Print the number of characters in |msg| 



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



##       - The (.upper) & (.lower) method will print all of the text in 'msg' to be uppercase or lowercase letters respectively.

print(msg.upper())      # This program is: Print the entirety of letters in |msg| to be uppercase

print(msg.lower())      #This program is: Print the entirety of letters in |msg| to be lowercase



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



##      - The (.find) method will print the index number of the character within the quotes.
##      - The (.find) method is case sensitive       

print(msg.find('I'))        # This program is: Print the index number of the letter |I|

print(msg.find('Spark'))    # This program is: Print the index of the first letter of the word |Spark|



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



##      - The (.replace) method will replace any chosen text with a another chosen text

print(msg.replace('Spark', 'krapS'))   # Essentially this program is: Replace |Spark| with |krapS| in |msg| and print.

print(msg.replace('S', 'Sh'))          # Essentially this program is: Replace |S| with |Sh| in |msg| and print.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



##      - The 'in' method will search if the text within the quotes is in the variable you choose in this example: (variable = msg)

print('Spark' in msg)   # Essentially the program is asking "Search to see if |Spark| is |in| the |msg|, if it is then print true, if not false

print('Python' in msg)  # Essentially the program is asking "Search to see if |Python| is |in| the |msg|, if it is then print true, if not false