import random

class guessing:
    def rand_number(self):
        random.seed()
        return random.randint(1,100)

    def passive_guess(self,randnum):
        guess=None
        while randnum!=guess:
            guess=input("Show me your guess lucky number : ")
        print("Congrats you get the number!")

def dynamic_guess(self):
        randnum=self.rand_number()
        guess=None
        while randnum!=guess:
            guess=input("Show me your guess lucky number: ")
            randnum=rand_number()
if __name__ == "__main__":
    play=guessing()
    play.guessor(play.rand_number())
