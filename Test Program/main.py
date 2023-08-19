import random
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QTableWidgetItem

def exitfunction():
    with open("test1.txt",mode = "w",  encoding="utf-8") as test1:
        test1.write('max_tries:\n')
        test1.write(max_tries)
        test1.write("\n")
        test1.write("\n")
        test1.write('name:\n')
        test1.write(test_name)
        test1.write("\n")
        test1.write("\n")
        test1.write('total_number_of_questions:\n')
        test1.write(str(total_number_of_questions))
        test1.write("\n")
        test1.write("\n")
        test1.write('number_of_questions:\n')
        test1.write(str(number_of_questions))
        test1.write("\n")
        test1.write("\n")
        for i in range(int(total_number_of_questions)):
            test1.write('type:\n')
            test1.write(questions_type[i])
            test1.write("\n")
            test1.write('question:\n')
            test1.write(questions_and_answers_text[i][0])
            test1.write("\n")
            if questions_type[i][1] == "2":
                test1.write('answers:\n')
                test1.write(questions_and_answers_text[i][1])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][2])
                test1.write("\n")
            if questions_type[i][1] == "3":
                test1.write('answers:\n')
                test1.write(questions_and_answers_text[i][1])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][2])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][3])
                test1.write("\n")
            if questions_type[i][1] == "4":
                test1.write('answers:\n')
                test1.write(questions_and_answers_text[i][1])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][2])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][3])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][4])
                test1.write("\n")
            if questions_type[i][1] == "5":
                test1.write('answers:\n')
                test1.write(questions_and_answers_text[i][1])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][2])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][3])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][4])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][5])
                test1.write("\n")
            if questions_type[i][1] == "6":
                test1.write('answers:\n')
                test1.write(questions_and_answers_text[i][1])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][2])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][3])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][4])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][5])
                test1.write("\n")
                test1.write(questions_and_answers_text[i][6])
                test1.write("\n")
            if questions_type[i][0] == "1":
                test1.write('correct:\n')
                test1.write(str(correct_answers[i][0]))
                test1.write("\n")
                test1.write("\n")
            if questions_type[i][0] == "2":
                test1.write('correct:\n')
                test1.write(str(correct_answers[i][0]))
                test1.write("\n")
                test1.write("\n")
    with open("Users1.txt",mode = "w",  encoding="utf-8") as Users1:
        for i in range(len(users_login)):
            Users1.write('login:\n')
            Users1.write(users_login[i])
            Users1.write("\n")
            Users1.write('password:\n')
            Users1.write(users_password[i])
            Users1.write("\n")
            Users1.write('level:\n')
            Users1.write(users_level[i])
            Users1.write("\n")
            Users1.write('best_test_result:\n')
            Users1.write(users_best_test_result[i])
            Users1.write("\n")
            Users1.write('tries:\n')
            Users1.write(tries[i])
            Users1.write("\n")
            Users1.write("\n")
    app.quit()

class MenuWindow(QDialog):
    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi("Start.ui", self)
        self.startButton.clicked.connect(self.start_login)
        self.exitButton.clicked.connect(exitfunction)

    def start_login(self):
        LoginMenuWindow = LoginMenu()
        all_widgets['LoginMenuwidget'] = LoginMenuWindow
        widget.addWidget(all_widgets['LoginMenuwidget'])
        widget.setCurrentWidget(all_widgets['LoginMenuwidget'])

class LoginMenu(QDialog):
    def __init__(self):
        super(LoginMenu, self).__init__()
        loadUi("Login.ui", self)
        self.login.setPlaceholderText("Введите логин")
        self.password.setPlaceholderText("Введите пароль")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.startButton.clicked.connect(self.start_login)
        self.error.setVisible(False)

    def start_login(self):
        global login_try
        global current_user
        user_login = self.login.text()
        user_password = self.password.text()
        global users_login
        global users_password
        if user_login in users_login and user_password in users_password:
            for i in range(len(users_login)):
                if (user_login == users_login[i]) and (user_password == users_password[i]):
                    if users_level[i] == '2':
                        AdminMenuWindow = AdminMenu()
                        all_widgets['AdminMenuwidget'] = AdminMenuWindow
                        widget.addWidget(all_widgets['AdminMenuwidget'])
                        widget.setCurrentWidget(all_widgets['AdminMenuwidget'])
                        current_user = i
                    if users_level[i] == '1':
                        TeacherMenuWindow = TeacherMenu()
                        all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
                        widget.addWidget(all_widgets['TeacherMenuwidget'])
                        widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
                        current_user = i
                    if users_level[i] == '0':
                        current_user = i
                        if int(tries[current_user]) > 0:
                            UserMenuWindow = UserMenu()
                            all_widgets['UserMenuwidget'] = UserMenuWindow
                            widget.addWidget(all_widgets['UserMenuwidget'])
                            widget.setCurrentWidget(all_widgets['UserMenuwidget'])
                        else:
                            endfunction()
                else:
                    self.error.setVisible(True)
        else:
            self.error.setVisible(True)

