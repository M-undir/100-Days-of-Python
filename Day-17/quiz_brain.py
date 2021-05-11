class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}:{current_question.text}. (True/False)?: ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, your_answer, correct_answer):
        if your_answer == correct_answer:
            self.score += 1
            print("That is... correct!")
        else:
            print("That is... incorrect.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()