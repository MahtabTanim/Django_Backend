# Import Dict and List from typing
from typing import Dict, List

# Type hint the roster of codenames and number of missions
roster: Dict[str, int] = {
    "Chuck": 37,
    "Devin": 2,
    "Steven": 4
}

# Unpack the values and add type hints for the new list
agents: List[str] = [
    f"Agent {agent}, {missions} missions" \
    for agent, missions in roster.items()
]


# print(repr(agents))

class Agent:
    def __init__(self, codename: str, missions: int, ):
        self.codename: str = codename
        self.missions: int = missions


def add_mission(self, location: str) -> None:
    self.missions += 1
    print(f"{self.codename} completed a mission in " + \
          f"{location}. This was mission #{self.missions}")


# Create an Agent object, add type hints
chuck: Agent = Agent("Charles Carmichael", 37)

# Create a list of locations, add a mission for each
locations: List[str] = ["Burbank", "Paris", "Prague"]


# for location in locations:
#   chuck.add_mission(location)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return f"${round(self._balance, 2)}"

    @balance.setter
    def balance(self, new_balance):
        if new_balance > 0:
            self._balance = new_balance

    @balance.deleter
    def balance(self):
        print("Deleting the 'balance' attribute")
        del self._balance


checking_account = BankAccount(100)

# Output the balance of the checking_account object
print(checking_account.balance)

# Set the balance to 150, output the new balance
checking_account.balance = 150
print(checking_account.balance)

# Delete the balance attribute, attempt to print the balance
del checking_account.balance


class BankAccount2:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return f"Email for this account is: {self._email}"

    @email.setter
    def email(self, new_email_address):
        if "@" in new_email_address:
            self._email = new_email_address
        else:
            print("Please make sure to enter a valid email.")

    @email.deleter
    def email(self):
        del self._email
        print("Email deleted, make sure to add a new email!")


b2 = BankAccount2("fsdfjhdsbj@emafiefre.com")

print(b2.email)
b2.email = "eenrewjn@ejjfnsdkfn.com"
print(b2.email)
del b2.email
b2.email = "fnjsdnkjn@kjfnesdfe"
print(b2.email)
