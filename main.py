from urllib import request
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import requests
from html import unescape


question_banks = []
mode = -1
while(mode not in ["1", "2"]):
    mode = input(
        "1. Basic questions \n2. Question from Trivia DB\nI choose: ").strip().lower()

if(mode == "2"):
    number_of_questions = int(input("How many question do you want to challenge?: "))
    r = requests.get(
        f"https://opentdb.com/api.php?amount={number_of_questions}&type=boolean&category=18")
    banks = r.json()["results"]
    for question in banks:
        question_banks.append(
            Question(unescape(question["question"]), question["correct_answer"]))
else:
    for question in question_data:
        question_banks.append(Question(question["text"], question["answer"]))


quiz_brain = QuizBrain(question_banks)
while(not quiz_brain.out_of_question()):
    quiz_brain.next_question()
    print(
        f"Current Score is {quiz_brain.score}/{quiz_brain.question_number}\n")

print(
    f"The final Score is {quiz_brain.score} out of {quiz_brain.question_number} questions\n")
