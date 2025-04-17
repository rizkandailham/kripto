import generate_hash
import kripadd

hashing=generate_hash.huruf()
hashing_file=kripadd.kripto_hash()
class hash_file:
    def write_file(self,file_name):
        file = open(file_name,'w')
        for i in range(0,99999):
            file.write(hashing.besar()+"\n")

    def write_hash(self,rand_str_file,hash_file):
        file=open(rand_str_file,'r')
        data=file.read().split("\n")
        file.close()
        file=open(hash_file,"w")
        for i in data:file.write(hashing_file.enc_sha256(i)+"\n")
        file.close()


if __name__ == '__main__':
    hash_file().write_file("Random_string.out")
    hash_file().write_hash("Random_string.out","hash.out")
