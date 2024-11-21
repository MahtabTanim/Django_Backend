from abc import ABC, abstractmethod


class Customer(ABC):
  @abstractmethod
  def make_payment(self, price):
    pass

class RewardsMember(Customer):
  def make_payment(self, price):
    print(f"""Total price for rewards member is 
          ${price * .90}, which is 10% off""")

class NewCustomer(Customer):
  def make_payment(self, price):
    print(f"""Total price for new customer is ${price}""")


class Checkout:
  # Create a _get_customer() factory method 
  def _get_customer(self, customer_type):
    if customer_type == "Rewards Member":
      return RewardsMember()
    elif customer_type == "New Customer":
      return NewCustomer()
  
  # Define the complete_transaction() method
  def complete_transaction(self, customer_type, price):
    customer = self._get_customer(customer_type)
    customer.make_payment(price)

# x = Checkout()
# x.complete_transaction("Rewards Member",100)


class LLM(ABC):
  @abstractmethod
  def complete_sentence(self, prompt):
    pass
# Finish defining OpenAI and Anthropic classes
class OpenAI(LLM):
  def complete_sentence(self, prompt):
    return prompt + " ... OpenAI end of sentence."
  
class Anthropic(LLM):
  def complete_sentence(self, prompt):
    return prompt + " ... Anthropic end of sentence."
  
class ChatBot:
    def _get_llm(self, provider):
        if provider == "OpenAI":
            return OpenAI()
        elif provider== "Anthropic":
            return Anthropic()
    
    def chat(self, prompt, provider):
    # Return an llm object, then call complete_sentence()
        llm = self._get_llm(provider)
        return llm.complete_sentence(prompt)