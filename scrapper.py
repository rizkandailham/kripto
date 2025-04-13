import pyshorteners
import flask
import json
import hashlib

class web:
    def pendek(link):
        objek=pyshorteners.Shorteners()
        return objek.tinyurl.short(link)
    def acak_tanpa_prase():
        s="qwertyuiopasdfghjkl;'[]\1234567890-=!@#$%^&*(()QWERTYUIOPASDFGHJKLZXCVBNM<>?:{{}}123456789+-"
        return "".join(random.sample())

    def acak(panjang,phaseprase):
        random.seed(phaseprase)
        s="qwertyuiopasdfghjkl;'[]\1234567890-=!@#$%^&*(()QWERTYUIOPASDFGHJKLZXCVBNM<>?:{{}}123456789+-"
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

    def login(self,username,password):
        validate=False
        if hashlib.sha256(username.encode()).hexdigest==hashlib.sha256(acak(16,"leetme").encode()).hexdigest():
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
