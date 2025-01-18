class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__secret = 'This is my secret'  # 私有变量

    def getName(self):
        return self.name

    def getSecret(self):
        return self.__secret

    # 私有方法
    def __selfFunc(self):
        print("这是私有方法！", self.__secret)

    def useSelfFunc(self):
        self.__selfFunc()


# 子类Student
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grade = 'A+'

    def info(self):
        print(self.name, self.age, self.grade)


if __name__ == '__main__':
    teacher_yi = Student('翼老师', 100)
    teacher_yi.info()
