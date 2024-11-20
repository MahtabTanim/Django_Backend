class Computer:
  def __init__(self, software_version):
    self.software_version = software_version

  def install_app(self, app_name, app_store):
    if app_store:
      print(f"Installing {app_name} from App Store.")
    else:
      print(f"Installing {app_name} from other provider.")

  def update_software(self, new_software_version):
      self.software_version = new_software_version
    
class Tablet(Computer):
  def install_app(self, app_name):
    print(f"{app_name} is being installed from the Tablet App Store.")

my_tablet = Tablet("1.1.1")

my_tablet.install_app("Datacamp")


class Team:
    def __init__(self,team_members):
       self.team_members = team_members
    def __add__(self,other):
       return self.team_members+ other.team_members
a =Team([1,2,3])
b =Team([3,4,5])
print(a+b)


class Network:
  def __init__(self, ip_addresses):
    self.ip_addresses = ip_addresses
class Computer :
    def __init__(self,operating_system, ip_address):
       self.operating_system = operating_system
       self.ip_address = ip_address
    def __add__(self, other):
        if self.operating_system == other.operating_system:
           return Network([self.ip_address, other.ip_address])
        raise Exception("Incompatible operating systems.")
# c1 = Computer("1","123")
c2 = Computer("1","245")
net = c1+c2
print(net.ip_addresses)

class Computer:
  def __init__(self, brand):
    self.brand = brand

  def browse_internet(self):
    print(f"Using {self.brand}'s default internet browser.")

class Tablet(Computer):
    def __init__(self, brand, apps):
       Computer.__init__(self, brand)
       self.apps = apps
    def uninstall_app(self, app):
       if app in self.apps:
          self.apps.remove(app)

class Smartphone(Tablet):
    def __init__(self, brand, apps, phone_number):
       Tablet.__init__(self,brand,apps)
       self.phone_number = phone_number
    def send_text(self, message,recipient):
       print(f"Sending {message} to {recipient} from {self.phone_number}")

personal_phone = Smartphone("Macrosung", ["Weather", "Camera"], "801-932-7629")
personal_phone.browse_internet()
personal_phone.uninstall_app("Weather")
personal_phone.send_text("Time for a new mission!","Chuck")


class Telephone:
  def __init__(self, phone_number):
    self.phone_number = phone_number

  def make_call(self, recipient):
    print(f"Calling {recipient} from {self.phone_number}")


class Smartphone(Computer,Telephone):
    def __init__(self, brand,phone_number,music_app):
       Computer.__init__(self,brand)
       Telephone.__init__(self,phone_number)
       self.music_app = music_app
    def play_music(self,song):
       print(f"Playing {song} using {self.music_app}")

personal_phone = Smartphone("Macrosung", "801-932-7629", "Dotify")
# Browse the internet, make a call to Alex, and play music
personal_phone.browse_internet()
personal_phone.make_call("Alex")
personal_phone.play_music("Creeks and Highways")