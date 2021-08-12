class Account:
    interest_rate = 0.58

    def __init__(self,owner,amount):
        self.owners=owner
        self.amounts=amount

    @classmethod
    def interest_by(Account,amt):
        return Account.interest_rate*amt


account=Account('tony',8000)
interest=Account.interest_by(12000)

print('用户：{}'.format(account.owners))
print('账户金额：{}'.format(account.amounts))
print('利率：{}'.format(Account.interest_rate))
print('利息：{0}'.format(interest))