classbook = {}
subject = ''
path = ''

def set_class (class_path: str):
    global path
    path = r'C:\Users\airin\Desktop\Studies\0. Workshop\Python\Python_HW8\\' + class_path + '.txt'


def set_subject(our_subject: str):
    global subject
    subject = our_subject

def open_file():
    with open(path, 'r', encoding ='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                classbook[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))

def save_file():
    new_file = []
    print(classbook)
    with open(path, 'r', encoding ='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in classbook.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding ='UTF-8') as data:
        data.write('\n'.join(new_file))
    
def student_mark(student: str, mark: int):
    marks = list(classbook.get(student))
    marks.append(mark)
    classbook[student] = marks

def get_classbook():
    return classbook
