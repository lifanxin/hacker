# -*- coding: utf-8 -*-
import nmap
import optparse


def nmapScan(target_host, target_port):
    nmap_scan = nmap.PortScanner()
    nmap_scan.scan(target_host, target_port)
    state = nmap_scan[target_host]['tcp'][int(target_port)]['state']
    print('[*] ' + target_host + ' tcp/' + target_port + ' ' + state)


def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='target_host', type='string', help='specify target host')
    parser.add_option('-p', dest='target_port', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    target_host = options.target_host
    target_ports = str(options.target_port).split(',')
    if (target_host == None) | (target_ports[0] == None):
        print(parser.usage)
        exit(0)
    for target_port in target_ports:
        nmapScan(target_host, target_port)


if __name__ == '__main__':
    main()
