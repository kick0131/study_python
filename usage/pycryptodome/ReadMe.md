## 内容
AES暗号化を行う、Python標準のPyCrypt派生ライブラリ
https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

## 準備
```
pip install pycryptodome
```

### [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
リスト内包表記でループ文を簡潔にするテクニック。

以下と同義
```.py
for x in (cipher.nonce, tag, ciphertext):
    file_out.write(x)
```

ちなみに、inの中の要素(cipher.nonce, tag, ciphertext)は左から順にxに評価される
