# -*- coding: utf-8 -*-

import re
print("Начать изменение письма?  Да-1 Нет-2")
a = int(input())
if a == 1:
    with open('letter.txt') as fl:
     let = fl.read()
     def repl(m): 
      return '[censored]'
    print(let)
else: 
    print("Выход")