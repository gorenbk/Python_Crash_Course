class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def talk(self,what):
        print(f"{self.name.title()} said {what.lower()}")