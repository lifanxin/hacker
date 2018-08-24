# -*- coding: utf-8 -*-
from pexpect import pxssh
import getpass


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()  #match the prompt
    print(s.before)
    print(s.before.decode())


def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print('[-] Error Connecting')
        exit(0)


if __name__ == '__main__':
    host = input('target_host: ')
    user_name = input('user_name: ')
    password = getpass.getpass('password: ')
    s = connect(host, user_name, password)
    send_command(s, 'ls')
