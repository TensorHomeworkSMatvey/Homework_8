class Animals:
    def __init__(self, body_growth):
        self.body_growth = body_growth
    def Anim(self):
        return "Im's animal"

class Mammals(Animals):
    def __init__(self, body_growth, view):
        super().__init__(body_growth)
        self.view = view
    def Mamm(self):
        return "Im's mammal"

class Human(Mammals):
    def __init__(self, body_growth, view, age, name, activity):
        super().__init__(body_growth, view)
        self.age = age
        self.name = name
        self.activity = activity
    def Hum(self):
        return "Im's human"

class Cats(Mammals):
    def __init__(self, body_growth, view, age, nickname, breed):
        super().__init__(body_growth, view)
        self.age = age
        self.nickname = nickname
        self.breed = breed
    def Cat(self):
        return "Im's cat"

class Dogs(Mammals):
    def __init__(self, body_growth, view, age, nickname, type):
        super().__init__(body_growth, view)
        self.age = age
        self.nickname = nickname
        self.type = type
    def Dog(self):
        return "Im's dog"