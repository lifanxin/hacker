# -*- coding: utf-8 -*-
import pexpect


PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect(['[P|p]assword:', ssh_newkey, pexpect.TIMEOUT])
    if ret == 0:
        child.sendline(password)
        child.expect(PROMPT)
        return child
    elif ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return
        child.sendline(password)
        child.expect(PROMPT)
        return child
    elif ret == 2:
        print('[-] Error Connecting')
        return


def main():
    host = '127.0.0.1'
    user = 'your_user_name'
    password = 'your_password'
    child = connect(user, host, password)
    send_command(child, 'ls')


if __name__ == '__main__':
    main()
