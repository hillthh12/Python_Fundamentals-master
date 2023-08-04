class bankAccount:
    def __init__(self,name:str, balance:int, interest_rate:int) -> None:
        self.balance = balance
        self.interest_rate = interest_rate
        self.name = name


    def account_deposit(self, deposit) -> int:
        self.balance = self.balance + (deposit)
        return(f'deposit: {deposit}')

    def account_withdraw(self, withdraw) -> int:
        if withdraw <= self.balance:
            self.balance = self.balance - (withdraw)
        else:
            print(f'{self.name}: you broke')

    def yield_interest(self) -> int:
        return self.interest_rate / 12

    def interest(self):
        return self.balance * self.yield_interest()

    def __repr__(self):
        return(f"{self.name}'s account balance is {self.balance}\ninterest rate: {self.interest_rate}\nearning interest: {self.interest()}")


miss_piggy = bankAccount(name = 'miss piggy',balance = 100000, interest_rate = .0125)
gonzo = bankAccount(name = 'gonzo', balance = 25, interest_rate = .0125)

miss_piggy.account_deposit(200)
miss_piggy.account_deposit(1000)
miss_piggy.account_deposit(1000)
miss_piggy.account_withdraw(40)
#print(miss_piggy)


gonzo.account_deposit(20)
gonzo.account_deposit(400)
gonzo.account_withdraw(75)
gonzo.account_withdraw(100)
gonzo.account_withdraw(100)
gonzo.account_withdraw(200)
#print(gonzo)
