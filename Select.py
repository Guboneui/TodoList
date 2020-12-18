import sys
class Select:
    todolist = []
    num = 0
    num_index = 0
    text = ''

    def __init__(self):
        Select.text = ''
        Select.num = 0
        Select.num_index = 0
        Select.todolist = []

    def select(self):
        Select.todolist = [1]


    def add(self):
        result = self.text
        return result

    def selectMenu(self):
        print("1: 추가\t2: 수정\t3: 삭제\t4: 나가기\t\t(clear포함)) \t 특정 요일을 보고 싶을 경우 '모아보기' 입력" )
        print("선택 : ")

        check = input()
        if (check == "1"):
            self.addTodo()

        elif (check == "2"):
            self.updateTodo()

        elif (check == "3"):
            self.deleteTodo()

        elif (check == "4"):
            print("프로그램을 종료합니다.")
            sys.exit()

        elif (check == "모아보기"):
            self.checkDay()

        elif (check == "clear"):
            self.clear()

            print("클리어 완료")

    def updatingMessage(self):
        print("updating...")

    def printTitle(self):
        print("todolist")

    def checkDay(self):
        day = input("보고싶은 요일을 영어로 입력해 주세요. Mon, Tue...")
        day_list = []

        if day == "Mon":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list[4:])

        elif day == "Tue":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list)

        elif day == "Wed":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list)

        elif day == "Wed":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list)

        elif day == "Thu":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list)

        elif day == "Fri":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list)

        elif day == "Sat":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list)

        elif day == "Sun":
            for list in Select.todolist:
                if list[0:3] == day:
                    day_list.append(list)

        print(day_list)

    def addTodo(self):
        print("추가할 내용을 요일을 꼭 포함해 입력해 주세요: ex) Mon.~~")
        Select.text = input()
        text_result = Select.text
        Select.todolist.append(text_result)
        self.updatingMessage()
        print(Select.todolist)
        print()

    def updateTodo(self):
        self.printTitle()
        Select.num = int(input("변경할 번호를 입력해 주세요: "))
        num_result = Select.num
        Select.num_index = num_result - 1
        Select.text = input("변경할 내용을 입력해 주세요(요일 포함)")
        text_result = Select.text
        Select.todolist[Select.num_index] = text_result
        print(Select.todolist)
        self.updatingMessage()

    def deleteTodo(self):
        self.printTitle()
        Select.num = int(input("삭제할 번호를 입력해 주세요: "))
        num_result = Select.num
        Select.num_index = num_result - 1
        del Select.todolist[Select.num_index]
        print(Select.todolist)
        self.updatingMessage()


    def clear(self):
        Select.todolist = []
        print(Select.todolist)
        self.updatingMessage()

    def start(self):
        while True:
            self.printTitle()
            self.selectMenu()
