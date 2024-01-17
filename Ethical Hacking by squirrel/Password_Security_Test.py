import random
import string

def crack_password(password):
    attempts = 0
    while True:
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
        attempts += 1
        if guess == password:
            return attempts

password = input("Enter the password to crack: ")
print("Cracking password...")

attempts = crack_password(password)

print("The password was cracked in " + str(attempts) + " attempts.\nThe more attempts it took, the longer it took means the more secure the password was.")