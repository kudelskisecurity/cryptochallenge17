# Kudelski Security Crypto Challenge 

[serve_sign.py](serve_sign.py) is a service running on host 213.244.194.155. It
calls the binary [sign](sign) in order to sign a message.

[serve_verify.py](serve_verify.py) is another service running on host
213.244.194.155. It verifies the signature of a message using the
[verify](veirfy) binary.

To solve the challenge, you must write a program that creates valid
signatures, which will be successfully verified by the verification
service. Obviously, your program should not just copy a signature
received from the signing service.

Prizes will have to be claimed at our party in Las Vegas, the evening
before the Black Hat briefings: 5 ETH, 3 ETH, and 2 ETH the the first,
second, and third winner. The ranking is established on the time of your
submission, to our email address <a
href="mailto:cryptochallenge@kudelskisecurity.com">cryptochallenge@kudelskisecurity.com</a>.
We recommend that you encrypt your message, using the following public
key:

```

-----BEGIN PGP PUBLIC KEY BLOCK-----
mQENBFlLgVABCADvD+n2XJ2+6oYCHYdJOkiyf4+cWwy4ovZSwaL9PbwrRUfgk/Zk
SwahAcd7QXY6XEmghvs0pINLbYIU3UaGDX6mMwq5bGPoz4WOQyGs4RzS6onw4FP1
g76Bh7K6Hm4VlZtP/KAlV7XyslL8rgrWOihvfGfExxKWVG5wzoIdfkCAINyFmF5b
sUUr4ZcXrK2NpQFT04VMRvyVvOwEaNL0CrHGeieKhS/79pMYDmDejdEUhxzvc09P
6qfRGl+zfyCVPYu65JKCbU2XXj68hak6tI5yjG3hk4VzvIUWOdM+4iHD7N9zAECd
zI8CLgFeuhH/Zo5ns9QSMUb16wZiauogf7q1ABEBAAG0N0NyeXB0byBjaGFsbGVu
Z2UgPGNyeXB0b2NoYWxsZW5nZUBrdWRlbHNraXNlY3VyaXR5LmNvbT6JATkEEwEI
ACMFAllLgVACGwMHCwkIBwMCAQYVCAIJCgsEFgIDAQIeAQIXgAAKCRDLvccLD8oU
cTb+B/9b0WhOgE0wzX2kd4p9XFxpe6jLvdkkAnwDTpWrTWVTlA9j7MyookBvHntM
YHMAnIxgij/cRp41iSu0Bf34t9xi+/rQD4oivd88TgdyFIvMBN7qNH0Ob4mANVp9
I58FW7/Zp8yHmtdai1fLLUNhoke9LHnTALqkey2uNBR6ivMBG4mrppNXGLWUUplO
EgS6itDH3itecWOGlMc1Dajofk1YcSDW2ShXkFCuEFoBdRmF+D1H6YPmrZA/IJdK
/wGRQCbPo4C7v8c1Q7ZYYJA0Wo0vtWVcF8L0XI5vucL7cm9NjQHn7O5wskU/SD3b
4aPnBOCWMHsD3SpSSmHtsW1Sv1YYuQENBFlLgVABCADBa7lv5LgjBr1jb4GCjDLN
SCroRo/vu5m9T2Tcim3ENp1mJFdaAqtJsTxfySLgDCCFXLSbsRnyXoE7+iOUNdw2
b2l+5GHRJ/uOspPr2VNsJbkaWXWM/s9YBnIwiUceD6ztFZ7SVH0pHhZgBvJ/PKHd
yScAKqRy9wohle3fUfsjngEM1DgAFXhAs6rv+WUKMslOTDuvNblwKVsIomeOYrJG
ajiu6be283ZXp/LyJA6LAsGoclkC7kSy7AhaeJVdXUuLnbvnM/d/tIqqtSXU/KhT
F267YVZtinXDbpJohlUQqPkCXdX675h6GezeJkmVStifXr7/BEIRDEBOvdc3jFWN
ABEBAAGJAR8EGAEIAAkFAllLgVACGwwACgkQy73HCw/KFHGmIgf/elTH1oyptN5L
tzg278SzRR09v259P2+kxskxKqxgY0wohcUctXH/uPKFFUeFvZCxTfOOoVeCP4It
jxBq6gOWM6svynehEvML+bEjlPTlDNc5W1L1zD8qjHjiMV+a9gX9cyrrqCea1JW+
phZzDKw++oLayIyB2DK/W32lkbGKHmorK+e0CT/4LTevwqrKuSMvkC86RoxZpeY/
gz/QNH26pIBM/wIS4P7beFSw6O7xQsBdmK8p94xiCZQRFeHUkp0BGExvZ04NWgqJ
27bRzs8pGmVLT71ia1B+CDsK/YMlxYjOLzpObVZ8ly1M789o5AFPN4vdEcgrEeJL
DSiJA+tqZg==
=ZYP7
-----END PGP PUBLIC KEY BLOCK-----
```


Note that terms and conditions are available in
[CONDITIONS.md](CONDITIONS.md).
