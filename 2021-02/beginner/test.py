from fuzzywuzzy import fuzz
import time

phrase = 'She sells seashells by the seashore'
ans = True
while ans:
    print('\nInstructions: You will be shown a phrase, and you have to type it as fast and accurate as possible!')
    print('\nAre you ready? (Press any key to continue)')
    ans = input('>> ')
    if ans:
        print(phrase)
        start = time.time()
        result = input('>> ')
        end = time.time()
        Ratio = fuzz.ratio(phrase,result)
        print('Your accuracy was '+str(Ratio)+'%!')
        print('Your time was '+"{:.2f}".format(end-start)+' seconds!')
        ans2 = True
        while ans2:
            print('\nDo you want to try again? (Y/N)')
            ans2 = input('>> ')
            if ans2.lower()=='n':
                ans2 = False
                ans = False
                print('Bye!')
            elif ans2.lower()=='y':
                ans2 = False
                ans = True
            else:
                print('Invalid answer. Please try again.')
                
#Ideas for added challenge
#Offer the user different phrases
#Should it be case sensitive?
#Create a scoreboard: Ask users for their name and keep the attempts
#Create a score that averages speed and accuracy!            

#%%

