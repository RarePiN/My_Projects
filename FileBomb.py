import os

#It will create a very large file, becare.

with open('Game.txt', 'w') as f:
  for i in range(500000):
    print(i)
    for i in range(2500):
      f.write('I am Scout from TF2.')
