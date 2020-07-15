# python-program-to-count-exact-no.-of-digits
This program tells the user the exact no. of digits in his/her input

# how it works_

+ The user types values:

<code>x = input("\t* Type something here: \t") # taking user input</code><br>
The program saves the input and stores in '<strong>x</strong>'

+ The program counts the no. of times space has been provided:

<code>y = x.count(" ") # counting spaces provided in user input</code><br>
The program stores this information in '<strong>y</strong>'

+ Creating a new variable to store the exact no. of digits:

<code>digits = len(x) - y # subtracting no. of spaces from the user input</code><br>
and thus, we get are required output!

