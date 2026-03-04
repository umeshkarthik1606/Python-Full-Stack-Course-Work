'''
class Flipkart:
    discount = 10

    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount = newdiscount
        print()

    def userinfo(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        print(f'Username: {self.name}')
        print(f'Phone number: {self.phonenumber}')

    @staticmethod
    def banner():
        print("Welcome to the flipkart\n10% discount is going on,shop now")





dileep = Flipkart()
dileep.userinfo('dileep',87654321987)

dileep.updatediscount(30)
Flipkart.updatediscount(40)

dileep.banner()
Flipkart.banner()

dileep1 = Flipkart()
dileep.userinfo('dileep1',87654321980)


dileep2 = Flipkart()
dileep.userinfo('dileep2',87654321907)
'''

'''
#CONSTRUCTOR
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Hey {self.username}, Welcome to the Instagram!!!")


Dileep = Instagram('dileep','D@123')
Ramu = Instagram('ramu','R@123')
'''
'''
#INHERITANCE
# Base Version
class InstagramV1:
    def __init__(self, username):
        self.username = username
        print(f"Hey {self.username}, Welcome to the Instagram!!!")

    def reels(self):
        print("You can upload and scroll the reels")

    def posts(self):
        print("You can post your pics")


class InstagramV2(InstagramV1):
    def __init__(self, username):
        super().__init__(username)

    def story(self):
        print("You can upload the story")


class InstagramV3(InstagramV2):
    def __init__(self, username):
        super().__init__(username)

    def note(self):
        print("You can upload a note")


class Live:
    def launchlive(self):
        print("Now you can go on live")


class Verification:
    def verify(self):
        print("You can verify your account for better features")


class InstagramV4(InstagramV3, Live, Verification):
    def __init__(self, username):
        super().__init__(username)


class Creator:
    def insights(self):
        print("You can check your post insights")


class Business(InstagramV4, Creator):
    def __init__(self, username):
        super().__init__(username)

    def buttons(self):
        print("You can contact them via mail and number")


# Testing
Dileep = InstagramV1('Dileep')
Dileep.reels()
Dileep.posts()

Ramu = InstagramV2('Ramu')
Ramu.reels()
Ramu.posts()
Ramu.story()

Ravi = InstagramV3('Ravi')
Ravi.reels()
Ravi.posts()
Ravi.story()
Ravi.note()

abid = InstagramV4('abid')
abid.reels()
abid.posts()
abid.story()
abid.note()
abid.launchlive()
abid.verify()

ram = Business('ram')
ram.reels()
ram.posts()
ram.story()
ram.note()
ram.launchlive()
ram.verify()
ram.insights()
ram.buttons()
'''




#POLYMORPHISM

class Hotstar:
    def __init__(self,username):
        print(f'Hey {username}, Welcome to the Hotstar')

    def playvideo(self):
        print("ads will play")
        print("Quality is low")
        print("No download option")
        print("No multiple logins")
        
    def search(self):
        print("You can search for program")
    def watchlist(self):
        print("You can add movies to watchlist")
    def notifications(self):
        print("You can get the push notifications")
    def login(self):
        print("You can login to hotstar")
        



























































































































