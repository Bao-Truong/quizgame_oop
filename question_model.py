from frozen import froze_it


@froze_it
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
    