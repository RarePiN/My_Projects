import os
import time
clear = lambda: os.system('clear')

def flag():
  line = '  ║'
  line = line + ("┌")
  for i in range(12):
    line = line + ("─")
  line = line + ("┐")
  print(line)
  
  line = '  ║'
  line = line + "│"
  for i in range(1):
    line = line + " "
  line = line + "★"
  for i in range(4):
    line = line + " "  
  line = line + "⋆"
  for i in range(5):
    line = line + " " 
  line = line + "│"
  print(line)
  
  line = '  ║'
  line = line + "│"
  for i in range(5):
    line = line + " "
  line = line + "⋆"
  for i in range(6):
    line = line + " "
  line = line + "│"
  print(line)
  
  line = '  ║'
  line = line + "│"
  for i in range(2):
    line = line + " "
  line = line + "⋆"
  for i in range(1):
    line = line + " "
  line = line + "⋆"
  for i in range(7):
    line = line + " "
  line = line + "│"
  print(line)
  
  line = '  ║'
  line = line + ("└")
  for i in range(12):
    line = line + ("─")
  line = line + ("┘")
  print(line)

def pole(x,length):
  print("  ▪")
  for i in range(length-x):
    print("  ║")
  flag()
  for i in range(x):
    print("  ║")  
  print("☵☰☰☰☵")

x = 0
length = 19
lyrics=["起来！","不愿 做 奴隶 的","人们!","把 我们 的 血肉","筑成 我们 新的 长城","中华 民族","到 了","最 危险的","时候","每个 人 被迫着","发出 最后的 吼声","起来！起来！起来！","起来！起来！起来！","我们 万众一心，","冒着 敌人 的","炮火， 前进！","冒着 敌人 的","炮火， 前进！","前进！ 前进！ 进！","前进！ 前进！ 进！"]

for i in range(length+1):
  clear()
  pole(x,length)
  x = x + 1
  print(" ")
  if x <= len(lyrics):
    print(lyrics[x-1])
  else:
    print(lyrics[len(lyrics)-1])
  print(" ")
  time.sleep(35.6/20)
  








# 起来！ 不愿 做 奴隶 的 人们！
# 把 我们 的 血肉， 筑成 我们 新的 长城！
# 中华 民族 到 了 最 危险的 时候，
# 每个 人 被迫着 发出 最后的 吼声。
# 起来！ 起来！ 起来！
# 我们 万众一心，
# 冒着 敌人 的 炮火， 前进！
# 冒着 敌人 的 炮火， 前进！
# 前进！ 前进！ 进！  


