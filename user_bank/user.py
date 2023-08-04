from jianno_bankAccount import bankAccount

class user(bankAccount):
    def __init__(self, name:str, last_name:str, email:str, age:int, balance:int, interest_rate:int) -> None:
        super().__init__(self, balance, interest_rate)
        self.first_name = name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0

    def __repr__(self):
        return(f'Hi {self.first_name} {self.last_name}\nemail: {self.email}\naccount balance: {self.balance}')

    def enroll_member(self):
        print(f'rewards member status: {self.rewards_member}')

    def enroll(self, member):
        self.rewards_member = member
        if True:
            self.gold_card_points = 200
        return self.gold_card_points

        
    def spend_points(self, points):
        if points <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - (points)
        print(f'available points: {self.gold_card_points}')

        

    def display_info(self):
        pass



john = user(name = 'john', last_name = 'casey', email = 'jcasey@buymore.com', age = 51, balance = 1, interest_rate = 0)
chuck = user(name = 'chuck', last_name = 'bartowski', email = 'cbartowski@nerdherd.com', age = 41, balance = 1, interest_rate = 0)

john.account_deposit(200)
john.account_withdraw(25)
print(john)
john.enroll(True)
john.enroll_member()
john.spend_points(50)

print('#' * 20)


print (chuck)
chuck.enroll(True)
chuck.enroll_member()
chuck.spend_points(80)