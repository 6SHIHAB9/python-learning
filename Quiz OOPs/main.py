from question_model import Question
from data import question_data


question_bank = []

for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

print(question_bank)