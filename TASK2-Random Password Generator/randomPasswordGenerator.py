import random

number_of_passwords = int(input("ENter the number of passwords required: "))
password_length = int(input('Enter the passsword lengthb (min 4): '))

capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
punctuations = "~!@#$%^&*()_+=-|/.,><?;':"

for j in range(number_of_passwords):

    password = random.choice(capital_letters) + random.choice(small_letters) + random.choice(digits) + random.choice(punctuations)
    
    for i in range(4,password_length):
        password = password + random.choice(capital_letters+small_letters+digits+punctuations)

    print(f"Password {j} is: "+''.join(random.sample(password, len(password))))