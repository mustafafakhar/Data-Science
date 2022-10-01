
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%&"

code = lower_case + upper_case + number + symbol
length = 9
temp = random.sample(code, length)

password = "".join(temp)

print("Your password is", password)

#Another method is you can use random.sample() in the password function
