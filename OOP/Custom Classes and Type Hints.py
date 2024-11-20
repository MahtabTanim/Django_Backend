# Import Dict and List from typing
from typing import Dict,List

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
    def __init__(self,codename:str,missions:int,):
        self.codename: str = codename
        self.missions : int = missions 
    def add_mission(self,location:str) -> str:
        self.missions += 1
        print(f"{self.codename} completed a mission in " + \
          f"{location}. This was mission #{self.missions}")


x = Agent("X",100)
x.add_mission("XXXX")