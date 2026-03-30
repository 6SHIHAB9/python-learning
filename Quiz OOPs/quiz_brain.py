class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_no]
        answer = input(f"Q.{self.question_no}: {question.text} (True/False): ")