class UserMenu(QDialog):
    def __init__(self):
        global current_question
        global questions_type
        super(UserMenu, self).__init__()
        loadUi("UserMenu.ui", self)
        self.label.setText(test_name)
        if questions_type[questions_list[current_question]] == "12":
            self.startButton.clicked.connect(self.start12function)
        if questions_type[questions_list[current_question]] == "22":
            self.startButton.clicked.connect(self.start22function)
        if questions_type[questions_list[current_question]] == "13":
            self.startButton.clicked.connect(self.start13function)
        if questions_type[questions_list[current_question]] == "23":
            self.startButton.clicked.connect(self.start23function)
        if questions_type[questions_list[current_question]] == "14":
            self.startButton.clicked.connect(self.start14function)
        if questions_type[questions_list[current_question]] == "24":
            self.startButton.clicked.connect(self.start24function)
        if questions_type[questions_list[current_question]] == "15":
            self.startButton.clicked.connect(self.start15function)
        if questions_type[questions_list[current_question]] == "25":
            self.startButton.clicked.connect(self.start25function)
        if questions_type[questions_list[current_question]] == "16":
            self.startButton.clicked.connect(self.start16function)
        if questions_type[questions_list[current_question]] == "26":
            self.startButton.clicked.connect(self.start26function)
        self.exitButton.clicked.connect(exitfunction)

    def start12function(self):
        global current_question
        question12Window = question12()
        all_widgets['question12widget'] = question12Window
        widget.addWidget(all_widgets['question12widget'])
        widget.setCurrentWidget(all_widgets['question12widget'])

    def start22function(self):
        global current_question
        question22Window = question22()
        all_widgets['question22widget'] = question22Window
        widget.addWidget(all_widgets['question22widget'])
        widget.setCurrentWidget(all_widgets['question22widget'])

    def start13function(self):
        global current_question
        question13Window = question13()
        all_widgets['question13widget'] = question13Window
        widget.addWidget(all_widgets['question13widget'])
        widget.setCurrentWidget(all_widgets['question13widget'])

    def start23function(self):
        global current_question
        question23Window = question23()
        all_widgets['question23widget'] = question23Window
        widget.addWidget(all_widgets['question23widget'])
        widget.setCurrentWidget(all_widgets['question23widget'])

    def start14function(self):
        global current_question
        question14Window = question14()
        all_widgets['question14widget'] = question14Window
        widget.addWidget(all_widgets['question14widget'])
        widget.setCurrentWidget(all_widgets['question14widget'])

    def start24function(self):
        global current_question
        question24Window = question24()
        all_widgets['question24widget'] = question24Window
        widget.addWidget(all_widgets['question24widget'])
        widget.setCurrentWidget(all_widgets['question24widget'])

    def start15function(self):
        global current_question
        question15Window = question15()
        all_widgets['question15widget'] = question15Window
        widget.addWidget(all_widgets['question15widget'])
        widget.setCurrentWidget(all_widgets['question15widget'])

    def start25function(self):
        global current_question
        question25Window = question25()
        all_widgets['question25widget'] = question25Window
        widget.addWidget(all_widgets['question25widget'])
        widget.setCurrentWidget(all_widgets['question25widget'])

    def start16function(self):
        global current_question
        question16Window = question16()
        all_widgets['question16widget'] = question16Window
        widget.addWidget(all_widgets['question16widget'])
        widget.setCurrentWidget(all_widgets['question16widget'])

    def start26function(self):
        global current_question
        question26Window = question26()
        all_widgets['question26widget'] = question26Window
        widget.addWidget(all_widgets['question26widget'])
        widget.setCurrentWidget(all_widgets['question26widget'])

class AdminMenu(QDialog):
    def __init__(self):
        global current_question
        global questions_type
        super(AdminMenu, self).__init__()
        loadUi("AdminMenu.ui", self)
        self.createuser.clicked.connect(self.createuserfunction)
        self.createteacher.clicked.connect(self.createteacherfunction)
        self.exitButton.clicked.connect(exitfunction)

    def createuserfunction(self):
        CreateUserWindow = CreateUser()
        all_widgets['CreateUserwidget'] = CreateUserWindow
        widget.addWidget(all_widgets['CreateUserwidget'])
        widget.setCurrentWidget(all_widgets['CreateUserwidget'])

    def createteacherfunction(self):
        CreateTeacherWindow = CreateTeacher()
        all_widgets['CreateTeacherwidget'] = CreateTeacherWindow
        widget.addWidget(all_widgets['CreateTeacherwidget'])
        widget.setCurrentWidget(all_widgets['CreateTeacherwidget'])

class CreateUser(QDialog):
    def __init__(self):
        super(CreateUser, self).__init__()
        loadUi("CreateUser.ui", self)
        self.login.setPlaceholderText("Введите логин")
        self.password.setPlaceholderText("Введите пароль")
        self.startButton.clicked.connect(self.createuser)
        self.error.setVisible(False)

    def createuser(self):
        user_login = self.login.text()
        user_password = self.password.text()
        global users_login
        global users_password
        global users_level
        global users_best_test_result
        global tries
        if user_login not in users_login:
            users_password.append(user_password)
            users_login.append(user_login)
            tries.append(max_tries)
            users_best_test_result.append('-1')
            users_level.append('0')
            AdminMenuWindow = AdminMenu()
            all_widgets['AdminMenuwidget'] = AdminMenuWindow
            widget.addWidget(all_widgets['AdminMenuwidget'])
            widget.setCurrentWidget(all_widgets['AdminMenuwidget'])
        else:
            self.error.setVisible(True)

class CreateTeacher(QDialog):
    def __init__(self):
        super(CreateTeacher, self).__init__()
        loadUi("CreateTeacher.ui", self)
        self.login.setPlaceholderText("Введите логин")
        self.password.setPlaceholderText("Введите пароль")
        self.startButton.clicked.connect(self.createteacher)
        self.error.setVisible(False)

    def createteacher(self):
        user_login = self.login.text()
        user_password = self.password.text()
        global users_login
        global users_password
        global users_level
        global users_best_test_result
        global tries
        if user_login not in users_login:
            users_password.append(user_password)
            users_login.append(user_login)
            tries.append(max_tries)
            users_best_test_result.append('-1')
            users_level.append('1')
            AdminMenuWindow = AdminMenu()
            all_widgets['AdminMenuwidget'] = AdminMenuWindow
            widget.addWidget(all_widgets['AdminMenuwidget'])
            widget.setCurrentWidget(all_widgets['AdminMenuwidget'])
        else:
            self.error.setVisible(True)

class TeacherMenu(QDialog):
    def __init__(self):
        global current_question
        global questions_type
        super(TeacherMenu, self).__init__()
        loadUi("TeacherMenu.ui", self)
        self.TestResults.clicked.connect(self.TestResultsfunction)
        self.CreateTest.clicked.connect(self.CreateTestfunction)
        self.AddQuestion.clicked.connect(self.AddQuestionfunction)
        self.exitButton.clicked.connect(exitfunction)

    def TestResultsfunction(self):
        TestResultsWindow = TestResults()
        all_widgets['TestResultswidget'] = TestResultsWindow
        widget.addWidget(all_widgets['TestResultswidget'])
        widget.setCurrentWidget(all_widgets['TestResultswidget'])

    def CreateTestfunction(self):
        CreateTestWindow = CreateTest()
        all_widgets['CreateTestwidget'] = CreateTestWindow
        widget.addWidget(all_widgets['CreateTestwidget'])
        widget.setCurrentWidget(all_widgets['CreateTestwidget'])

    def AddQuestionfunction(self):
        global amount_of_new_questions
        global new_question_and_answers
        amount_of_new_questions = 1
        new_question_and_answers = []
        AddQuestionWindow = AddQuestion()
        all_widgets['AddQuestionwidget'] = AddQuestionWindow
        widget.addWidget(all_widgets['AddQuestionwidget'])
        widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

