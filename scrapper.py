import pyshorteners


class web:
    def pendek(link):
        objek=pyshorteners.Shorteners()
        return objek.tinyurl.short(link)

    def acak(panjang,phaseprase):
        random.seed(phaseprase)
        s="qwertyuiopasdfghjkl;'[]\1234567890-=!@#$%^&*(()QWERTYUIOPASDFGHJKLZXCVBNM<>?:{{}}123456789+-"
        return "".join(random.sample(s,panjang))
