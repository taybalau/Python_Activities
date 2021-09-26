import pandas as pd

df = pd.read_excel('data.xlsx')  # Registered user data
#print(df)
df_size = len(df)  # Dataframe size
access = False


class User:

    counter = df['number'][df_size-1] + 1  # The bank account number generator

    def __init__(self, first_name, last_name, cpf, password, balance):
        self.number = User.counter  # Bank account number
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.password = password
        self.balance = balance

    def add_money(self, value):
        """This function performs operations such as: deposit in its own account or bank transfers received"""
        balance = self.balance + value
        return balance

    def withdraw_money(self, value):
        """This function performs operations such as: withdrawals or bank
        transfers to other users registered at the bank """
        balance = self.balance - value
        return balance


def check_cpf(df, cpf):
    """Function that checks if a CPF is already registered in the database.
    If so, the function returns True. If not, the function returns False.
    The parameters passed are: df(data frame, that is, the database)
    and the cpf entered for registration by the user"""
    cpf_list = list(df['cpf'])
    if cpf in cpf_list:
        return True
    return False

menu_choice = input(

    'Choose an option:\n' 
    '1 - Create an Account.\n'
    '2 - Access Account.\n'
)

if menu_choice == '1':
    print('Create an Account...')
    firstname = input('Enter your first name: ').capitalize()
    lastname = input('Enter your last name: ').capitalize()
    cpf1 = input('Enter the first nine digits of your CPF: ')
    cpf2 = input('Enter the last two digits of your CPF: ')

    # Existence Conditions for CPF Registration:
    # (it needs to have twelve whole numbers and cannot be registered in the database)
    try:
        cpf_test1 = int(cpf1)
        cpf_test2 = int(cpf2)
    except:
        print('Invalid CPF. Try again.')
        quit()

    cpf = f'{cpf1}-{cpf2}'

    if len(cpf) != 12:
        print('Invalid CPF. Try again.')
        quit()

    test = check_cpf(df, cpf)
    if test:
        print('Account already registered in this CPF.')
        quit()

    balance = input('Enter your balance: ')
    password = input('Enter your password: ')
    verify_password = input('Confirm your password: ')

    while password != verify_password:
        print('Confirmation does not match. Try again.')
        password = input('Enter your password: ')
        verify_password = input('Confirm your password: ')

    user1 = User(firstname, lastname, cpf, password, balance)
    df.loc[df_size] = list((user1.__dict__).values())
    # The former line puts the information to registration entered by the user into the DataFrame.
    print(f'Account created successfully. Your account number is: {user1.number}')
elif menu_choice == '2':
    print('Access account...')
    a_cpf = input('CPF: ')
    a_password = input('Password: ')
    cpf_list = list(df['cpf'])
    a_cpf = a_cpf[:9] + '-' + a_cpf[9:]  # Adds the '-' character before the CPF check digits

    if a_cpf in cpf_list:  # Checks if the CPF entered by the user is registered
        p = cpf_list.index(a_cpf)  # CPF position entered in the database
        if a_password == df['password'][p]:  # Checks if the password entered matches with the CPF
            access = True
            print('Access granted.')
        else:
            print('Access denied. Wrong password.')
    else:
        print('Access denied. CPF not registered.')
else:
    print('Unrecognized option.')


if access:
    user2 = User(df['first_name'][p], df['last_name'][p], df['cpf'][p], df['password'][p], df['balance'][p])
    print(f'You are logging in as {user2.first_name} {user2.last_name}...')
    menu_choice2 = input(

        'Chose an Option:\n'
        '1 - Check balance\n'
        '2 - Make a deposit\n'
        '3 - Withdraw\n'
        '4 - Transfer\n'
        '5 - Cancel\n'
    )
    while menu_choice2 != '5':
        if menu_choice2 == '1':
            print(f'Your current balance is R$ {user2.balance}')
        elif menu_choice2 == '2':
            value = float(input('Enter the amount you want to deposit into your account: '))
            balance = user2.add_money(value)
            print(f'Deposit successful. Your balance is now R$ {balance}')
            df.loc[p, 'balance'] = balance  # Update the database
        elif menu_choice2 == '3':
            value = float(input('Enter the amount you want to withdraw: '))
            balance = user2.balance
            if value > float(balance):
                print(f'Insufficient funds. Unable to perform the operation.')
            else:
                balance = user2.withdraw_money(value)
                print(f'Successful withdrawal. Your balance is now R$ {balance}')
                df.loc[p, 'balance'] = balance
        elif menu_choice2 == '4':
            deposit_account = int(input('Enter the account number you want to transfer to: '))
            list_number_accounts = list(df['number'])
            for account in list_number_accounts:
                if account == deposit_account:  # Checks if the account entered by the user is in the Database
                    p2 = list_number_accounts.index(account)
                    # p2 is the position in the database of the user indicated to receive the transfer
                    user3 = User(df['first_name'][p2], df['last_name'][p2], df['cpf'][p2], df['password'][p2],
                            df['balance'][p2])
                    answer = input(f'The account you want to deposit is from {user3.first_name} {user3.last_name}? '
                                   f'(y/n)\n')
                    if answer == 'y':
                        value = float(input(f'What amount do you want to transfer to {user3.first_name} '
                                        f'{user3.last_name}? '))
                        balance = user2.balance
                        if value > float(balance):
                            print('Insufficient funds. Unable to perform the operation.')
                        else:
                            balance2 = user3.add_money(value)
                            df.loc[p2, 'balance'] = balance2
                            balance1 = user2.withdraw_money(value)
                            df.loc[p, 'balance'] = balance1
                            print(f'Operation performed successfully. Your balance is now R$ {balance1} ')
                    elif answer == 'n':
                        print('Try again.')
                    else:
                        print('Option not recognized.')
        else:
            print('Option not recognized.')
        menu_choice2 = input(

            'Chose an Option:\n'
            '1 - Check balance\n'
            '2 - Make a deposit\n'
            '3 - Withdraw\n'
            '4 - Transfer\n'
            '5 - Cancel\n'
        )
    if menu_choice2 == '5':
        print('Operation canceled successfully.')


df.to_excel('data.xlsx', index=False)

# print(df)