import random
n=int(input('введите длину пароля'))
d=int(input('если вы хотите составить пароль только из чисел, введите "1";'
            'если только из букв, введите "2";'
            'если только из знаков, введите "3";'
            'если из чисел и букв, введите "12";'
            'если из букв и знаков, введите "23";'
            'если из чисел и знаков, введите "13"'
            'если из чисел, букв и знаков, введите "123";'))
numbers="0123456789"
letters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
signs="§±!@#$%^&*()_+-={}[]|`~/?><,.№"
numbersandletters="012345678qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
lettersandsigns="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM§±!@#$%^&*()_+-={}[]|`~/?><,.№"
numbersandsigns="0123456789§±!@#$%^&*()_+-={}[]|`~/?><,."
all="012345678qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM§±!@#$%^&*()_+-={}[]|`~/?><,.№"
password=""
for i in range(n):
    if d==1:
        a=random.choice(numbers)
        password+=a
    if d==2:
        a=random.choice(letters)
        password+=a
    if d==3:
        a=random.choice(signs)
        password+=a
    if d==12:
        a=random.choice(numbersandletters)
        password+=a
    if d==23:
        a=random.choice(lettersandsigns)
        password+=a
    if d==13:
        a=random.choice(numbersandsigns)
        password+=a
    if d==123:
        a=random.choice(all)
        password+=a
print(password)