class TestResults(QDialog):
    def __init__(self):
        super(TestResults, self).__init__()
        loadUi("TestResults.ui", self)
        counter = 0
        for i in range(len(users_login)):
            if users_level[i] == '0':
                counter = counter + 1
        self.Results.setRowCount(counter)
        self.Results.setColumnCount(3)
        self.Results.setHorizontalHeaderLabels(["Логин", "Лучший результат", "Осталось попыток"])
        counter = 0
        for i in range(len(users_login)):
            if users_level[i] == '0':
                self.Results.setItem(counter, 0, QTableWidgetItem(users_login[i]))
                self.Results.setItem(counter, 1, QTableWidgetItem(users_best_test_result[i]))
                self.Results.setItem(counter, 2, QTableWidgetItem(tries[i]))
                counter = counter + 1
        self.behindButton.clicked.connect(self.behind)
        self.exitButton.clicked.connect(exitfunction)

    def behind(self):
        TeacherMenuWindow = TeacherMenu()
        all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
        widget.addWidget(all_widgets['TeacherMenuwidget'])
        widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])

class CreateTest(QDialog):
    def __init__(self):
        super(CreateTest, self).__init__()
        loadUi("CreateTest.ui", self)
        self.name.setPlaceholderText("Введите название теста")
        self.nextButton.clicked.connect(self.nextstep)


    def nextstep(self):
        global amount_of_new_questions
        global correct_answers
        global questions_and_answers_text
        global questions_type
        global number_of_questions
        global total_number_of_questions
        global max_tries
        global test_name
        global new_test
        questions_and_answers_text.clear()
        questions_type.clear()
        correct_answers.clear()
        test_name = self.name.text()
        amount_of_new_questions = self.total.value()
        total_number_of_questions = self.total.value()
        max_tries = self.tries.text()
        number_of_questions = self.use.value()
        new_test = False
        for i in range(len(users_login)):
            users_best_test_result[i] = '-1'
            tries[i] = str(max_tries)

        AddQuestionWindow = AddQuestion()
        all_widgets['AddQuestionwidget'] = AddQuestionWindow
        widget.addWidget(all_widgets['AddQuestionwidget'])
        widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

class AddQuestion(QDialog):
    def __init__(self):
        super(AddQuestion, self).__init__()
        loadUi("AddQuestion.ui", self)
        global qtype
        qtype = ''
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.nextButton.clicked.connect(self.nextstep)
        self.label_3.setVisible(False)

    def btnfunction(self, num):
        global qtype
        if num == 1:
            qtype = qtype + '1'
        if num == 2:
            qtype = qtype + '2'

    def nextstep(self):
        global questions_type
        global qtype
        qtype = qtype + self.spinBox.text()
        if len(qtype) != 2:
            self.label_3.setVisible(True)
            qtype = ''
        else:
            if qtype == "12":
                addquestion12Window = addquestion12()
                all_widgets['addquestion12widget'] = addquestion12Window
                widget.addWidget(all_widgets['addquestion12widget'])
                widget.setCurrentWidget(all_widgets['addquestion12widget'])
            if qtype == "22":
                addquestion22Window = addquestion22()
                all_widgets['addquestion22widget'] = addquestion22Window
                widget.addWidget(all_widgets['addquestion22widget'])
                widget.setCurrentWidget(all_widgets['addquestion22widget'])
            if qtype == "13":
                addquestion13Window = addquestion13()
                all_widgets['addquestion13widget'] = addquestion13Window
                widget.addWidget(all_widgets['addquestion13widget'])
                widget.setCurrentWidget(all_widgets['addquestion13widget'])
            if qtype == "23":
                addquestion23Window = addquestion23()
                all_widgets['addquestion23widget'] = addquestion23Window
                widget.addWidget(all_widgets['addquestion23widget'])
                widget.setCurrentWidget(all_widgets['addquestion23widget'])
            if qtype == "14":
                addquestion14Window = addquestion14()
                all_widgets['addquestion14widget'] = addquestion14Window
                widget.addWidget(all_widgets['addquestion14widget'])
                widget.setCurrentWidget(all_widgets['addquestion14widget'])
            if qtype == "24":
                addquestion24Window = addquestion24()
                all_widgets['addquestion24widget'] = addquestion24Window
                widget.addWidget(all_widgets['addquestion24widget'])
                widget.setCurrentWidget(all_widgets['addquestion24widget'])
            if qtype == "15":
                addquestion15Window = addquestion15()
                all_widgets['addquestion15widget'] = addquestion15Window
                widget.addWidget(all_widgets['addquestion15widget'])
                widget.setCurrentWidget(all_widgets['addquestion15widget'])
            if qtype == "25":
                addquestion25Window = addquestion25()
                all_widgets['addquestion25widget'] = addquestion25Window
                widget.addWidget(all_widgets['addquestion25widget'])
                widget.setCurrentWidget(all_widgets['addquestion25widget'])
            if qtype == "16":
                addquestion16Window = addquestion16()
                all_widgets['addquestion16widget'] = addquestion16Window
                widget.addWidget(all_widgets['addquestion16widget'])
                widget.setCurrentWidget(all_widgets['addquestion16widget'])
            if qtype == "26":
                addquestion26Window = addquestion26()
                all_widgets['addquestion26widget'] = addquestion26Window
                widget.addWidget(all_widgets['addquestion26widget'])
                widget.setCurrentWidget(all_widgets['addquestion26widget'])

