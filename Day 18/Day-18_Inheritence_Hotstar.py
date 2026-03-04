#inheritence
class Hotstar:
    def __init__(self,username):
        print(f'Hay {username}, Welcome to Hotstar')

    def playvideo(self):
        print('Ads will run')
        print('Quality is low')
        print('No downlode option')
        print('no Multiple logins')

    def search(self):
        print(f'You can search for program')
    def watchlist(self):
        print('you can add movies to searchlist')
    def notification(self):
        print('You can get the push Notifications')
    def login(self):
        print('You are logedin to the Hotstar')

class PremiumHotstar(Hotstar):
    def __init__(self,username):
        print(f'Hay {username}, Welcome to the Premium Hotstar')
    def plaayvideo(self):
        print('Ads will not run')
        print('Quality is High')
        print('downlode option')
        print('Multiple logins')
        
luffy = Hotstar('luffy')
luffy.playvideo()
luffy.search()
luffy.watchlist()
luffy.notification()
luffy.login()
