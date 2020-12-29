# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:14:10 2020

@author: Bashir
"""
from coffee_bot_loops_extra_funtions import print_message, get_size, order_latte

  
def coffee_bot():
  print('Welcome to the cafe!')
  order_drink = 'yes'
  drinks=[]
  while order_drink == 'yes':
   size = get_size()  
   drink_type = get_drink_type()
   drinks.append(drink_type)

   drink = '{} {}'.format(size, drink_type)
   print('Alright, that\'s a {}!'.format(drink))
   res = ""
   while res  not in ["a","b"]:
     res = input("Do you want another drink\n[a]yes\n[b]no\n")
     # if res == "a":
     #  order_drink = "yes"
     #  return order_drink
     if res == "b":
      order_drink = "no"
      print("Okay!Thanks")
      
  
  
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))
  print("Okay so I have:\n")
  for item in drinks:
      print(item)
     

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!
def order_mocha():
  while True:

   res = input("Would you like to try our limited-edition peppermint mocha?\n[a] Sure!\n[b] Maybe next time!\n")
   if res == "a":
     return "peppermint mocha"
   elif res == "b":
     return "mocha"
   print_message()


####main
coffee_bot()
