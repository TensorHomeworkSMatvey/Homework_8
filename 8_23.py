class Human:
    def __init__(self, name, age, activity):
        self.name = name
        self.age = age
        self.activity = activity

class Student(Human):
    def __init__(self, name, age, activity, count_homework):
        super().__init__(name, age, activity)
        self.count_homework = count_homework
    def __lt__(self, other):
        return self.count_homework < other.count_homework
    def __le__(self, other):
        return self.count_homework <= other.count_homework
    def __eq__(self, other):
        return self.count_homework == other.count_homework
    def __ne__(self, other):
        return self.count_homework != other.count_homework
    def __gt__(self, other):
        return self.count_homework > other.count_homework
    def __ge__(self, other):
        return self.count_homework >= other.count_homework

Tim = Student("Tim", 19, "programmer", 5)
Tom = Student("Tom", 20, "programmer", 4)