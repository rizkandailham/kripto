import hashlib
from binascii import *
from base64 import *
from time import sleep
import pyotp
from pyotp import TOTP as phrase
import random
import string
class kripto_hash:
    #metode 1 penggunaan fungsi secara berurut
  def enc_traditional(self,kunci):
      message= hashlib.sha256()
      message.update(kunci.encode())
      return message.hexdigest()
    #metode 2 direct hashing
  def enc_sha256(self,kunci):
    return hashlib.sha256(kunci.encode()).hexdigest()
  def enc_sha224(self,kunci):
      return hashlib.sha224(kunci.encode()).hexdigest()
  def enc_sha512(self,kunci):
      return hashlib.sha512(kunci.encode()).hexdigest()
  def enc_386(self,kunci):
      return hashlib.sha385(kunci.encode()).hexdigest()
  def enc_sha3_224(self,kunci):
      return hashlib.sha3_224(kunci.encode()).hexdigest()
  def enc_sha3_256(self,kunci):
      return hashlib.sha3_256(kunci.encode()).hexdigest()
  def enc_sha3_384(self,kunci):
      return hashlig.sha3_384(kunci.encode()).hexdigest()
  def enc_sha3_512(self,kunci):
      return hashlib.sha3_512(kunci.encode()).hexdigest()

class secure_pass:
    def generate_pass(self):
        random.seed()
        return "".join(random.sample(string.ascii_letters, random.randint(10,16)))

    def generate_hex(self):
        seed="".join(random.sample(string.ascii_letters*3, random.randint(32,64)))
        random.seed(seed)
        return "".join(random.sample(string.hexdigits*4, random.randint(10,16)))

    def validate_blok(self,randpass):
        i=True
        while i==True:
            password=self.generate_pass()
            if randpass == password:
                print("ditemukan")
                i=False
    
class enkripsi:
  #membuat otp dari secret key
  def otp(key):
      return phrase(kunci).now()
  #fungsi untuk memvalidasi otp yg digenerate dari fungsi otp
  def otp(verif):
      return phrase(verif).verify()
  #membuat otp dengan format yang telah distandarisasi
  def otp_app(key,email,app_name):
      return phrase(key).provisioning_uri(name=email,issuer_name=app_name)
  #membuat random karakter sepanjang 32 character
  def generate_key():
      return pyotp.random_base32()
  #membuat secret key dengan format hex encoded string
  def generate_key_hex():
      return pyotp.random_hex()
  #mengubah hash menjadi base64
  def b64(self,kunci):
    enkrip=unhexlify(kunci)
    return b2a_base64(enkrip).decode()
  #melakukan decoding base64 ke hash awal
  def b64_decode(self,kunci):
    hex=b64decode(kunci)
    return hexlify(hex).decode()
  #dibuat untuk penjelasan
  def penjelasan(self,kunci):
    print("melakukan hash ke sha256")
    print("melakukan hexlify terlebih dahulu terhadap kunci")
    print(hexlify(kunci.encode()))
    sleep(5)
    print("hasil hexlify akan dilakukan hashing ke sha256")
    kunci=kripto.enc(self,kunci)
    sleep(5)
    print(kunci)
    sleep(5)
    print("melakukan encode ke base64")
    print("sebelumnya base64 dilakukan unhexlify terlebih dahulu")
    sleep(5)
    print(unhexlify(kunci))
    sleep(5)
    print("hasil encode sebagai berikut")
    kunci=kripto.b64(self,kunci)
    sleep(5)
    print(kunci)
    print("melakukan decode kembali ke sha256 ")
    sleep(5)
    print("hasil awal decode menggunakan library base64 adalah data yang masih unhexlify")
    print(b64decode(kunci))
    print("untuk itu dilakukan hexlify dan decode ke string dengan hasil sebagai berikut")
    kunci=kripto.b64_decode(self,kunci)
    print(kunci)
  #experiment only
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


if __name__ == "__main__":
    print("welcome do you need a coffe?")
