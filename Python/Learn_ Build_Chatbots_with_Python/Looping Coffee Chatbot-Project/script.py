def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'
  drinks = []

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)

    while True:
      order_drink = input("Would you like to order another drink? (y/n) \n>")

      if order_drink in ['Y', 'yes', 'sure']:
        order_drink = 'y'
      elif order_drink in ['N', 'no', 'nah']:
        order_drink = 'n'
      if order_drink in ['y', 'n']:
        break
  print("Your order:")

  for drink in drinks:
    print('-', drink)
  
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))
  
  
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')
  
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return brewed_coffee()
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
 def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte() 
  
# Define new functions here!
def order_mocha():
  while True:
    res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>")

    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return "mocha"
   
    print_message()

def brewed_coffee():
  res = input("Would you like to try our Colombian Coffee? \n[a] Absolute! \n[b] Not today! \n>")

  if res == 'a':
    return 'Colombian brewed coffee'
  elif res == 'b':
    return 'original brewed coffee'
  
  print_message()

# Returns user input or returns to the beginning if the input is "stop" (order is cancelled).
def order_input(text):
    res = input(text)
    if res == "stop":
        print("Order cancelled!")
        coffee_bot()
    else:
        return res

coffee_bot()

