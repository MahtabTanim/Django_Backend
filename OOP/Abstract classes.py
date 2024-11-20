# Import the ABC class and abstractmethod decorator from abc
from abc import ABC, abstractmethod


# Define an abstract base class called Company
class Company(ABC):
    # Create an abstract method called create_budget()
    @abstractmethod
    def create_budget(self):
        pass

    # Create a concrete method with name hire_employee()
    def hire_employee(self, name):
        print(f"Welcome to the team, {name}!")


class Technology(Company):
    def __init__(self, name):
        self.name = name

    # Define a create_budget() method
    def create_budget(self, year, expenses):
        for expense, amount in expenses.items():
            print(f"{year} budget for {expense} is {amount}")


# Create an instance of the Technology class, call methods
t = Technology("Tina's Tech Advisors")
t.create_budget(2024, {"Salaries": 10000, "Supplies": 500})
t.hire_employee("Christian")
