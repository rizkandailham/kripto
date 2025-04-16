import random
import collections

class dice:
    def rolling(self):
        random.seed()
        return random.randint(1,6)

    def start(self):
        freq=[]
        for i in range(0,100):
            freq.append(dice().rolling())

        return freq


if __name__ == '__main__':
    play=dice()
    hasil=collections.Counter(play.start())
    print("Frequensi ny sebagai berikut: ")
    for i in hasil:
        print(i)
