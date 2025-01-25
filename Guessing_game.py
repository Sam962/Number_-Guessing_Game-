#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

print("*** Welcom To The Guessing The Number Game!! ***")
def start_game():
    print("*** Welcom To The Guessing The Number Game!! ***")
    
    while True:
        start = input("Start The Game! (Yes/No): ....").strip().lower()
        if start =="yes":
            print("LET'S GOOO..")
            break
        else:
            print("See you Soon!")


    # create the random number 
    rand_num = random.randrange(100)


    # set a Limit of attempt for user to guess
    total_guess_num = 7

    # init limit (number of attempts)
    guess_init = 0

    # start the while loop for the program
    while guess_init < total_guess_num:

        # ask the user to Enter their guess number!
        gus_num = int(input("Enter your Guess Number: "))
        guess_init += 1

        if gus_num == rand_num:
            print(f" Winner!! you match the Number in {guess_init} attempts")
            break

        elif guess_init >= total_guess_num and gus_num != rand_num:
            print("Sorry! Game Over! try Again :) ")

        elif gus_num > rand_num:
            print(f"Your number {gus_num} is HIGHER!")

        elif gus_num < rand_num:
            print(f"your number {gus_num} is LESSER!")

        
start_game()


# In[ ]:





# In[ ]:




