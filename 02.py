import random
lvl = 0
diffi = 10000
guess = 0
computer_guess = random.randint(1,diffi) #selects any number between 0 to 11

while 1>0:
    user_guess = input("Enter your guess guess: ")
    try:
        user_guess = int(user_guess)
    except Exception as e:
        print("Please enter a vaild number.")


    
    if user_guess > computer_guess:
        print("Too High")
        guess +=1
    elif user_guess < computer_guess:
        print("Too Low")
        guess +=1

    elif user_guess == computer_guess:
        print(f"You won! You guessed {guess} times.")
        ans = input("Do You want to play again? Yes Or No: ")
        new_ans = ans.lower()
        if ans == 'yes':
            print("Okay let's play again!")
            diffi += 10
            lvl += 1  #same as lvl = lvl + 1
            guess = 0
            computer_guess = random.randint(1,diffi)
        else:
            print(f"You have completed till level {lvl}.")
            print("Exiting the game. Have a nice day!")
        

