class InstagramV1:
    def __init__(self,username):
        self.username = username
        print(f'hey {self.username}, Welcome to the Instagram.!.')

    def reels(self):
        print('You can uplode and scroll the reels')

    def post(self):
        print('You can post your pics')

class InstagramV2(InstagramV1):
    def __init__(self,username):
        super().__init__(username)

    def story(self):
        print('You can uplode the story')

class InstagramV3(InstagramV2):
    def __init__(self,username):
        super().__init__(username)

    def note(self):
        print('You can add notes')


class Live:
    def launchlive(self):
        print('Now you can go live')

class verification:
    def verify(self):
        print('You can verify your account for better feature')
        
class InstagramV4(InstagramV3,Live,verification):
    def __init__(self,username):
        super().__init__(username)
    
class Creator(InstagramV4):
     def __init__(self,username):
        super().__init__(username)

     def insights(self):
         print('You can check your post insights')

class Business(InstagramV4):
    def __init__(self,username):
        super().__init__(username)

    def buttons(self):
        print('You can contact them through mail and number')

franky = InstagramV1('franky')
franky.reels()
franky.post()

sanji = InstagramV2('sanji')
sanji.reels()
sanji.post()
sanji.story()

jimbi = InstagramV3('jimbi')
jimbi.note()

ussope = InstagramV4('ussope')
ussope.launchlive()
ussope.verify()

        
