# Stefan Bordei 2021
# Shared expenses tracking and management system.


import sys


class Member:
    """
    Class constructor for members.
    
    :param name: identifier.
    :param balance: initialized with the value 0.
    
    """
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def print_balance(self):
        print("%s has balance: €%.2f" % (self.name, self.balance))


class Transaction:
    """
    Class for each transaction.
    
    :param name: identifier.
    :param amount: int/float.
    :param payee: Member identifier.
    
    """
    def __init__(self, name, amount, payee):
        self.name = name
        self.amount = amount
        self.payee = payee


class Event:
    def __init__(self, name, members):
        """
        This is a class for events tracking transactions of participating members.
        
        :param name: identifier
        :param members: list, participating members
        
        """
        self.name = name
        names = []
        for member in members:
            names.append(member.name)
        if len(set(names)) < len(members):
            sys.exit("A member name is added more than once.")

        self.members = members
        self.transactions = []
        self.amount = 0

    def add_transaction(self, name, amount, payee):
        
        # Before adding a transaction check:
        # -the payee is an event participant
        # -the amount entered is a positive number
        
        try:
            val = round(float(amount), 2)
            if val <= 0:
                raise ValueError("Negative amount:", val)
            if payee not in self.members:
                raise NameError("Payee not an event participant.")

            transaction = Transaction(name, val, payee)
            self.transactions.append(transaction)
            self.amount += val
            per_member = val / len(self.members)
            for member in self.members:
                if payee == member:
                    member.balance += (val - per_member)
                else:
                    member.balance -= per_member
        except Exception as e:
            print("Transaction error: {}".format(e))
            print("Skipping transaction...")

    def print_balance(self):
        reconcile_val = self.amount / len(self.members)
        print("Total: €%.2f, that is €%.2f each." % (self.amount, reconcile_val))
        print()
        for m in self.members:
            m.print_balance()

    def reconcile(self):
        self.print_balance()
        print()

        for x in self.members:
            if x.balance <= 0:
                continue

            for y in self.members:
                if y.balance > 0:
                    continue

                amount = min(-y.balance, x.balance)
                if amount == 0:
                    continue
                print('{} pays {} €{:.2f}'.format(y.name, x.name, amount))
                y.balance += amount
                x.balance -= amount


# Template:

annie = Member('Annie')
sally = Member('Sally')
bill = Member('Bill')

concert = Event('Concert', [annie, bill, sally])
concert.add_transaction('tickets', 180, annie)
concert.add_transaction('dinner', 75, sally)
concert.add_transaction('drinks', 19, bill)
concert.add_transaction('taxi', 16, bill)

concert.reconcile()
