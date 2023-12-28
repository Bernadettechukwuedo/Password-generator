import random
from string import ascii_letters, digits

# declare your variables
length = int(input("Enter the length of password: "))
print("On the next questions, answer either yes or no")
string1 = input("Should it contain alphabet: ").upper()
digit = input("Should it contain digits and symbols: ").upper()
symbols = "?'@#%^&*"
digits = digits + symbols
count = 0

while count != length:
    if string1 == "YES":
        if digit == "YES":
            alpha = ascii_letters + digits
        else:
            alpha = ascii_letters

    if string1 == "NO":
        if digit == "YES":
            alpha = digits
        else:
            print("No choice selected")
            break

    output = random.choice(alpha)
    count += 1

    print(output, end="")
