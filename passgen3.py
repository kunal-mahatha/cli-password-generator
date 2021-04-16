import string
import random
import argparse
import sys

parser = argparse.ArgumentParser(description="Password Generator")
parser.add_argument('-s', '--service', type = str, help = "Name of the Website where u want to use it", default='Facebook')
parser.add_argument('-l', '--len', type = int, help = "Length of the Password", default=8)
args = parser.parse_args()

def passgen(service, len):
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

    pd = p[:len]

    password = "".join(pd)

    print(password)

    file = open("passwords.txt", 'a')
    file.write(service)
    file.write(" : ")
    file.write(password)
    file.write('\n')
    file.close
    

if __name__ == '__main__':
    passgen(args.service, args.len)
