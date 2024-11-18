import random

# Function to take user input for questions and answers
def setup_quiz(num_questions):
    questions = []
    answers = []
    for i in range(num_questions):
        question = input(f"Enter question {i + 1}: ")
        answer = input(f"Enter the correct answer for question {i + 1}: ").strip().lower()
        questions.append(question)
        answers.append(answer)
    return questions, answers

# Function to run the quiz for a user
def run_quiz(questions, answers):
    score = 0
    user_answers = []
    # Shuffle questions and answers in a random order
    question_order = list(range(len(questions)))
    random.shuffle(question_order)

    for i in question_order:
        user_answer = input(f"{questions[i]}: ").strip().lower()
        user_answers.append((questions[i], user_answer, answers[i]))
        if user_answer == answers[i]:
            score += 1

    return score, user_answers

# Main function to handle multiple users
def main():
    # Get the number of questions from the user
    while True:
        try:
            num_questions = int(input("Enter the number of questions for the quiz: "))
            if num_questions <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Set up quiz questions and answers
    questions, answers = setup_quiz(num_questions)
    
    scores = {}  # Store scores for each user
    total_score = 0
    num_users = 0

    while True:
        name = input("\nEnter your name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        score, user_answers = run_quiz(questions, answers)
        total_score += score
        num_users += 1
        scores[name] = score

        print(f"\n{name}, your score: {score}/{num_questions}")
        print(f"Percentage: {score * 100 / num_questions:.2f}%")

        print("\nReview of your answers:")
        for question, user_answer, correct_answer in user_answers:
            if user_answer == correct_answer:
                print(f"Correct: {question} - Your Answer: {user_answer}")
            else:
                print(f"Incorrect: {question} - Your Answer: {user_answer}, Correct Answer: {correct_answer}")

        # Ask if another user wants to take the quiz or if the current user wants to replay
        another = input("\nWould you like to play again or let another user take the quiz? (yes to continue / no to exit): ").strip().lower()
        if another != 'yes':
            break

    # Display results and statistics
    if num_users > 0:
        max_score_user = max(scores, key=scores.get)
        avg_score = total_score / num_users
        print("\n--- Quiz Summary ---")
        for user, score in scores.items():
            print(f"{user}'s score: {score}/{num_questions}")
        print(f"\nUser with the highest score: {max_score_user} ({scores[max_score_user]}/{num_questions})")
        print(f"Average score: {avg_score:.2f}/{num_questions}")

if __name__ == "__main__":
    main()
