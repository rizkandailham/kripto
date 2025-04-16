import random
import kripadd
import hashlib

hashing=kripadd.kripto_hash()

class guessing:
    def rand_number(self):
        random.seed()
        return random.randint(1,100)

    def passive_guess(self,randnum):
        guess=None
        randnum=hashing.enc_sha256(randnum)
        while randnum!=guess:
            guess=input("Show me your guess lucky number : ")
            guess=hashing.enc_sha256(str(guess))
        print("Congrats you get the number!")

    def dynamic_guess(self):
        random.seed()
        randnum=self.rand_number()
        guess=None
        while randnum!=guess:
            guess=input("Show me your guess lucky number: ")
            guess=hashing.enc_sha256(str(guess))
            randnum=hashing.enc_sha256(str(self.rand_number()))
            #print(randnum)
            #print(guess)
if __name__ == "__main__":
    play=guessing()
    play.guessor(play.rand_number())
