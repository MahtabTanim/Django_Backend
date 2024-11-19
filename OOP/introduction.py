class Person:
  CURRENT_YEAR = 2024
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # Add a class method decorator
  @classmethod
  # Define the from_birth_year method
  def from_birth_year(cls, name, birth_year):
    # Create age
    age = Person.CURRENT_YEAR - birth_year
    # Return the name and age
    return cls(name,age)

# bob = Person.from_birth_year("Bob", 1990)
# print(bob.name)
# ros = Person("Ros",100)
# print(ros.name)

class BetterDate:
  def __init__(self, year, month, day):
    self.year, self.month, self.day = year, month, day
    
  # Define a class method from_str
  @classmethod
  def from_str(cls,datestr):
    # Split the string at "-"
    parts = datestr.split("-")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    # Return the class instance
    return cls(year,month,day)

# Create the xmas object      
# xmas = BetterDate.from_str("2024-12-25")   
# print(xmas.year)
# print(xmas.month)
# print(xmas.day)

class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  def __init__(self, name, salary=50000,project=None):
    Employee.__init__(self,name, salary)
    self.project = project
  def display(self):
    print("Manager ",self.name)

# Define a Manager object
# mng = Manager("Debbie Lashko",86500,"Hello")
# mng.give_raise(10000)

# # Print mng's name
# print(mng.name)
# print(isinstance(mng,Employee))

class Player:
    MAX_POSITION = 10

    def __init__(self):
      self.position = 0

    def move(self, steps):
      if self.position + steps < Player.MAX_POSITION:
        self.position += steps 
      else:
        self.position = Player.MAX_POSITION  

class Racer(Player):
  MAX_POSITION = 15

# p = Player()
# r = Racer()
# print("p.MAX_POSITION = ", p.MAX_POSITION)
# print("r.MAX_POSITION = ", r.MAX_POSITION)
# print(r.position)

# p1 = Player()
# p2 = Player()
# print(p1==p2)

class BankAccount:
  def __init__(self,number , balance = 0):
    self.balance = balance
    self.number = number
  def withdraw(self,amount):
    self.balance -= amount

  def __eq__(self, value):
    print('BankAccount __eq__ method invoked')
    return type(self)==type(value) and self.number == value.number
  def __repr__(self):
    return f"Customer {self.number} {self.balance}"
  # def __str__(self):
  #   return f"Number  : {self.number} balance {self.balance}"

class SavingsAccount(BankAccount):
  def __init__(self, number, balance,interest_rate):
    super().__init__(number, balance)
    self.interest_rate = interest_rate
  def __eq__(self, value):
    print('SavingsAccount __eq__ method invoked')
    return type(self)==type(value) and self.number == value.number

# a = BankAccount(123,1000)
# b = SavingsAccount(456,1000,0.05)
# print(a)



# Use a try - except - except pattern (with two except blocks) inside the function to catch
# Modify the function to catch exceptions
def invert_at_index(x, ind):
  try:
    return 1/x[ind]
  except ZeroDivisionError:
    print("Cannot divide by zero!")
  except IndexError:
    print("Index out of range!")
 
a_list = [5,6,0,7]

# Works okay
# print(invert_at_index(a_list, 1))

# Potential ZeroDivisionError
# print(invert_at_index(a_list, 2))

# Potential IndexError
# print(invert_at_index(a_list, 5))


class SalaryError(ValueError): 
  pass
class BonusError(SalaryError): 
  pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Raise exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
      raise BonusError("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
      raise SalaryError("The salary after bonus is too low!")
      
    self.salary += amount
