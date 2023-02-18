class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __call__(self):
        return self.name

    def __str__(self):
        # displaying ledger
        header = str(self.name).center(30, '*')
        for i in self.ledger:
            header += '\n'
            # first 23 letters of description aligned to the left
            header += '{:<23}'.format(str(i['description'])[:23])
            key = '{:.2f}'.format(i['amount'])
            # first 7 digits aligned to the right
            header += '{:>7}'.format(str(key)[:7])
        # displaying total balance on the bottom of each category
        header += '\nTotal: {:.2f}'.format(self.balance)
        return header

    def deposit(self, amount, description=''):
        description = description.strip('*')
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

# if no desc is given, it should default to an empty string. The method should append an aobject to the
# ledger list in the form of {"amount": amount, "description": description}

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({'amount':-abs(amount), 'description': description})
            self.balance -= amount
            return True

# similar to the deposit method, but the amount passed in should be stored
# in the ledger as a negative number. If there are not enough funds,
# nothing should be added to the ledger. This method should return True if
# the withdrawal took place, and False otherwise.

    def get_balance(self):
        return self.balance

# method that returns the current balance of the budget category based on the deposits and
# withdrawals that have occurred.

    def transfer(self, amount, category):
        # check if fund are available
        if self.check_funds(amount):
            # transferring amount to existing object
            category.deposit(amount, ('Transfer from %s' % self.name))

            # for name, value in globals().items():
            #     if name == category:
            #         value.deposit(amount, ("Transfer from %s" % self.name))
            #         continue
            # deducting amount from donors balance
            self.withdraw(amount, ("Transfer to %s" % category))
            return True
        else:
            return False

    # A transfer method that accepts an amount and another budget category as arguments.
    # The method should add a withdrawal with the amount and the description "Transfer to
    # [Destination Budget Category]". The method should then add a deposit to the other budget
    # category with the amount and the description "Transfer from [Source Budget Category]".
    # If there are not enough funds, nothing should be added to either ledgers.
    # This method should return True if the transfer took place, and False otherwise.
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True


# method that accepts an amount as an argument. It returns False if the amount is greater
# than the balance of the budget category and returns True otherwise. This method should be
# used by both the withdraw method and transfer method.
def create_spend_chart(categories):
    total_spent = []
    final_message = ''
    first_column = [['100|', '90|', '80|', '70|', '60|', '50|', '40|', '30|', '20|', '10|', '0|']]
    for i in categories:
        temp_spent = 0
        for j in i.ledger:
            if j['amount'] < 0:
                temp_spent += j['amount']
        total_spent.append({temp_spent: i.name})
    temp_amounts = []
    temp_names = []
    for i in total_spent:
        for amount, name in i.items():
            temp_amounts.append(amount)
            temp_names.append(name)
    summed_amounts = abs(sum(temp_amounts))
    # creating a list of bubbles, each corresponding to value of 10%, starting from 0%
    bubbles = []
    for i in temp_amounts:
        tmp_bubbles = []
        tmp_bubbles += ('o' for o in range(int((abs(i)*10)//summed_amounts)+1))
        bubbles.append(tmp_bubbles)
    # filling up the rest of the list with blank spaces, up to 11 values
    for i in range(len(bubbles)):
        for j in range(11-len(bubbles[i])):
            bubbles[i].insert(j, ' ')
    final_message +='Percentage spent by category\n'
    data = first_column + bubbles
    index = 0
    # creating final chart
    while index < 11:
        final_message += '{:>4}'.format(data[0][index])
        for j in range(1, len(data)):
            final_message += '{:^3}'.format(data[j][index])
        final_message += ' \n'
        index += 1
    final_message += '    ' + '-'*(((len(data)-1)*3)+1)+'\n'
    split_names = []
    for i in temp_names:
        split_names += [list(i)]
    col_length = (max([len(i) for i in split_names]))
    for i in split_names:
        while len(i) < col_length:
            i.append(' ')
    index = 0
    while index < col_length:
        final_message += '    '
        for i in range(len(split_names)):
            final_message += '{:^3}'.format(split_names[i][index])
        if index < col_length-1:
            final_message += ' \n'
        index += 1
    final_message += " "

    return final_message





tools = Category('tools')
tools.deposit(100)
tools.deposit(200, 'na drewno')
tools.deposit(50)
food = Category('food')
food.deposit(10000, 'wyplata jezyk lata jak lopata')
food.withdraw(200, 'zakupy')
tools.withdraw(100, 'cost of living')
tools.withdraw(260, 'szludzek')
food.transfer(100, 'tools')
electronics = Category('Electronics')
electronics.deposit(420, 'cash back')
electronics.withdraw(100, 'new coils')
electronics.withdraw(150, 'new screen')
electronics.transfer(120, 'tools')
#print(tools.ledger)
#print('tools ledger', tools.ledger)
print(food)
print(tools)
print(electronics)
print(create_spend_chart([food, tools, electronics]))
#print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
#call = food.__call__()
#print(food.__call__())
lista = globals().copy()
#print('lista items', lista.items())
#print(lista['food'].name)
# for x, y in lista.items():
#     if x == 'food':
#         print(y.__call__())

