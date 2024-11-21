from abc import ABC,abstractmethod

class Product(ABC):
    @abstractmethod
    def purchase(self,quantity):
        pass
    @abstractmethod
    def update_price(self,new_price):
        pass 


class Business(ABC):
  @abstractmethod
  def sell_product(self, product_name, price, quantity):
    pass

# Create a class that inherits the Business interface
class Bakery(Business):
  def __init__(self, business_name):
    self.business_name = business_name
  
  # Provide a definition of the sell_product() method 
  def sell_product(self, product_name, price, quantity):
    total_revenue = price * quantity
    print(f"""{self.business_name} sold {quantity} {product_name} for a total of ${total_revenue}""")
    
# Attempt to create a Bakery object
blue_eyed_baker = Bakery("Blue Eyed Baker")
blue_eyed_baker.sell_product("x",100,12)
print("Hello world")


# Attempt to create a Bakery object, observe the exception
# try:
#   blue_eyed_baker = Bakery("Blue Eyed Baker")
# except Exception as e :
#   print(e)
