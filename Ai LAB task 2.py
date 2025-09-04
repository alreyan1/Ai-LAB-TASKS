print("FizzBuzz Game")

points = 0
rounds = 10   
for num in range(1, rounds + 1):
    print(f"Round {num}: The number is {num}")
    answer = input("Your answer: ")

    if num % 3 == 0 and num % 5 == 0:
        correct = "FizzBuzz"
    elif num % 3 == 0:
        correct = "Fizz"
    elif num % 5 == 0:
        correct = "Buzz"
    else:
        correct = str(num)

    if answer == correct:
        print("Correct! Well done.")
        points += 1
    else:
        print(f"That was incorrect. The right answer was: {correct}")

    print(f"Current Score: {points}")
    print("-" * 40)

print("Game Over!")
print(f"Your Final Score: {points} out of {rounds}")
