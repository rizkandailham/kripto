#export requirement dengan pip freeze > requirements.txt
#inilah pentingny pakek venv biar nggak kebanyakan install lib
import pyshorteners
import flask
import json
import hashlib
import string

class web:
    def pendek(link):
        objek=pyshorteners.Shorteners()
        return objek.tinyurl.short(link)
    def acak_tanpa_prase():
        length=random.randint(8,16)
        s=string.ascii_letters+string.punctuation
        return "".join(random.sample(s,length))

    def acak(panjang,phaseprase):
        random.seed(phaseprase)
        s=string.ascii_letters+string.punctuation
        return "".join(random.sample(s,panjang))
class web_server:
    def input_password(self,pass):
        return hashlib.sha256(pass.encode()).hexdigest()

    def validasi(self,hash,pass):
        valid=False
        if hash==hashlib.sha256(pass.encode()).hexdigest():
                valid=True
        return valid

    def reset_password(self,phaseprase):
        return web.acak(8,phaseprase)

    def buat_password_random(self,phaseprase):
        return web.acak(random.randint(8,16),phaseprase)

    def registrasi(self):
    #gabut bro wkwkwk lum ketemu yg mood untuk disimpen di database atau kek gimana
    def login(self,username,password):
        validate=False
        length=random.randint(8,16)
        s=string.ascii_letters+string.punctuation
        seed=random.random_sample(s,length)
        if hashlib.sha256(username.encode()).hexdigest==hashlib.sha256(acak(length,seed).encode()).hexdigest():
            if hashlib.sha256(password.encode()).hexdigest() == hashlib.sha256(acak(16,"pass").encode()).hexdigest():
                validate=True
        return validate

    def mining(self):

    def exchange(self):

    def simpan_hasil_mining_data(self):

    def start_mining(self):

    def pilih_algoritma_hashing(self):

    def masukan_phaseprase(self):

    def authenticator_google(self):

    def multifactor_authenticator(self):

    def proses_regression(self):

    def proses_classification(self):
