from  question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for que in question_data: #iterate thru quedata
    myQ = Question(que["question"], que["correct_answer"]) # create object myQ from class Ques with parameters text and answer from the quedata
    question_bank.append(myQ) #add the objects to the bank

quiz = QuizBrain(question_bank)

while quiz.still_has_que():
     quiz.next_que()
print(f"You have Completed the quiz\n Your current score is :{quiz.score}/{quiz.question_number}")