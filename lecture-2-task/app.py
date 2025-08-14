import random


def get_rand_num():
    return random.randrange(1, 10)


def generate_question():
    rand_num1 = get_rand_num()
    rand_num2 = get_rand_num()
    question = f"What is {rand_num1} x {rand_num2}?"
    correct_answer = rand_num1 * rand_num2
    return question, correct_answer


print("Welcome to the simple multiplication quiz!")
print("You will be given 5 multiplication problems to solve.\n")
max_score = 5
user_score = 0


for _ in range(5):
    question, correct_answer = generate_question()
    print(question)

    try:
        user_input = int(input("Your answer: "))

        if user_input == correct_answer:
            print("Correct!\n")
            user_score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}\n")
    except ValueError:
        print("Not an integer\n")

print(f"You scored {user_score} out of {max_score}. Well done!")
