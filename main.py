from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random

question_banks = []
for question in question_data:
    question_banks.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_banks)
while(not quiz_brain.out_of_question()):
    quiz_brain.next_question()
    print(f"Current Score is {quiz_brain.score}/{quiz_brain.question_number}\n")    

print(f"The final Score is {quiz_brain.score} out of {quiz_brain.question_number} questions\n")
