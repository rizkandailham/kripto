import random
import string

class huruf():

    def besar(self):
        return "".join(random.sample(string.ascii_uppercase,random.randint(8,26)))

    def kecil(self):
        return "".join(random.sample(string.ascii_lowercase,random.randint(8,26)))

    def hex(self):
        return "".join(random.sample(string.hexdigits,random.randint(6,9)))
