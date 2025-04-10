import hashlib
from binascii import *
from base64 import *


class kripto:
  def enc(self,kunci):
    return hashlib.sha256(kunci.encode()).hexdigest()

  def b64(self,kunci):
    enkrip=unhexlify(kunci)
    return b2a_base64(enkrip).decode()
  def b64_decode(self,kunci):
    hex=b64decode(kunci)
    return hexlify(hex).decode()
  def penjelasan(self,kunci):
    print("melakukan hash ke sha256")
    print("melakukan hexlify terlebih dahulu terhadap kunci")
    print(hexlify(kunci.encode()))
    print("hasil hexlify akan dilakukan hashing ke sha256")
    kunci=kripto.enc(self,kunci)
    print(kunci)
    print("melakukan encode ke base64")
    print("sebelumnya base64 dilakukan unhexlify terlebih dahulu")
    print(unhexlify(kunci))
    print("hasil encode sebagai berikut")
    kunci=kripto.b64(self,kunci)
    print(kunci)
    print("melakukan decode kembali ke sha256 ")
    print("hasil awal decode menggunakan library base64 adalah data yang masih unhexlify")
    print(b64decode(kunci))
    print("untuk itu dilakukan hexlify dan decode ke string dengan hasil sebagai berikut")
    kunci=kripto.b64_decode(self,kunci)
    print(kunci)
  def perulangan(self,kunci):
    i=1
    found=False
    for i in range(0,1000000000000,1):
        if kripto.enc(self,str(i))[-6::] == kripto.enc(self,kunci)[-6::]:
            print("ditemukan pada ",i)
            found=True
            break

    if found == False :
        print("tidak ditemukan blok yang sama")
