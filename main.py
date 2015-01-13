#!/usr/bin/env python3

import sys


class Menu(object):
    def __init__(self, user):
        self.user = user

        self.menu_item = {"1": self.query, "2": self.deposit,
                          "3": self.withdraw, "4": self.transaction}

        print("Willkommen {}".format(self.user))

    def show_menu(self):
        while True:
            picked_item = input("Wähle eine option\
            \n 1. Kontostand abfragen\n 2. Geld einzahlen\n 3. Geld abheben\n"
                                " 4. Überweisung\n 5. Logout\n")
            check_input(picked_item, 1)

            if picked_item == "5":
                break

            try:
                self.menu_item[picked_item]()
            except KeyError:
                print("Invalid Entry, please choose one entry from the menu")

    def query(self):
        konto[self.user].query()

    def deposit(self):
        try:
            amount = int(input("Wieviel möchten Sie einzahlen?: "))
        except ValueError:
            print("Whoops, this should be a number!\nTry again")
            self.deposit()
        else:
            konto[self.user].deposit(amount)

    def withdraw(self):
        try:
            amount = int(input("Wieviel möchten Sie abheben?: "))
        except ValueError:
            print("Whoops, this should be a number!\nTry again")
            self.deposit()
        else:
            konto[self.user].withdraw(amount)

    def transaction(self):
        receiver = int(input("Wählen Sie einen Empfänger\n "
                             "1. dennis\n 2. nils "))

        try:
            amount = int(input("Wieviel möchten Sie überweisen?: "))
        except:
            print("gtfo")
        else:
            konto[self.user].transaction(userlist[receiver - 1], amount)


class Account(object):
    def __init__(self, user):
        self.user = user
        self.balance = 0

    def query(self):
        print("{}'s actual Account balance is {}".format(
            self.user, self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("Ihr neuer Kontostand beträgt {}".format(self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        print("Ihr neuer Kontostand beträgt {}".format(self.balance))

    def transaction(self, receiver, amount):
        self.balance -= amount
        konto[receiver].balance += amount
        print("Nach der Überweisung ist Ihr neuer Kontostand: {}".format(
            self.balance))


def login():
    maxtries = 3

    while maxtries != 0:
        pin = input("Enter PIN: ")
        if not check_input(pin, 4):
            continue
        if pin in pins:
            m = Menu(pins[pin])
            m.show_menu()
            break
        else:
            print("PIN falsch, versuchen Sie es erneut ")
            maxtries -= 1
    if maxtries == 0:
        while True:
            try:
                puk = input("you fucked it up, maybe you got a PUK?")
            except ValueError:
                print("Well, you have to type 4 digits, no bullshit")
            if puk in puks:
                print("Alright {}, your PIN is {}".format(puks[puk],
                                                          users[puks[puk]]))
                break


def check_input(user_input, chars):
    if len(user_input) != chars:
        print("Invalid Input, Input must be {} characters long".format(chars))
        return False
    elif not user_input.isdigit():
        print("Invalid Input, Input must be digit/s only")
        return False
    else:
        return True


if __name__ == '__main__':
    konto = {}
    users = {"dennis": "1234", "nils": "2345"}
    pins = {"1234": "dennis", "2345": "nils"}
    userlist = ["dennis", "nils"]
    puks = {"0815": "dennis", "0816": "nils"}
    for user in users:
        konto[user] = Account(user)

    while True:
        option = None
        try:
            option = int(input("Choose an option\n 1. Login\n 2. Quit\n"))
        except ValueError:
            print("Invalid Input, please choose an option from the menu")
        if option == 1:
            login()
        elif option == 2:
            sys.exit()
        else:
            print("Invalid Input, please choose an option from the menu")