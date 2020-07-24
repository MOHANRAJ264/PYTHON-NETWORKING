#Layer3  addressing MAC
from netaddr import *
def finding_all_details_of_MAC(addr):

    #Instances of the EUI class are used to represent MAC addresses
    mac=EUI(addr)

    #methods to provide info on OUI and other organizational info
    print("OUI-:",mac.info)
    oui=mac.oui
    print("Organization-:",oui.registration().org)
    print("Registration address",oui.registration().address)



if __name__ == "__main__":
    addr=input("Enter your MAC(Physical addres)-:")
    finding_all_details_of_MAC(addr)
    #80-32-53-86-08-6B
    