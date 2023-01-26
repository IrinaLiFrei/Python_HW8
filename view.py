import model


def input_class():
    return input('С каким классом работаем? ').upper()


def input_subject():
    return input('Какой предмет? ').lower()

def who_answer():
    return input('Кто будет отвечать? ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_pupil(classbook: dict):
    for i, pupil in enumerate(classbook, 1):
        print(f'    {i}. {pupil:20} {classbook.get(pupil)}')