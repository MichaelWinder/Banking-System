class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def display_info(self):
        line("-", 25)
        print("Name: ", self.first_name, self.last_name)
        print("Gender: ", self.gender)
        print("Address: ", self.street_address, self.city)
        print("Email: ", self.email)
        print("Credit Card number: ", self.cc_number, "Type:", self.cc_type)
        print("Balance: ", self.balance)
        print("Account number: ", self.account_no)
        line("-", 25)


def line(symbol, length: int):
    print(symbol * length)


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8]), line[9])


def findUser(text):
    u_name = input(text).title()
    found_users = False
    for user_object in userList:
        if user_object.first_name + " " + user_object.last_name == u_name:
            found_users = True
            user_object.display_info()
    if not found_users:
        print(f"There are no Users with the name {u_name}")


def overdrafts():
    count = 0
    total_overdraft = 0
    for user_object in userList:
        if user_object.balance < 0:
            print(user_object.first_name, user_object.last_name,
                  f": ${user_object.balance}")
            total_overdraft += user_object.balance
            count += 1
    print(f"There are {count} user(s) that have an overdue balance, "
          f"there is a total overdraft of ${total_overdraft * -1:.2f}")


def missingEmails():
    count = 0
    for user_object in userList:
        if user_object.email == "":
            print(user_object.first_name, user_object.last_name)
            count += 1
    print(f"There are {count} user(s) that haven't set an email for their "
          f"account")


def bankDetails():
    count = 0
    bank_total_worth = 0
    highest_balance = ["x", 0]
    lowest_balance = ["x", 0]
    for user_object in userList:
        count += 1
        bank_total_worth += user_object.balance
        if user_object.balance > highest_balance[1]:
            highest_balance[0] = user_object.first_name + " " + \
                                 user_object.last_name
            highest_balance[1] = user_object.balance
        if user_object.balance < lowest_balance[1]:
            lowest_balance[0] = user_object.first_name + " " + \
                                user_object.last_name
            lowest_balance[1] = user_object.balance
    print(f"The bank has {count} user(s) and has a total worth of "
          f"${bank_total_worth:.2f}.\nThe user with the highest balance is "
          f"{highest_balance[0]} with ${highest_balance[1]:.2f} and the user "
          f"with the lowest balance is {lowest_balance[0]} with $"
          f"{lowest_balance[1]:.2f}")


def transfer():
    acc_number = input("Enter the account number that you want to send "
                       "money from: ")
    for user_object in userList:
        if acc_number == user_object.account_no:
            user_object.display_info()
            amount = float(input("Enter the value you would like to send: "))
            while amount > user_object.balance:
                amount = float(input("Error incorrect amount\nEnter the value "
                                     "you would like to send: "))
            acc_number_send = input("Enter the account number that you "
                                    "want to send money to: ")
            for user_object_2 in userList:
                if acc_number_send == user_object_2.account_no:
                    user_object_2.display_info()
                    user_object.balance -= amount
                    user_object_2.balance += amount
                    user_object.display_info()
                    user_object_2.display_info()


userList = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ").upper()
    print()

    if userChoice == "1":
        findUser("Enter the name of the user you would like to search "
                 "for (first and last name): ")
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()
