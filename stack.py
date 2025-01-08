#Palindrome Checker

#Player Input
greeting = int(input("Would you like to check if a word is a Palindrome? Press 1 if you would like to!"))
if greeting == 1:
    player_input = input("Type the word that you want to check: ") 
    
    
#Cleaning the PI 
clean_input = list(player_input.replace(" "," ").lower())

stack = []
#single out the letters
for char in clean_input:
    stack.append(char)
    #pop them and compare
for char in stack:
    compare =  stack.pop()    
    if compare != char:
        print(player_input)
        print("Not a Palindrome")
        #break stops the code if at any point if they dont match so it doesnt run until its finished
        break
else:
    print(player_input)
    print("This is a Palindrome")    

