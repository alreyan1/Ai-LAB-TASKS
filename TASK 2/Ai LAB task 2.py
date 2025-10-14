print("FizzBuzz Game")

points = 0
rounds = 10
pre = 0
curr = 1

for num in range(1, rounds + 1):
    total_num = pre + curr
    print(f"Round {num}: The number is {total_num}")
    answer = input("Your answer: ")
    pre = curr
    curr = total_num

    if total_num % 3 == 0 and total_num % 5 == 0:
        correct = "FizzBuzz"
    elif total_num % 3 == 0:
        correct = "Fizz"
    elif total_num % 5 == 0:
        correct = "Buzz"
    else:
        correct = str(total_num)

    if answer == correct:
        print("Correct! Well done.")
        points += 1
    else:
        print(f"That was incorrect. The right answer was: {correct}")

    print(f"Current Score: {points}")
    print("-" * 40)

print("Game Over!")
print(f"Your Final Score: {points} out of {rounds}")
