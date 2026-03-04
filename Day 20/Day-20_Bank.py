from abc import ABC,abstractmethod
class BankAccount(ABC):
    def checkbalance(self):
        print("you cna check out your balance")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingsAccount(BankAccount):
    def deposit(self):
        print('2 lakhs per day')
    def withdraw(self):
        print('1 lakh you can withdraw')

class CurrentAccount(BankAccount):
    def deposit(self):
        print('unlimeted deposut')
    def withdraw(self):
        print('unlimeted withdraawl')

class JointAccount(BankAccount):
    def deposit(self):
        print('only two people can deposit')
    def withdraw(self):
        print('1-2 lakhs per day you can withdraw')

class SalaryAccount(BankAccount):
    def deposit(self):
        print('no limit')
    def withdraw(self):
        print('20k - 1lakh per day')

class PensionAccount(BankAccount):
    def deposit(self):
        print('no deposit')
    def withdraw(self):
        print('40k per day')

print('-------------luffy-------------')
luffy = SavingsAccount()
luffy.checkbalance()
luffy.deposit()
luffy.withdraw()

print('-------------naruto-------------')
naruto = CurrentAccount()
naruto.checkbalance()
naruto.deposit()
naruto.withdraw()

print('-------------ichego-------------')
ichego = JointAccount()
ichego.checkbalance()
ichego.deposit()
ichego.withdraw()

print('-------------eren-------------')
eren = SalaryAccount()
eren.checkbalance()
eren.deposit()
eren.withdraw()

print('-------------shadow-------------')
shadow = PensionAccount()
shadow.checkbalance()
shadow.deposit()
shadow.withdraw()
