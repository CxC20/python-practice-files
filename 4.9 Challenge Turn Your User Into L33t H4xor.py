##Write a script called translate.py that asks the user for some input
##with the following prompt: Enter some text:. Then use the .replace()
##method to convert the text entered by the user into “leetspeak” by making
##the following changes to lower-case letters:
##• The letter a becomes 4
##• The letter b becomes 8
##• The letter e becomes 3
##• The letter l becomes 1
##• The letter o becomes 0
##• The letter s becomes 5
##• The letter t becomes 7
##Your program should then display the resulting string as output. Below
##is a sample run of the program:
##Enter some text: I like to eat eggs and spam.
##I 1ik3 70 347 3gg5 4nd 5p4m.

leet_input = input("Enter some text: ")
leet_input = leet_input.replace("a", "4")
leet_input = leet_input.replace("b", "8")
leet_input = leet_input.replace("e", "3")
leet_input = leet_input.replace("l", "1")
leet_input = leet_input.replace("o", "0")
leet_input = leet_input.replace("s", "5")
leet_input = leet_input.replace("t", "7")
print(leet_input)
