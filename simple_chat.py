class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    def ask_question(self, sameone, question):
        print(f'{sameone.name}, {question}')
        sameone.answer_question(question)
        print()


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, все будет хорошо,'
                  ' хочешь покажу тебе смешное видео! :)')
        else:
            super().answer_question(question)


class CodReviewer(Human):
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print(f'{student.name}, среди ошибок кода не обнаружено,'
                  ' еще раз повтори предыдущие уроки и попробуй заново,'
                  ' тогда все плучится!')
        elif question == 'я два раза исправил, но все равно не работает,' \
                         ' что делать?':
            print('Я могу подсказать направление, но делать за тебя не буду,'
                  ' ты должен научиться сам находить решение '
                  'задачю')
        else:
            super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print(f'{student.name}, немного отдохни и возвращайся с вопросами '
                  'по теории :)')
        elif question == 'как мне устроиться питонистом?':
            print('Cейчас расскажу.')
        elif question == 'давай сходим на свидание?':
            print(f'{student.name}, когда все выучишь, обязательно сходим ;)')
        else:
            super().answer_question(question)


if __name__ == '__main__':
    student = Student('Иван')
    friend = Human('Антон')
    curator = Curator('Марина')
    reviewer = CodReviewer('Андрей')
    mentor = Mentor('Даша')
    student.ask_question(friend, 'как устроиться питонистом?')
    student.ask_question(mentor, 'как мне устроиться питонистом?')
    student.ask_question(curator, 'мне грустненько, что делать?')
    student.ask_question(reviewer, 'что не так с моим проектом?')
    student.ask_question(mentor, 'мне грустненько, что делать?')
    student.ask_question(curator, 'где я допусли ошибку в коде?')
    student.ask_question(reviewer, 'я два раза исправил, но все равно не'
                                   ' работает, что делать?')
    student.ask_question(reviewer, 'что же мне делать?')
    student.ask_question(mentor, 'что же мне делать?')
    student.ask_question(mentor, 'давай сходим на свидание?')
