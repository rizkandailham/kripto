import random
import string

class huruf():

    def besar():
        return "".join(random.sample(string.ascii_uppercase,random.randint(8,32)))

    def kecil():
        return "".join(random.sample(string.ascii_lowercase,random.randint(8,32)))

    def hex():
        return "".join(random.sample(string.hexdigits,random.randint(8,32)))
