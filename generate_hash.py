import random
import string

class huruf():

    def besar(self):
        return "".join(random.sample(string.ascii_uppercase,random.randint(8,26)))

    def kecil(self):
        return "".join(random.sample(string.ascii_lowercase,random.randint(8,26)))

<<<<<<< HEAD
    def hex():
        return "".join(random.sample(string.hexdigits,random.randint(8,32)))
if __name__ == '__main__':
    print("Silahkan jadikan module!")
=======
    def hex(self):
        return "".join(random.sample(string.hexdigits,random.randint(6,9)))
>>>>>>> ff2c3e5c73229084b38dd031c6412c2aaae58323
