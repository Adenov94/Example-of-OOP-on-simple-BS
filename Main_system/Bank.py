
class bank:
    __id = 0
    __balance = 0
    #costumer = 1

    def __init__(self, id, amount, costumer_count=None):
        try:
            self.__id = id
            if amount>0:
                self.__balance = amount
            else:
                print("Balance shouldn't be zero")
            self.costumer = costumer_count
            #costumer_num = costumer_count
        except NameError:
                print("Enter the number")

    def dep (self, amount):
        if amount>0:
            self.__balance += amount
            return True
        else:
            return False


    def withdr(self, amount):
        if (amount >0 and amount <= self.__balance):
            self.__balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        print(self.__balance)

    def ret_id(self):
        return self.__id