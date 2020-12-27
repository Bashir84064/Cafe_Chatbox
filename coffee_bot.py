# Define your functions
#greetings
def greetings():
  print ("Welcome to the cafe")
#user_name
def user_name():
  name = str(input("Can I get your name\n"))
  return name
#coffee size
def get_size():
  """res = None
  size = None
  #prompts till user give input from the requested options
  while res not in ['a','b','c']:
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
    if res == "a":
      size = "Small"
    elif res == "b":
      size = "Medium"
    elif res == "c":
      size= "Large"
     
  return size"""
#another implementation with recursive function
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

  
  if res == "a":
       res = "Small"
  elif res == "b":
       res = "Medium"
  elif res == "c":
       res= "Large"
  else:
       print_message()
       res=get_size()
       return res

     
  return res
#print_message for invalid input
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
#function to get type of drink
def get_drink_type():
  res = input("What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n")
  if res == "a":
    res = " Brewed Coffee"
  elif res == "b":
    res = "Mocha"
  elif res =="c":
    res ="Latte"
    res = order_latte() + " "+"Latte"
  else:
    print_message()
    res = get_drink_type()
    return res
  return res
#function if user orders latte
def order_latte():
  res= input("And what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n")
  if res == "a":
    res = "2% milk"
  elif res == "b":
    res = "Non-fat milk"
  elif res=="c":
    res = "Soy milk"
  else:
    print_message()
    res = order_latte()
    return res
  return res
 #option to use plastic cup or own  
def cup_type():
  cup_type = None
  cup=None
  while  cup_type not in {"a","b"}:
    cup_type = input("Would you like?\n[a]Plastic cup\n[b]Own Cup\n")
    if cup_type=="a":
      cup= "Platsic Cup"
    elif cup_type=="b":
      cup="Own Cup"
  return cup

# Complete functionality!
def coffee_bot():
#1 fetch coffee_size from user
  size= get_size()

#2 fetch coffee type from user
  drink_type=get_drink_type()
#3 choice of cup
  cup=cup_type()
#outputs the order
  print("Alright,that's a {},{} in {}!".format(size,drink_type,cup))
  print("Thanks,{}! Your drink will be ready shortly.".format(name))

 #Function for another order
def another_order():
  res = input("do you want anything else?\n[a]yes\n[b]no\n")
  if res =="b":
    res="Okay have a nice day"
  elif res== "a":
    res = coffee_bot()
    
  else:
    res= another_order()
    return res

  return res
   
 
 ############################################
#coffee bot in action
greetings()
#get user name
name = user_name()
coffee_bot()
another_order()
