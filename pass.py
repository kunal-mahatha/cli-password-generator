import string
import random

k1 = string.ascii_lowercase
k2 = string.ascii_uppercase
k3 = string.digits
k4 = string.punctuation

p = []
p.extend(k1)
p.extend(k2)
p.extend(k3)
p.extend(k4)

random.shuffle(p)

service = input("Where do you want to use your password : ")

len = int(input("Enter password length : "))

pd = p[:len]

password = "".join(pd)

print(f"Your Password for {service} is : {password}")