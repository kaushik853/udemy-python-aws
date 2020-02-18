from random import choice
len_of_pass = 11


valid_pass_option = "QWERTYUIOPASDFGHJKLZXCVBNMqazwsxedcrfvtgbyhnujmikolp0123456789!@#$%^&*()?"
password = []

for i in range(len_of_pass):
    password.append(choice(valid_pass_option))

random_pass = "".join(password)


print(random_pass)