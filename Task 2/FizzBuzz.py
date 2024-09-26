import random

def fizz_buzz_game():
    rounds = 5  

    for _ in range(rounds):
        number = random.randint(1, 200)
        
        if number % 3 == 0 and number % 5 == 0:
            correct_answer = "Fizz Buzz"
        elif number % 3 == 0:
            correct_answer = "Fizz"
        elif number % 5 == 0:
            correct_answer = "Buzz"
        else:
            correct_answer = str(number)

        
        user_input = input(f"What should you say for {number}? ")
        
        4
        if user_input.strip().lower() != correct_answer.lower():
            print(f"Wrong! The correct answer was '{correct_answer}'.")
            print("Game over!")
            break
    else:
        print("Congrats! You completed all rounds!")


fizz_buzz_game()
