import hashlib
from binascii import b2a_base64
from base64 import b64decode
from binascii import hexlify
class sandi:
  def s256(self, kunci):
    blok=str(kunci).encode()
    return hashlib.sha256(blok).hexdigest()

  def s1(self,kunci):
    blok=str(kunci).encode()
    return hashlib.sha1(blok).hexdigest()
  def encode_64(self,kunci):
    return b2a_base64(bytes.fromhex(kunci)).decode("ascii")
  def decode_64(self, kunci):
    dec=b64decode(kunci)
    dec=hexlify(dec)
    return dec.decode("ascii")
  def koneksi_lokal(user,pass):
      d=r"C:\Users\disdukcapil_adb\github\kripto\instantclient_23_7"
      oracledb.init_oracle_client(lib_dir=d)
      connection=oracledb.connect(user=user,password=pass, host="10.16.7.23",port=1521,service_name="local")
      hubung=connection.cursor()
      hubung.execute("select nik from demographics")
      #keluarkan hasil eksekusi seluruhnya fetchall()
      array=[]
      for i in hubung.fetchall()
        array.append(i)
      #metode 2 menggunakan fetchone()
      #hasil eksekusi di tarik 1 per 1 disimpan di dalam array

      while True:
          row=cursor.fetchone()
          array.append(i)
