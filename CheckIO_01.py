#The password will be considered strong enough if its length is greater than or equal to 10 symbols,
#  it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
#  The password contains only ASCII latin letters or digits.
#Input: A password as a string.

# Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
# In the results you will see the converted results.
# How it is used: If you are worried about the security of your app or service, you can check your users' passwords for complexity.
# You can use these skills to require that your users passwords meet more conditions (punctuations or unicode).

#Precondition:
#re.match("[a-zA-Z0-9]+", password)
#10 < len(password) ≤ 64


import re
password = input("Введите пароль не менее 10 символов и не более 64")
if 10 <= len(password) <= 64:
    if re.match("[a-zA-Z0-9]+", password):
        if re.search("[a-z]+", password) and re.search("[A-Z]+", password) and re.search("[0-9]+", password):
            print('Вы ввели корректный пароль.')
            passw = True
        else:
            print('Неправильный пароль')
            passw =  False
    else:
        print('неправильный пароль!')
        passw = False
else:
    print('неправильный пароль!')
    passw = False
print(bool(passw))
