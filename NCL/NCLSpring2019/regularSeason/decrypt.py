# Python bytecode 2.7 (62211)
# Embedded file name: ./decryptor.py
# Compiled at: 2019-04-07 21:34:37
import os
from time import sleep
import datetime, base64
, hashlib
from Crypto import Random
from Crypto.Cipher import AES
now = datetime.datetime.now()
seed = int(now.strftime('%Y%m%d'))
random.seed(seed)
cryptoKey = str(random.randint(0, sys.maxint))
password = 'gooeyflubber'

class Cipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, input_filename, output_filename):
        chunk_size = 65536
        file_size = str(os.path.getsize(input_filename)).zfill(16)
        IV = ''
        for i in range(16):
            IV += chr(random.randint(0, 255))

        encryptor = AES.new(self.key, AES.MODE_CBC, IV)
        with open(input_filename, 'rb') as (inputfile):
            with open(output_filename, 'wb') as (outf):
                outf.write(file_size)
                outf.write(IV)
                while True:
                    chunk = inputfile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    else:
                        if len(chunk) % 16 != 0:
                            chunk += ' ' * (16 - len(chunk) % 16)
                    outf.write(encryptor.encrypt(chunk))

    def decrypt(self, input_filename, output_filename):
        chunk_size = 65536
        with open(input_filename, 'rb') as (inf):
            filesize = long(inf.read(16))
            IV = inf.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, IV)
            with open(output_filename, 'wb') as (outf):
                while True:
                    chunk = inf.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    outf.write(decryptor.decrypt(chunk))

                outf.truncate(filesize)


cipher = Cipher(cryptoKey)

def write(string):
    sys.stdout.write(string)
    sys.stdout.flush()


def blink(times):
    while times > 0:
        write('.')
        sleep(0.53)
        times -= 1


def verify(text):
    return text == password


if len(sys.argv) != 1:
    print 'Usage: python decryptor.pyc'
    exit(1)
write('H4ckp0t Jakp0t F1ag St0rag3> Connecting to Datastore')
blink(3)
write('\n')
guess = raw_input('H4ckp0t Jakp0t F1ag St0rag3> Enter your decryption password: ')
write('H4ckp0t Jakp0t F1ag St0rag3> Validating')
blink(3)
if verify(guess):
    write('Correct\n')
    src = raw_input('H4ckp0t Jakp0t F1ag St0rag3> Specify encrypted directory: ')
    dst = raw_input('H4ckp0t Jakp0t F1ag St0rag3> Specify output directory: ')
    for r, d, files in os.walk(src):
        for filename in files:
            print filename
            cipher.decrypt(src + filename, dst + filename)

else:
    write('Incorrect. Encrypting hard drive\n')
    blink(3)
    sys.exit(1)
