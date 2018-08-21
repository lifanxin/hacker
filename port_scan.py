# -*- coding: utf-8 -*-
import optparse
from socket import *
from threading import *


screen_lock = Semaphore(value = 1)


def connScan(target_host, target_port):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((target_host, target_port))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screen_lock.acquire()
        print('[+] {}/tcp open'.format(target_port))
        print('[+] ' + str(results))
    except Exception as e:
        screen_lock.acquire()
        print('[-] {}/tcp closed'.format(target_port))
        print(e)
    finally:
        screen_lock.release()
        connSkt.close()


def portScan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print('[-] Cannot resolve {}: Unknown host'.format(target_host))
        return

    try:
        target_name = gethostbyaddr(target_ip)
        print('\n[+] Scan Results for: ' + target_name[0])
    except:
        print('\n[+] Scan Results for：' + target_ip)
    setdefaulttimeout(10)
    for target_port in target_ports:
         # print('Scanning port ' + target_port)
         # connScan(target_host, int(target_port))
         t = Thread(target=connScan, args=(target_host, int(target_port)))
         t.start()


def main():
    parser = optparse.OptionParser('usage %prog -H <target host>  -p <target port>')
    parser.add_option('-H', dest='target_host', type='string', help='specify target host')
    parser.add_option('-p', dest='target_port', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    target_host = options.target_host
    target_ports = str(options.target_port).split(',')
    if (target_host == None) | (target_ports[0] == None):
        # print(parser.usage)
        print('[-] You must specify a target host and port[s].')
        exit(0)
    portScan(target_host, target_ports)


if __name__ == '__main__':
    main()
