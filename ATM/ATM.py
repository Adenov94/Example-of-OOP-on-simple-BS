from Main_system.Bank import bank

class atm(bank):

    def __init__(self, id, object):
        self.temp_id = object.ret_id()
        if (id == self.temp_id):
            print("Account was veriifed")
        else:
            print("Account error")


    def withdraw(self, object, money):
        if (object.withdr(money)):
            print("Thanks for  using our ATM")
        else:
            print("error on withdraw")
