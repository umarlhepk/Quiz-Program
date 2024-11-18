# Quiz Program

## Overview
This Quiz Program is a Python-based console application that allows multiple users to take a customizable quiz. It's designed for practice and learning, making use of Python features such as loops, conditional statements, functions, and data structures.

## Features
- Customizable number of questions.
- Randomized question order for every quiz session.
- Tracks individual user scores and provides feedback.
- Displays statistics, including:
  - Scores for all users.
  - The highest score.
  - The average score of all users.
- Handles invalid inputs gracefully (e.g., empty names or invalid answers).

## How It Works
1. The admin user specifies the number of questions and inputs them along with the correct answers.
2. Each quiz taker:
   - Enters their name.
   - Answers the quiz questions.
   - Receives feedback on their performance (score, percentage, and a review of correct/incorrect answers).
3. The program allows multiple users to take the quiz in one session.
4. After all users finish, a summary of results is displayed.

## Technologies Used
- **Programming Language**: Python
- **Modules**: `random` for shuffling questions.

## Instructions to Run
1. Ensure you have Python 3.x installed on your machine.
2. Clone the repository using:
   ```bash
   git clone https://github.com/YourUsername/QuizProgram.git
Navigate to the project directory:
bash
Copy code
cd QuizProgram
Run the program:
bash
Copy code
python quiz_program.py
Follow the prompts in the console to input questions, take the quiz, and view results.
Project Structure
bash
Copy code
QuizProgram/
├── quiz_program.py  # Main source code file
├── README.md        # Documentation file
Future Enhancements
Add a graphical user interface (GUI).
Store questions and answers in a database or external file.
Allow exporting results to a file.
