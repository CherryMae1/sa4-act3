number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))


while True:
  if guess == str(number):
    print("Congratulations! You guessed the right number.")
    break
  elif guess == 'q' or guess == 'Q':
    print(f"You have quit, the number was: {number}.")
    break
  else:
    num = int(guess)
    if num < number:
      print("Your guess is too low, please try again or press 'q' to quit.")
    elif num > number:
      print("Your guess is too high, please try again or press 'q' to quit.")
      
  guess = input("What number am I thinking of? ")

