class Flipcart:

    discount = 10

    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount = newdiscount
        print(f'{cls.discount} is updated')

    def userinfo(self,name,ph):
        self.name = name
        self.ph = ph
        print(f'usernsme: {self.name}')
        print(f'phone number: {self.ph}')

    @staticmethod
    def banner():
        print('Welcome to the flipcart\n10% discount is going on, shop now')

ramesh = Flipcart()
ramesh.userinfo('ramesh',7799446611)

ramesh.updatediscount(30)
Flipcart.updatediscount(40)

ramesh.banner()
Flipcart.banner()
