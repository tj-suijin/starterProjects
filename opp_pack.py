# Trying out new packages from pypi
# Test: tell jokes until a funny one is brought up
import pyjokes

answer = input("Do you want to hear a joke? [y/n] ")     #asking for user input

if answer == 'y':       #y will be yes and anything else means no 
    answer = True
else:
    answer = False

print(pyjokes.get_joke('en','all'))      #tells a joke in english

while answer is True:       #will tell jokes until funny joke is said
    wow = input("Was that funny? [y/n]")
    if wow == 'y':
        break
    else:
        print(pyjokes.get_joke('en','all'))

print('Thanks for the fun!')
