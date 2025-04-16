import hashlib
from binascii import b2a_base64
from base64 import b64decode
from binascii import hexlify
import oracledb
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
