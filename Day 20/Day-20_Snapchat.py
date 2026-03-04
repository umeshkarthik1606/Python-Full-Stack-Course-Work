try:
    class Snapchat:
        def __init__(self, username, password, friends):
            self.username = username
            self.__password = password
            self._friends = friends

        def getpassword(self):
            return self.__password

        def setpassword(self, new_password):
            self.__password = new_password

        @property
        def oprFriends(self):
            return self._friends
        
        @oprFriends.setter
        def oprFriends(self,new_friends):
            self._friends.append(new_friends)


    zoro = Snapchat('zoro', '123', ['luffy', 'jimbi'])

    print(f'Name before modification: {zoro.username}')
    zoro.username = 'moss head'
    print(f'Name after modification: {zoro.username}')

    print(f'Password before modification: {zoro.getpassword()}')
    zoro.setpassword('123@123')
    print(f'Password after modification: {zoro.getpassword()}')

    print(f'Friends before ading: {zoro.oprFriends}')
    zoro.oprFriends = 'robin'
    print(f'Friends after ading: {zoro.oprFriends}')
except (NameError,ValueError,AttributeError):
    print('There is an Error')
