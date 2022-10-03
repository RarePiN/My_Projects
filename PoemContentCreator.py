import random

#Do not have enough words for your homework? No worry! Use this program to increase the word count of your poem.

pessage = input("Input your pessage:")
microsoft = pessage.split()
words = ['riot','mood','piano','corner','mean','spare','expect','dead','mosque','west','infrastructure','patrol','hot','gear','onion','occupy','pledge','architecture','impulse','deprive','favourite','access','belong','crowd','distribute','negligence','redundancy','hut','orange','constant','bracket','fair','sow','embark','divorce','hostage','terrify','fun','association','minister','appeal','user','disturbance','harmony','camp','estimate','choice','legend','treat','ribbon','simplicity','boom','joystick','raptor','stealth','jet','possible','enterprise','bullshit']
count = len(microsoft)

wordincrease = int(input("How many words you wanna increase?"))

for i in range(wordincrease):
    position = random.randint(0,wordincrease)
    microsoft.insert(position, random.choice(words))

final = ''
total = count + wordincrease

for k in range(int(total)):
    final = final + " " + microsoft[k] + " "

print(final)
