# -*- coding: utf-8 -*-
from Crypto.Cipher import AES

# 自作パッケージ
from basic.logutil.logutil import LogUtil

logger = LogUtil.getlogger(__name__)

key = b"seed012345678901"


@LogUtil.insertfunclog
def encrypt():
    # keyは16バイト以上
    data = b"secret password"
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    logger.info(f'text:{ciphertext}')
    logger.info(f'tag :{tag}')
    #
    logger.info(f'nonce:{cipher.nonce}')

    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()


@LogUtil.insertfunclog
def decrypt():
    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # byte to str
    logger.info(f'data: {data.decode()}')


if __name__ == '__main__':
    encrypt()
    decrypt()