class addquestion12(QDialog):
    def __init__(self):
        super(addquestion12, self).__init__()
        loadUi("addquestion12.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def btnfunction(self, num):
        global new_correct
        if num == 1:
            new_correct.append(1)
        if num == 2:
            new_correct.append(2)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        correct_answers.append(new_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

class addquestion22(QDialog):
    def __init__(self):
        super(addquestion22, self).__init__()
        loadUi("addquestion22.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        res_correct = []
        res_correct.append(str(new_correct2[0][0]) + str(new_correct2[0][1]))
        correct_answers.append(res_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

    def btnfunction(self, num):
        global new_correct2
        if num == 1 and new_correct2[0][0] == 0:
            new_correct2[0][0] = 1
        elif num == 1 and new_correct2[0][0] == 1:
            new_correct2[0][0] = 0
        if num == 2 and new_correct2[0][1] == 0:
            new_correct2[0][1] = 1
        elif num == 2 and new_correct2[0][1] == 1:
            new_correct2[0][1] = 0

class addquestion13(QDialog):
    def __init__(self):
        super(addquestion13, self).__init__()
        loadUi("addquestion13.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def btnfunction(self, num):
        global new_correct
        if num == 1:
            new_correct.append(1)
        if num == 2:
            new_correct.append(2)
        if num == 3:
            new_correct.append(3)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        correct_answers.append(new_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

class addquestion23(QDialog):
    def __init__(self):
        super(addquestion23, self).__init__()
        loadUi("addquestion23.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        res_correct = []
        res_correct.append(str(new_correct2[0][0]) + str(new_correct2[0][1]) + str(new_correct2[0][2]))
        correct_answers.append(res_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

    def btnfunction(self, num):
        global new_correct2
        if num == 1 and new_correct2[0][0] == 0:
            new_correct2[0][0] = 1
        elif num == 1 and new_correct2[0][0] == 1:
            new_correct2[0][0] = 0
        if num == 2 and new_correct2[0][1] == 0:
            new_correct2[0][1] = 1
        elif num == 2 and new_correct2[0][1] == 1:
            new_correct2[0][1] = 0
        if num == 3 and new_correct2[0][2] == 0:
            new_correct2[0][2] = 1
        elif num == 3 and new_correct2[0][2] == 1:
            new_correct2[0][2] = 0

class addquestion14(QDialog):
    def __init__(self):
        super(addquestion14, self).__init__()
        loadUi("addquestion14.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.answer4.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def btnfunction(self, num):
        global new_correct
        if num == 1:
            new_correct.append(1)
        if num == 2:
            new_correct.append(2)
        if num == 3:
            new_correct.append(3)
        if num == 4:
            new_correct.append(4)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        new_question_and_answers.append(str(self.answer4.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        correct_answers.append(new_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

class addquestion24(QDialog):
    def __init__(self):
        super(addquestion24, self).__init__()
        loadUi("addquestion24.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.answer4.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        new_question_and_answers.append(str(self.answer4.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        res_correct = []
        res_correct.append(str(new_correct2[0][0]) + str(new_correct2[0][1]) + str(new_correct2[0][2]) + str(new_correct2[0][3]))
        correct_answers.append(res_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

    def btnfunction(self, num):
        global new_correct2
        if num == 1 and new_correct2[0][0] == 0:
            new_correct2[0][0] = 1
        elif num == 1 and new_correct2[0][0] == 1:
            new_correct2[0][0] = 0
        if num == 2 and new_correct2[0][1] == 0:
            new_correct2[0][1] = 1
        elif num == 2 and new_correct2[0][1] == 1:
            new_correct2[0][1] = 0
        if num == 3 and new_correct2[0][2] == 0:
            new_correct2[0][2] = 1
        elif num == 3 and new_correct2[0][2] == 1:
            new_correct2[0][2] = 0
        if num == 4 and new_correct2[0][3] == 0:
            new_correct2[0][3] = 1
        elif num == 4 and new_correct2[0][3] == 1:
            new_correct2[0][3] = 0

class addquestion15(QDialog):
    def __init__(self):
        super(addquestion15, self).__init__()
        loadUi("addquestion15.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.answer4.setPlaceholderText("Введите ответ")
        self.answer5.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def btnfunction(self, num):
        global new_correct
        if num == 1:
            new_correct.append(1)
        if num == 2:
            new_correct.append(2)
        if num == 3:
            new_correct.append(3)
        if num == 4:
            new_correct.append(4)
        if num == 5:
            new_correct.append(5)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        new_question_and_answers.append(str(self.answer4.text()))
        new_question_and_answers.append(str(self.answer5.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        correct_answers.append(new_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

class addquestion25(QDialog):
    def __init__(self):
        super(addquestion25, self).__init__()
        loadUi("addquestion25.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.answer4.setPlaceholderText("Введите ответ")
        self.answer5.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        new_question_and_answers.append(str(self.answer4.text()))
        new_question_and_answers.append(str(self.answer5.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        res_correct = []
        res_correct.append(
        str(new_correct2[0][0]) + str(new_correct2[0][1]) + str(new_correct2[0][2]) + str(new_correct2[0][3]) + str(new_correct2[0][4]))
        correct_answers.append(res_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

    def btnfunction(self, num):
        global new_correct2
        if num == 1 and new_correct2[0][0] == 0:
            new_correct2[0][0] = 1
        elif num == 1 and new_correct2[0][0] == 1:
            new_correct2[0][0] = 0
        if num == 2 and new_correct2[0][1] == 0:
            new_correct2[0][1] = 1
        elif num == 2 and new_correct2[0][1] == 1:
            new_correct2[0][1] = 0
        if num == 3 and new_correct2[0][2] == 0:
            new_correct2[0][2] = 1
        elif num == 3 and new_correct2[0][2] == 1:
            new_correct2[0][2] = 0
        if num == 4 and new_correct2[0][3] == 0:
            new_correct2[0][3] = 1
        elif num == 4 and new_correct2[0][3] == 1:
            new_correct2[0][3] = 0
        if num == 5 and new_correct2[0][4] == 0:
            new_correct2[0][4] = 1
        elif num == 5 and new_correct2[0][4] == 1:
            new_correct2[0][4] = 0

class addquestion16(QDialog):
    def __init__(self):
        super(addquestion16, self).__init__()
        loadUi("addquestion16.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.answer4.setPlaceholderText("Введите ответ")
        self.answer5.setPlaceholderText("Введите ответ")
        self.answer6.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.btn6.clicked.connect(lambda checked, num=6: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def btnfunction(self, num):
        global new_correct
        if num == 1:
            new_correct.append(1)
        if num == 2:
            new_correct.append(2)
        if num == 3:
            new_correct.append(3)
        if num == 4:
            new_correct.append(4)
        if num == 5:
            new_correct.append(5)
        if num == 6:
            new_correct.append(6)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        new_question_and_answers.append(str(self.answer4.text()))
        new_question_and_answers.append(str(self.answer5.text()))
        new_question_and_answers.append(str(self.answer6.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        correct_answers.append(new_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

class addquestion26(QDialog):
    def __init__(self):
        super(addquestion26, self).__init__()
        loadUi("addquestion26.ui", self)
        global new_question_and_answers
        global new_correct
        global new_correct2
        new_question_and_answers = []
        new_correct = []
        new_correct2 = [[0 for j in range(6)] for i in range(1)]
        self.question.setPlaceholderText("Введите вопрос")
        self.answer1.setPlaceholderText("Введите ответ")
        self.answer2.setPlaceholderText("Введите ответ")
        self.answer3.setPlaceholderText("Введите ответ")
        self.answer4.setPlaceholderText("Введите ответ")
        self.answer5.setPlaceholderText("Введите ответ")
        self.answer6.setPlaceholderText("Введите ответ")
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.btn6.clicked.connect(lambda checked, num=6: self.btnfunction(num))
        self.nextButton.clicked.connect(self.next)

    def next(self):
        global amount_of_new_questions
        global new_question_and_answers
        global total_number_of_questions
        global qtype
        global questions_type
        amount_of_new_questions = amount_of_new_questions - 1
        new_question_and_answers.append(str(self.question.text()))
        new_question_and_answers.append(str(self.answer1.text()))
        new_question_and_answers.append(str(self.answer2.text()))
        new_question_and_answers.append(str(self.answer3.text()))
        new_question_and_answers.append(str(self.answer4.text()))
        new_question_and_answers.append(str(self.answer5.text()))
        new_question_and_answers.append(str(self.answer6.text()))
        if new_test:
            total_number_of_questions = total_number_of_questions + 1
        res_correct = []
        res_correct.append(
            str(new_correct2[0][0]) + str(new_correct2[0][1]) + str(new_correct2[0][2]) + str(new_correct2[0][3]) + str(
                new_correct2[0][4]) + str(new_correct2[0][5]))
        correct_answers.append(res_correct)
        questions_and_answers_text.append(new_question_and_answers)
        questions_type.append(qtype)
        if amount_of_new_questions == 0:
            TeacherMenuWindow = TeacherMenu()
            all_widgets['TeacherMenuwidget'] = TeacherMenuWindow
            widget.addWidget(all_widgets['TeacherMenuwidget'])
            widget.setCurrentWidget(all_widgets['TeacherMenuwidget'])
        else:
            AddQuestionWindow = AddQuestion()
            all_widgets['AddQuestionwidget'] = AddQuestionWindow
            widget.addWidget(all_widgets['AddQuestionwidget'])
            widget.setCurrentWidget(all_widgets['AddQuestionwidget'])

    def btnfunction(self, num):
        global new_correct2
        if num == 1 and new_correct2[0][0] == 0:
            new_correct2[0][0] = 1
        elif num == 1 and new_correct2[0][0] == 1:
            new_correct2[0][0] = 0
        if num == 2 and new_correct2[0][1] == 0:
            new_correct2[0][1] = 1
        elif num == 2 and new_correct2[0][1] == 1:
            new_correct2[0][1] = 0
        if num == 3 and new_correct2[0][2] == 0:
            new_correct2[0][2] = 1
        elif num == 3 and new_correct2[0][2] == 1:
            new_correct2[0][2] = 0
        if num == 4 and new_correct2[0][3] == 0:
            new_correct2[0][3] = 1
        elif num == 4 and new_correct2[0][3] == 1:
            new_correct2[0][3] = 0
        if num == 5 and new_correct2[0][4] == 0:
            new_correct2[0][4] = 1
        elif num == 5 and new_correct2[0][4] == 1:
            new_correct2[0][4] = 0
        if num == 6 and new_correct2[0][5] == 0:
            new_correct2[0][5] = 1
        elif num == 6 and new_correct2[0][5] == 1:
            new_correct2[0][5] = 0

def endfunction():
    congratulationWindow = Congratulation()
    all_widgets['congratulationwidget'] = congratulationWindow
    widget.addWidget(all_widgets['congratulationwidget'])
    widget.setCurrentWidget(all_widgets['congratulationwidget'])

def nextfunction12():
    global current_question
    current_question = current_question + 1
    question12Window = question12()
    all_widgets['question12widget'] = question12Window
    widget.addWidget(all_widgets['question12widget'])
    widget.setCurrentWidget(all_widgets['question12widget'])

def nextfunction22():
    global current_question
    current_question = current_question + 1
    question22Window = question22()
    all_widgets['question22widget'] = question22Window
    widget.addWidget(all_widgets['question22widget'])
    widget.setCurrentWidget(all_widgets['question22widget'])

def nextfunction13():
    global current_question
    current_question = current_question + 1
    question13Window = question13()
    all_widgets['question13widget'] = question13Window
    widget.addWidget(all_widgets['question13widget'])
    widget.setCurrentWidget(all_widgets['question13widget'])

def nextfunction23():
    global current_question
    current_question = current_question + 1
    question23Window = question23()
    all_widgets['question23widget'] = question23Window
    widget.addWidget(all_widgets['question23widget'])
    widget.setCurrentWidget(all_widgets['question23widget'])

def nextfunction14():
    global current_question
    current_question = current_question + 1
    question14Window = question14()
    all_widgets['question14widget'] = question14Window
    widget.addWidget(all_widgets['question14widget'])
    widget.setCurrentWidget(all_widgets['question14widget'])

def nextfunction24():
    global current_question
    current_question = current_question + 1
    question24Window = question24()
    all_widgets['question24widget'] = question24Window
    widget.addWidget(all_widgets['question24widget'])
    widget.setCurrentWidget(all_widgets['question24widget'])

def nextfunction15():
    global current_question
    current_question = current_question + 1
    question15Window = question15()
    all_widgets['question15widget'] = question15Window
    widget.addWidget(all_widgets['question15widget'])
    widget.setCurrentWidget(all_widgets['question15widget'])

def nextfunction25():
    global current_question
    current_question = current_question + 1
    question25Window = question25()
    all_widgets['question25widget'] = question25Window
    widget.addWidget(all_widgets['question25widget'])
    widget.setCurrentWidget(all_widgets['question25widget'])

def nextfunction16():
    global current_question
    current_question = current_question + 1
    question16Window = question16()
    all_widgets['question16widget'] = question16Window
    widget.addWidget(all_widgets['question16widget'])
    widget.setCurrentWidget(all_widgets['question16widget'])

def nextfunction26():
    global current_question
    current_question = current_question + 1
    question26Window = question26()
    all_widgets['question26widget'] = question26Window
    widget.addWidget(all_widgets['question26widget'])
    widget.setCurrentWidget(all_widgets['question26widget'])


def behindfunction12():
    global current_question
    current_question = current_question - 1
    question12Window = question12()
    all_widgets['question12widget'] = question12Window
    widget.addWidget(all_widgets['question12widget'])
    widget.setCurrentWidget(all_widgets['question12widget'])

def behindfunction22():
    global current_question
    current_question = current_question - 1
    question22Window = question22()
    all_widgets['question22widget'] = question22Window
    widget.addWidget(all_widgets['question22widget'])
    widget.setCurrentWidget(all_widgets['question22widget'])

def behindfunction13():
    global current_question
    current_question = current_question - 1
    question13Window = question13()
    all_widgets['question13widget'] = question13Window
    widget.addWidget(all_widgets['question13widget'])
    widget.setCurrentWidget(all_widgets['question13widget'])

def behindfunction23():
    global current_question
    current_question = current_question - 1
    question23Window = question23()
    all_widgets['question23widget'] = question23Window
    widget.addWidget(all_widgets['question23widget'])
    widget.setCurrentWidget(all_widgets['question23widget'])

def behindfunction14():
    global current_question
    current_question = current_question - 1
    question14Window = question14()
    all_widgets['question14widget'] = question14Window
    widget.addWidget(all_widgets['question14widget'])
    widget.setCurrentWidget(all_widgets['question14widget'])

def behindfunction24():
    global current_question
    current_question = current_question - 1
    question24Window = question24()
    all_widgets['question24widget'] = question24Window
    widget.addWidget(all_widgets['question24widget'])
    widget.setCurrentWidget(all_widgets['question24widget'])

def behindfunction15():
    global current_question
    current_question = current_question - 1
    question15Window = question15()
    all_widgets['question15widget'] = question15Window
    widget.addWidget(all_widgets['question15widget'])
    widget.setCurrentWidget(all_widgets['question15widget'])

def behindfunction25():
    global current_question
    current_question = current_question - 1
    question25Window = question25()
    all_widgets['question25widget'] = question25Window
    widget.addWidget(all_widgets['question25widget'])
    widget.setCurrentWidget(all_widgets['question25widget'])

def behindfunction16():
    global current_question
    current_question = current_question - 1
    question16Window = question16()
    all_widgets['question16widget'] = question16Window
    widget.addWidget(all_widgets['question16widget'])
    widget.setCurrentWidget(all_widgets['question16widget'])

def behindfunction26():
    global current_question
    current_question = current_question - 1
    question26Window = question26()
    all_widgets['question26widget'] = question26Window
    widget.addWidget(all_widgets['question26widget'])
    widget.setCurrentWidget(all_widgets['question26widget'])


class question12(QDialog):
    def __init__(self):
        super(question12, self).__init__()
        loadUi("question12.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        if user_answers[current_question][0] == 1:
            self.btn1.setChecked(1)
        if user_answers[current_question][0] == 2:
            self.btn2.setChecked(1)
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2

class question22(QDialog):
    def __init__(self):
        super(question22, self).__init__()
        loadUi("question22.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        if user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and user_answers[current_question][0] == 0:
            user_answers[current_question][0] = 1
        elif num == 1 and user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if num == 2 and user_answers[current_question][1] == 0:
            user_answers[current_question][1] = 1
        elif num == 2 and user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0

class question13(QDialog):
    def __init__(self):
        super(question13, self).__init__()
        loadUi("question13.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        if user_answers[current_question][0] == 1:
            self.btn1.setChecked(1)
        if user_answers[current_question][0] == 2:
            self.btn2.setChecked(1)
        if user_answers[current_question][0] == 3:
            self.btn3.setChecked(1)
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3

class question23(QDialog):
    def __init__(self):
        super(question23, self).__init__()
        loadUi("question23.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        if user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and user_answers[current_question][0] == 0:
            user_answers[current_question][0] = 1
        elif num == 1 and user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if num == 2 and user_answers[current_question][1] == 0:
            user_answers[current_question][1] = 1
        elif num == 2 and user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if num == 3 and user_answers[current_question][2] == 0:
            user_answers[current_question][2] = 1
        elif num == 3 and user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0

class question14(QDialog):
    def __init__(self):
        super(question14, self).__init__()
        loadUi("question14.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        self.btn4.setText(questions_and_answers_text[questions_list[current_question]][4])
        if user_answers[current_question][0] == 1:
            self.btn1.setChecked(1)
        if user_answers[current_question][0] == 2:
            self.btn2.setChecked(1)
        if user_answers[current_question][0] == 3:
            self.btn3.setChecked(1)
        if user_answers[current_question][0] == 4:
            self.btn4.setChecked(1)
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3
        if num == 4:
            user_answers[current_question][0] = 4

class question24(QDialog):
    def __init__(self):
        super(question24, self).__init__()
        loadUi("question24.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        self.btn4.setText(questions_and_answers_text[questions_list[current_question]][4])
        if user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0
        if user_answers[current_question][3] == 1:
            user_answers[current_question][3] = 0
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and user_answers[current_question][0] == 0:
            user_answers[current_question][0] = 1
        elif num == 1 and user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if num == 2 and user_answers[current_question][1] == 0:
            user_answers[current_question][1] = 1
        elif num == 2 and user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if num == 3 and user_answers[current_question][2] == 0:
            user_answers[current_question][2] = 1
        elif num == 3 and user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0
        if num == 4 and user_answers[current_question][3] == 0:
            user_answers[current_question][3] = 1
        elif num == 4 and user_answers[current_question][3] == 1:
            user_answers[current_question][3] = 0

class question15(QDialog):
    def __init__(self):
        super(question15, self).__init__()
        loadUi("question15.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        self.btn4.setText(questions_and_answers_text[questions_list[current_question]][4])
        self.btn5.setText(questions_and_answers_text[questions_list[current_question]][5])
        if user_answers[current_question][0] == 1:
            self.btn1.setChecked(1)
        if user_answers[current_question][0] == 2:
            self.btn2.setChecked(1)
        if user_answers[current_question][0] == 3:
            self.btn3.setChecked(1)
        if user_answers[current_question][0] == 4:
            self.btn4.setChecked(1)
        if user_answers[current_question][0] == 5:
            self.btn5.setChecked(1)
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3
        if num == 4:
            user_answers[current_question][0] = 4
        if num == 5:
            user_answers[current_question][0] = 5

class question25(QDialog):
    def __init__(self):
        super(question25, self).__init__()
        loadUi("question25.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        self.btn4.setText(questions_and_answers_text[questions_list[current_question]][4])
        self.btn5.setText(questions_and_answers_text[questions_list[current_question]][5])
        if user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0
        if user_answers[current_question][3] == 1:
            user_answers[current_question][3] = 0
        if user_answers[current_question][4] == 1:
            user_answers[current_question][4] = 0
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and user_answers[current_question][0] == 0:
            user_answers[current_question][0] = 1
        elif num == 1 and user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if num == 2 and user_answers[current_question][1] == 0:
            user_answers[current_question][1] = 1
        elif num == 2 and user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if num == 3 and user_answers[current_question][2] == 0:
            user_answers[current_question][2] = 1
        elif num == 3 and user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0
        if num == 4 and user_answers[current_question][3] == 0:
            user_answers[current_question][3] = 1
        elif num == 4 and user_answers[current_question][3] == 1:
            user_answers[current_question][3] = 0
        if num == 5 and user_answers[current_question][4] == 0:
            user_answers[current_question][4] = 1
        elif num == 5 and user_answers[current_question][4] == 1:
            user_answers[current_question][4] = 0

class question16(QDialog):
    def __init__(self):
        super(question16, self).__init__()
        loadUi("question16.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        self.btn4.setText(questions_and_answers_text[questions_list[current_question]][4])
        self.btn5.setText(questions_and_answers_text[questions_list[current_question]][5])
        self.btn6.setText(questions_and_answers_text[questions_list[current_question]][6])
        if user_answers[current_question][0] == 1:
            self.btn1.setChecked(1)
        if user_answers[current_question][0] == 2:
            self.btn2.setChecked(1)
        if user_answers[current_question][0] == 3:
            self.btn3.setChecked(1)
        if user_answers[current_question][0] == 4:
            self.btn4.setChecked(1)
        if user_answers[current_question][0] == 5:
            self.btn5.setChecked(1)
        if user_answers[current_question][0] == 6:
            self.btn6.setChecked(1)
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.btn6.clicked.connect(lambda checked, num=6: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3
        if num == 4:
            user_answers[current_question][0] = 4
        if num == 5:
            user_answers[current_question][0] = 5
        if num == 6:
            user_answers[current_question][0] = 6

class question26(QDialog):
    def __init__(self):
        super(question26, self).__init__()
        loadUi("question26.ui", self)
        global current_question
        self.label.setText(questions_and_answers_text[questions_list[current_question]][0])
        self.btn1.setText(questions_and_answers_text[questions_list[current_question]][1])
        self.btn2.setText(questions_and_answers_text[questions_list[current_question]][2])
        self.btn3.setText(questions_and_answers_text[questions_list[current_question]][3])
        self.btn4.setText(questions_and_answers_text[questions_list[current_question]][4])
        self.btn5.setText(questions_and_answers_text[questions_list[current_question]][5])
        self.btn6.setText(questions_and_answers_text[questions_list[current_question]][6])
        if user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0
        if user_answers[current_question][3] == 1:
            user_answers[current_question][3] = 0
        if user_answers[current_question][4] == 1:
            user_answers[current_question][4] = 0
        if user_answers[current_question][5] == 1:
            user_answers[current_question][5] = 0
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.btn6.clicked.connect(lambda checked, num=6: self.btnfunction(num))
        if current_question != number_of_questions + 1:
            if current_question > 0:
                if questions_type[questions_list[current_question - 1]] == "12":
                    self.behindButton.clicked.connect(behindfunction12)
                if questions_type[questions_list[current_question - 1]] == "22":
                    self.behindButton.clicked.connect(behindfunction22)
                if questions_type[questions_list[current_question - 1]] == "13":
                    self.behindButton.clicked.connect(behindfunction13)
                if questions_type[questions_list[current_question - 1]] == "23":
                    self.behindButton.clicked.connect(behindfunction23)
                if questions_type[questions_list[current_question - 1]] == "14":
                    self.behindButton.clicked.connect(behindfunction14)
                if questions_type[questions_list[current_question - 1]] == "24":
                    self.behindButton.clicked.connect(behindfunction24)
                if questions_type[questions_list[current_question - 1]] == "15":
                    self.behindButton.clicked.connect(behindfunction15)
                if questions_type[questions_list[current_question - 1]] == "25":
                    self.behindButton.clicked.connect(behindfunction25)
                if questions_type[questions_list[current_question - 1]] == "16":
                    self.behindButton.clicked.connect(behindfunction16)
                if questions_type[questions_list[current_question - 1]] == "26":
                    self.behindButton.clicked.connect(behindfunction26)
            else:
                self.behindButton.setText("Выход")
                self.behindButton.clicked.connect(exitfunction)
        if current_question != number_of_questions - 1:
            if questions_type[questions_list[current_question + 1]] == "12":
                self.nextButton.clicked.connect(nextfunction12)
            if questions_type[questions_list[current_question + 1]] == "22":
                self.nextButton.clicked.connect(nextfunction22)
            if questions_type[questions_list[current_question + 1]] == "13":
                self.nextButton.clicked.connect(nextfunction13)
            if questions_type[questions_list[current_question + 1]] == "23":
                self.nextButton.clicked.connect(nextfunction23)
            if questions_type[questions_list[current_question + 1]] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[questions_list[current_question + 1]] == "24":
                self.nextButton.clicked.connect(nextfunction24)
            if questions_type[questions_list[current_question + 1]] == "15":
                self.nextButton.clicked.connect(nextfunction15)
            if questions_type[questions_list[current_question + 1]] == "25":
                self.nextButton.clicked.connect(nextfunction25)
            if questions_type[questions_list[current_question + 1]] == "16":
                self.nextButton.clicked.connect(nextfunction16)
            if questions_type[questions_list[current_question + 1]] == "26":
                self.nextButton.clicked.connect(nextfunction26)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and user_answers[current_question][0] == 0:
            user_answers[current_question][0] = 1
        elif num == 1 and user_answers[current_question][0] == 1:
            user_answers[current_question][0] = 0
        if num == 2 and user_answers[current_question][1] == 0:
            user_answers[current_question][1] = 1
        elif num == 2 and user_answers[current_question][1] == 1:
            user_answers[current_question][1] = 0
        if num == 3 and user_answers[current_question][2] == 0:
            user_answers[current_question][2] = 1
        elif num == 3 and user_answers[current_question][2] == 1:
            user_answers[current_question][2] = 0
        if num == 4 and user_answers[current_question][3] == 0:
            user_answers[current_question][3] = 1
        elif num == 4 and user_answers[current_question][3] == 1:
            user_answers[current_question][3] = 0
        if num == 5 and user_answers[current_question][4] == 0:
            user_answers[current_question][4] = 1
        elif num == 5 and user_answers[current_question][4] == 1:
            user_answers[current_question][4] = 0
        if num == 6 and user_answers[current_question][5] == 0:
            user_answers[current_question][5] = 1
        elif num == 6 and user_answers[current_question][5] == 1:
            user_answers[current_question][5] = 0


class Congratulation(QDialog):
    def __init__(self):
        super(Congratulation, self).__init__()
        loadUi("Congratulation.ui", self)
        res = 0
        global tries
        tries[current_user] = str(int(tries[current_user]) - 1)
        for i in range(number_of_questions):
            if questions_type[questions_list[i]][0] == "1":
                if user_answers[i][0] == correct_answers[questions_list[i]][0]:
                    res = res + 1

            else:
                if questions_type[questions_list[i]][1] == "2" and (str(user_answers[i][0]) + str(user_answers[i][1])) == correct_answers[questions_list[i]][0]:
                    res = res + 1
                if questions_type[questions_list[i]][1] == "3" and (str(user_answers[i][0]) + str(user_answers[i][1]) + str(user_answers[i][2])) == correct_answers[questions_list[i]][0]:
                    res = res + 1
                if questions_type[questions_list[i]][1] == "4" and (str(user_answers[i][0]) + str(user_answers[i][1]) + str(user_answers[i][2]) + str(user_answers[i][3])) == correct_answers[questions_list[i]][0]:
                    res = res + 1
                if questions_type[questions_list[i]][1] == "5" and (str(user_answers[i][0]) + str(user_answers[i][1]) + str(user_answers[i][2]) + str(user_answers[i][3]) + str(user_answers[i][4])) == correct_answers[questions_list[i]][0]:
                    res = res + 1
                if questions_type[questions_list[i]][1] == "6" and (str(user_answers[i][0]) + str(user_answers[i][1]) + str(user_answers[i][2]) + str(user_answers[i][3]) + str(user_answers[i][4]) + str(user_answers[i][5])) == correct_answers[questions_list[i]][0]:
                    res = res + 1
        if res > int(users_best_test_result[current_user]):
            users_best_test_result[current_user] = str(res)
        self.best_result.setText("Лучший результат тестирования: " + users_best_test_result[current_user] + "/" + str(number_of_questions))
        self.result.setText("Результат тестирования: " + str(res) + "/" + str(number_of_questions))
        self.exitButton.clicked.connect(exitfunction)
        if int(tries[current_user]) > 0:
            self.restartButton.clicked.connect(self.restartfunction)
        else:
            self.restartButton.setVisible(False)

    def restartfunction(self):
        global current_question
        global user_answers
        user_answers = [[0 for j in range(6)] for i in range(number_of_questions)]
        current_question = 0
        UserMenuWindow = UserMenu()
        all_widgets['UserMenuwidget'] = UserMenuWindow
        widget.addWidget(all_widgets['UserMenuwidget'])
        widget.setCurrentWidget(all_widgets['UserMenuwidget'])

data = []
with open("test1.txt", encoding="utf-8") as test:
    for line in test:
        data.append(line.rstrip('\n'))
questions_type = []
t = 0
q = 0
a = 0
c = 0
j = 1
for i in range(len(data)):
    if data[i] == "max_tries:":
        max_tries = data[i + 1]
    if data[i] == "name:":
        test_name = data[i+1]
    if data[i] == "total_number_of_questions:":
        total_number_of_questions = int(data[i+1])
        questions_and_answers_text = [[] for i in range(total_number_of_questions)]
        correct_answers = [[] for i in range(total_number_of_questions)]
    if data[i] == "number_of_questions:":
        number_of_questions = int(data[i+1])
        questions_list = [-1 for i in range(number_of_questions)]
        for v in range(number_of_questions):
            temp = -1
            while temp in questions_list:
                temp = random.randint(0, total_number_of_questions - 1)
            questions_list[v] = temp
    if data[i] == "type:":
        questions_type.append(data[i+1])
        t = t + 1
    if data[i] == "question:":
        questions_and_answers_text[q].append(data[i + 1])
        q = q + 1
    if data[i] == "answers:" and questions_type[t - 1][1] == "2":
        questions_and_answers_text[a].append(data[i + 1])
        questions_and_answers_text[a].append(data[i + 2])
        a = a + 1
    if data[i] == "answers:" and questions_type[t - 1][1] == "3":
        questions_and_answers_text[a].append(data[i + 1])
        questions_and_answers_text[a].append(data[i + 2])
        questions_and_answers_text[a].append(data[i + 3])
        a = a + 1
    if data[i] == "answers:" and questions_type[t - 1][1] == "4":
        questions_and_answers_text[a].append(data[i + 1])
        questions_and_answers_text[a].append(data[i + 2])
        questions_and_answers_text[a].append(data[i + 3])
        questions_and_answers_text[a].append(data[i + 4])
        a = a + 1
    if data[i] == "answers:" and questions_type[t - 1][1] == "5":
        questions_and_answers_text[a].append(data[i + 1])
        questions_and_answers_text[a].append(data[i + 2])
        questions_and_answers_text[a].append(data[i + 3])
        questions_and_answers_text[a].append(data[i + 4])
        questions_and_answers_text[a].append(data[i + 5])
        a = a + 1
    if data[i] == "answers:" and questions_type[t - 1][1] == "6":
        questions_and_answers_text[a].append(data[i + 1])
        questions_and_answers_text[a].append(data[i + 2])
        questions_and_answers_text[a].append(data[i + 3])
        questions_and_answers_text[a].append(data[i + 4])
        questions_and_answers_text[a].append(data[i + 5])
        questions_and_answers_text[a].append(data[i + 6])
        a = a + 1
    if data[i] == "correct:" and questions_type[t - 1][0] == "1":
        correct_answers[c].append(int(data[i + 1]))
        c = c + 1
    if data[i] == "correct:" and questions_type[t - 1][0] == "2":
        correct_answers[c].append(data[i + 1])
        c = c + 1

current_question = 0
user_answers = [[0 for j in range(6)] for i in range(number_of_questions)]

data.clear()
with open("Users.txt", encoding="utf-8") as users:
    for line in users:
        data.append(line.rstrip('\n'))
users_login = []
users_password = []
users_level = []
users_best_test_result = []
tries = []
for i in range(len(data)):
    if data[i] == "tries:":
        tries.append(data[i+1])
    if data[i] == "login:":
        users_login.append(data[i+1])
    if data[i] == "password:":
        users_password.append(data[i+1])
    if data[i] == "level:":
        users_level.append(data[i+1])
    if data[i] == "best_test_result:":
        users_best_test_result.append(data[i+1])

current_user = -1
amount_of_new_questions = 0
new_question_and_answers = []
new_correct = []
new_correct2 = [[0 for j in range(6)]for i in range(1)]
qtype = ''
new_test = True

app = QApplication(sys.argv)
menuWindow = MenuWindow()
all_widgets = {'menuwidget': menuWindow}
widget = QtWidgets.QStackedWidget()
widget.addWidget(all_widgets['menuwidget'])
widget.setCurrentWidget(all_widgets['menuwidget'])
widget.setFixedWidth(1350)
widget.setFixedHeight(650)
widget.setWindowTitle('Geleos & Grunt Test System')
widget.show()
app.exec_()
