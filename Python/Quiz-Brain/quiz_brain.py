from data import question_data
import random


class QuizBrain:

    def __init__(self):
        self.current_score = 0
        self.question_number = 1

    def get_questions(self):
        for questions in question_data:
            question_text = questions["text"]
            answer_text = questions["answer"]
            user_input = input(f"{question_text} (True/False): ")
            if answer_text.lower() == user_input:
                self.current_score += 1
                print("You got it right!")
                print(f"The correct answer was: {answer_text}")
                print(f"Your current score is : {self.current_score}/{self.question_number}")
                self.question_number += 1
            elif answer_text.lower() != user_input:
                print("That's wrong.")
                print(f"The correct answer was: {answer_text}")
                print(f"Your current score is : {self.current_score}/{self.question_number}")
                self.question_number += 1
            else:
                print("Sorry wrong input.")

