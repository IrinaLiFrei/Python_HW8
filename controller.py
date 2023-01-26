import model
import view

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    student = ''
    while True:
        classbook = model.get_classbook()
        view.list_of_pupil(classbook)
        student = view.who_answer()
        if student == 'exit':
            break
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()

