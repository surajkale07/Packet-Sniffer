from scapy.all import *

def handler(packet):
    print(packet.summary())

if __name__ == "__main__":

    sniff(iface=conf.iface, prn=handler, store=0)