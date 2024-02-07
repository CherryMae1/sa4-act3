number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
amt_guess = 5


while True:
  if guess == str(number):
    print("Congratulations! You guessed the right number.")
    break
  elif guess == 'q' or guess == 'Q':
    print(f"You have quit, the number was: {number}.")
    break
  else:
    amt_guess -= 1
    print(f"You have {amt_guess} left.")
    if amt_guess == 0:
      print('You have run out of guesses.')
      break
    guess = input("What number am I thinking of? ")
  

