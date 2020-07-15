# Decoration stuff

print('=====================================================================')
print('                     Test.py is ready for use!                          ')
print('=====================================================================\n')

x = input("\t* Type something here: \t") # taking user input

y = x.count(" ") # counting spaces provided in user input
 
digits = len(x) - y # subtracting no. of spaces from the user input

print("\n\tNow since your input i.e., '", x.capitalize(), "' was\n\t received with", len(x), "digit(s) and you gave", y, "space(s), therefore\n\t the no. of digits is equal to ", digits, "DIGIT(s)\n\n")

# Decoration stuff, again
print("         ===   ==================================   ==")
print('                 **    Output ends here!   **         ')
print("         ===   ==================================   ==") 

# Hope you got what you're lookin' for!