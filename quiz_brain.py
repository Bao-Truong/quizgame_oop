from frozen import froze_it


@froze_it
class QuizBrain:
    def __init__(self, question_banks):
        self.question_number = 0
        self.question_list = question_banks
        self.score=0

    def next_question(self):
        if(not self.out_of_question()):
            question = f"Q.{self.question_number+1}: {self.question_list[self.question_number].text}"
            student_answer = input(question + " (True/False)?: ").lower()
            return self.check_answer(student_answer)
        else:
            print("End of the quest!")
            return False

    def out_of_question(self):
        return self.question_number >= len(self.question_list)

    def check_answer(self, student_answer):
        if(student_answer in ["t", "true"] and self.question_list[self.question_number].answer == "True") or (student_answer in ["f", "false"] and self.question_list[self.question_number].answer == "False"):
            self.question_number += 1
            self.score+=1
            print("Correct!🎁")
            return True
        else:
            self.question_number += 1
            print("Wrong!!🧨")
            return False
