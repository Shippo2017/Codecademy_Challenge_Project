# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()

  print("Alright, that's a {} {}!".format(size, drink_type))

  cup = cup_type()

  name = input("Can I get your name please? \n>")
  print(f"Thanks, {name}! Your drink will be ready shortly.")


def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")

  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. please enter the corresponding letter for your response.")

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")

  if res == 'a':
    return "Brewed Coffee"
  elif res == 'b':
    return "Mocha"
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>")

  if res == 'a':
    return "latte"
  elif res == 'b':
    return "non-fat latte"
  elif res == 'c':
    return "soy latte"
  else:
    print_message()
    return order_latte()

def cup_type():
  res = input("Would you like a plastic cup or did you bring your own reusable cup? \n[a] I'll need a cup. \n[b] Brought my own! \n>")

  if res == 'a':
    print("Okay, no problem! we'll get you a plastic cup.")
  elif res == 'b':
    print("Great! We'll fill up your reusable cup.")
  else:
    print_message()
    return cup_type()

# Call coffee_bot()!
coffee_bot()
