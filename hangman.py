import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)            
display=[]
for i in range(len(chosen_word)):
    display+="_"
lives=6


from hangman_art import hangman_art

from hangman_art import stages

print(hangman_art)
print(f"{' '.join(display)}")
while True:
    
    guess=input("Enter your guess:").lower() 
    
    if guess in display:
        print("you have already guessed this alphabet")
    
    for j in range(len(chosen_word)):
        if chosen_word[j] == guess:
            display[j]=guess
            
    
    
    
    if guess not in chosen_word:
        print("wrong guess!")
        lives-=1
        print(f"your current lives are:{lives}")
        if lives==0:
            print('\n')
            print("You lose")
            break        
    if "_" not in display:
        print("Congratulations\n\tYou Won!")
        break
    
    print(stages[lives])
    
    print(f"{' '.join(display)}")   
