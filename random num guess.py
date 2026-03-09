import random
lowest_number=1
highest_number=100
answer = random.randint(lowest_number, highest_number)
guesses=0
is_running=True
print("python guessing game")
print(f" please select a number between {lowest_number} and {highest_number}")
while is_running:
      guess=input("enter your guess:")
      if guess.isdigit():
           guess=int(guess)
           guesses=+1
           if guess < lowest_number or  guess > highest_number:
             print("that number is out of range")
             print(f"please select a number between {lowest_number} and {highest_number}")
           elif guess < answer:
             print("TOO Low!Try again!")
           elif guess > answer:
            print("TOO High!Try again!")
             
           else:
            print(f"CORRECT! The answer was {answer}")
            print(f"number of guesses:{guesses}")
            is_running = False 
      else:
            print("Invalid input! Please enter a number.")


      
          