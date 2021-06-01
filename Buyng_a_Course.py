"""
Dictionary and Tuple activitie: A form to purchase a programming course
"""

# Course options

a = 'Python'
b = 'Java'
c = 'SQL'
d = 'C'

print("Please, select the course option:\n'a' for Python\n'b' for java\n'c' for SQL\n'd' for C")
course_choice = input('> ')

if course_choice not in ('a', 'b', 'c', 'd'):
    print('Invalid input')
    quit()
elif course_choice == 'a':
    course_choice = a
elif course_choice == 'b':
    course_choice = b
elif course_choice == 'c':
    course_choice = c
elif course_choice == 'd':
    course_choice = d


print("Please, select the session option:\n'e' for 8 a.m. \n'f' for 10 a.m.\n'g' for 2 p.m. \n'h' 7 p.m.")
session_choice = input('> ')

e = '8 a.m.'
f = '10 a.m.'
g = '2 p.m.'
h = '7 p.m.'

if session_choice not in ('e', 'f', 'g', 'h'):
    print('Invalid input')
    quit()
elif session_choice == 'e':
    session_choice = e
elif session_choice == 'f':
    session_choice = f
elif session_choice == 'g':
    session_choice = g
elif session_choice == 'h':
    session_choice = h

course_options = {f'Course': course_choice, 'Session': session_choice}

# Personal details

print("Please, enter your full name")
name = input('> ')

print("Please, enter your phone number")
contact = input('> ')

personal_details = {f'Name': name, 'Contact': contact}

# Payment details

bs = 'Bank Slip'
cc = 'Credit Card'
pp = 'PayPal'

print("Please, select the payment method:\n'bs' for bank slip. \n'cc' for credit card.\n'pp' for 2 paypal")
payment_method = input('>')

if payment_method not in ('bs', 'cc', 'pp'):
    print('Invalid input')
    quit()
elif payment_method == 'bs':
    payment_method = bs
elif payment_method == 'cc':
    print('Please. enter your credit card number')
    cc_number = input('> ')
    print('Please. enter your credit card password')
    cc_pw = input('> ')
    payment_method = cc
elif payment_method == 'pp':
    print('Please. enter your paypal number')
    pp_email = input('> ')
    payment_method = pp

if payment_method == bs:
    payment_details = {f'Payment Method': bs}
elif payment_method == cc:
    payment_details = {f'Payment Method': cc, 'Credit Card Number': cc_number, 'Credit Card Password': cc_pw}
elif payment_method == pp:
    payment_details = {f'Payment Method': pp, 'PayPal E-mail': pp_email}

print(course_options)
print(personal_details)
print(payment_details)
