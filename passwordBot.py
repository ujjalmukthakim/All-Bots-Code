import string
import secrets

def MakePassword(size):
    charecters=(
        string.ascii_letters+
        string.digits+
        string.punctuation
    )
    password=''
    for i in range(size):
        password+=secrets.choice(charecters)
    return password

print(MakePassword(10))
