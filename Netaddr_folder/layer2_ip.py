#Layer 2 Addressing the IP
#pip install netaddr
from netaddr import IPAddress
def finding_details_of_IP(addr):

    #IPAddress object represents a single IP address
    ip=IPAddress(addr)

    #version of IP
    print("IP Version-:",ip.version)

    #methods to handle coverting an IP adress into binary or bits, split an IP, pack 
    print("IP Binary-:",ip.bin)
    print("IP bits-:",ip.bits())
    print("IP split-:",ip.words)
    print("IP pack-:",ip.packed)

    #methods to check if the type of IP address(class, scope, type)
    print("If unicast-:",ip.is_unicast())
    print("If link to local-:",ip.is_link_local())


if __name__ == "__main__":
    addr=input('Enter the IP address-:')
    #192.168.43.124
    finding_details_of_IP(addr)