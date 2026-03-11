import random
import string
import secrets

adjectives = ['sleepy','slow','smelly',
              'wet','fat','red',
              'orange','yellow','green',
              'blue','purple','fluffy',
              'white','proud','brave',
              'gigantic', 'tiny', 'swift',
              'dark', 'bright', 'calm', 'loud',
              'happy', 'sad']
nouns = ['apple','dinosaur','ball',
         'toaster','goat','dragon',
         'hammer','duck','panda',
         'cat', 'dog', 'mouse',
         'computer', 'car', 'book',
         'sky', 'ocean', 'mountain']

print('Welcome to Password Picker!')

password_length = int(input("Enter the desired password length"))
while True:
    adjective = secrets.choice(adjectives)
    noun = secrets.choice(nouns)
    number = secrets.randbelow(100)
    special_char = secrets.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your New Password Is: %s' % password)

    response = input('Would you like a new password? Type y or n: ')
    if response == 'n':
        break
    


