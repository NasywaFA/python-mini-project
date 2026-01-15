import random
from libs import welcome_message


welcome_message("HELLO THERE FELAS :3")

#input name
user_name = input('''
Enter your name: ''')

while user_name == '':
    user_name = input('Please enter your name: ')


#greeting
while True:
    #envelope setup
    envelope_shape = '|><|'
    empty_envelope = [envelope_shape] * 5 #original

    letter_position = random.randint(1, 5)

    envelope = empty_envelope.copy() #for the answer

    envelope[letter_position - 1] = '|<3|'
    empty_envelope = ' '.join(empty_envelope)
    envelope = ' '.join(envelope)
    
    print(f'''
    Hello {user_name}! Take a look at the envelopes below
    {empty_envelope}
    ''')

    #question
    user_choise = int(input('Which envelope the letter is in? [1 / 2 / 3 / 4 / 5]: '))
    if user_choise > int('1, 5'):
        print('Invalid input. Please enter a number between 1 and 5.')
        break
            

    confirm_answer = input(f'Are you sure your answer is {user_choise}? [y/n]: ')

    if confirm_answer == "y":
        if user_choise == letter_position:
            print(f'''
    {envelope}
    Congratulations {user_name}, you found the letter!
    ''')
        else:
            print(f'''
    {empty_envelope}
    Sorry, you missed the letter. Please try again~
    ''')
    elif confirm_answer == "n":
        print('Alright, let\'s try again!')
        exit()
    else:
        print('Invalid input. Please try again.')
        exit()
        
    play_again = input('\nWant to continue the game? [y/n]: ')
    if play_again == 'n':
        break
    
print('Thanks For Playing!')