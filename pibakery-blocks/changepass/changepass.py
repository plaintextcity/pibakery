#!/usr/bin/env python
# Thanks to Filipe Pina on StackOverflow
# plaintextcity: use sha512.  Allow sha512 crypts directly.

import subprocess,crypt,random, sys

login = 'pi'
password = sys.argv[1]
magic = password[:3]
print 'magic: ' + magic

if magic != '$6$':
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
    salt = ''.join(random.choice(ALPHABET) for i in range(16))
    password = crypt.crypt(password,'$6$'+salt+'$')

r = subprocess.call(('usermod', '-p', password, login))

if r != 0:
    print 'Error changing password for ' + login
