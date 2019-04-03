from Main_system.Bank import bank

class bank_oper(bank):

    def __init__(self):
        pass

    def deposit(self, object, amount):
        if object.dep(amount):
            print("Successfull deposit of %i" %amount)
        else:
            print("The error on deposit")

    def withdraw(self, object, money):
        if (object.withdr(money)):
            print("Thanks for service")
        else:
            print("error on withdraw")

    def transfer(self, object_w, object_d, amount):
        if (object_w.withdr(amount) and object_d.dep(amount)):
            print("Transfer succesfully")
        else:
            print("error")

    def check(self, object):
        object.check_balance()


   # def check_balance(self, object):
    #    print(object.__balance)
