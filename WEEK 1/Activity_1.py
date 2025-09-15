# [ALEX FHERMAYE]
# Python Version 3.11.4
# Activity 1

colors = "red, orange, yellow, green, blue, indigo, violet"
print("The colors in the Rainbow are: ")
#for color in colors:
print(colors)

#Error 1
# colors = ['red', 'orange', "yellow", "green", "blue', 'indigo', 'violet']
# SyntaxError: unterminated string literal (detected at line 1)

# - This error occurred because in line 1 of the code, all words are separated by string quotations instead of the entire sentence being a string by itself. 

#_________________________________________________

#Error 2
# print('The colors in the Rainbow are: ")
# SyntaxError: unterminated string literal (detected at line 2)

# - This error occurred because the string text that is supposed to be printed does not have quotation marks in the beginning of the text. 

#__________________________________________________

#Error 3
#print(colors))
#SyntaxError: unmatched ')'

# - This error occurred because there was an extra parentheses after the initial correct one at the end of the print command for colors and the sentence "for color in colors:" needs to be converted into a comments sentence so that the command can run properly. 