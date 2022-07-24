from data import Data


# This class is for storing the questions and answers in the list.
class QuizBrian:

    def __init__(self):
        self.score = 0
        self.info = Data()

    # Method for storing the questions in a list.
    def get_questions(self):
        question_bank = []
        question = self.info.question_list()["results"]
        for i in range(10):
            question_bank.append(question[i]["question"])
        return question_bank

    # Method for storing the correct answers in a list.
    def answer(self):
        answer_bank = []
        correct_answer = self.info.question_list()["results"]
        for i in range(10):
            answer_bank.append(correct_answer[i]["correct_answer"])
        return answer_bank
