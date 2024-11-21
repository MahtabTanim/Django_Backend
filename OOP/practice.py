class Person:
    def __init__(self):
        pass
    @classmethod
    def greet(cls,word:str):
        print(word)
        return 100

Person.greet("Hello")