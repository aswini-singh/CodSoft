import random

class QuizGame:
    def __init__(self, file_path):
        self.questions = []
        self.score = 0
        self.load_quiz_questions(file_path)

    def load_quiz_questions(self, file_path):
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
            i = 0
            while i < len(lines):
                question_line = lines[i]
                if question_line.endswith(''):
                    question = {"question": question_line, "options": [], "correct_answer": ""}
                    i += 1
                    while i < len(lines) and not lines[i].startswith("option: "):
                        question["options"].append(lines[i])
                        i += 1
                    if i < len(lines):
                        question["correct_answer"] = lines[i][8:]
                        i += 1
                    self.questions.append(question)
                else:
                    i += 1

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def ask_multiple_choice_question(self, question_data):
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=65):
            print(f"{chr(i)}. {option}")
        user_answer = input("Your answer (A, B, or C): ").strip().upper()
        if user_answer == question_data["correct_answer"]:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is {question_data['correct_answer']}.")
            return False

    def ask_fill_in_the_blank_question(self, question_data):
        user_answer = input(f"{question_data['question']}\nYour answer: ").strip().lower()
        if user_answer == question_data['correct_answer'].lower():
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is '{question_data['correct_answer']}'.")
            return False

    def start_quiz(self):
        self.shuffle_questions()
        print("Welcome to the Quiz Game!")
        print("Rules:")
        print("1. Answer multiple-choice questions with A, B, or C.")
        print("2. For fill-in-the-blank questions, with A, B, or C.")
        print("Let's begin!\n")

        for question_data in self.questions:
            question_type = "multiple_choice" if "options" in question_data else "fill_in_the_blank"           
            if question_type == "multiple_choice":
                self.score += self.ask_multiple_choice_question(question_data)
            else:
                self.score += self.ask_fill_in_the_blank_question(question_data)
        self.display_results()

    def display_results(self):
        print("\nQuiz completed!")
        print(f"Your score is {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Congratulations! You answered all questions.")
        elif self.score >= len(self.questions) / 2:
            print("Good job! You did well.")
        else:
            print("Keep practicing. You can do better next time.")

if __name__ == "__main__":
    game = QuizGame("Quiz_Game/questions.txt")
    game.start_quiz()
