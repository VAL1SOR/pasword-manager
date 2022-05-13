import random 
import string

def get_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

print(get_random_string(20))