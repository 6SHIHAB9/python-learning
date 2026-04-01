class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        return False


    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"Q.{self.question_no}: {question.text} (True/False): ")
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Thats Wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_no}")
        print("\n")
    
    def final_message(self):
        print("You've completed the Quiz!")
        print(f"Your final score is {self.score}/{self.question_no}")
