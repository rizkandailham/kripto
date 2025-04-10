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

#print(buat.s256("ilham rizkanda, S.Kom"))
"""
no=0
lop=False
while lop==False:

  if buat.s256(no) == "35803409c35e5cd3acd801517af64528c4a35c79e121fef83f5389294e8416ce":
    print("ditemukan pada ",no)
    print("hash yang dicari 597180d3039f1b7b7dde3ebdc56e13c698ef66dc18cf72ed61a4f79c8a904524")
    break
  else:
    no+=1
"""
#print(buat.s256(123423))
