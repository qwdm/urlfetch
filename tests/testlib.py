import random
import string

def randstr(l=None, chars=string.ascii_letters+string.digits):
    l = l or random.randint(1, 100)
    return ''.join(random.choice(chars) for i in xrange(l))


randint = random.randint
