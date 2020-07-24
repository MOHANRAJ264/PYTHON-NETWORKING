#To understand cname ... Google.com has many services like mail,docs .though mail and docs have diffrent domain names
#they could actually point to the same computer with 1 IP address

import dns 
import dns.resolver


def look_dns(name):
    
    try:
        result = dns.resolver.resolve(name, 'CNAME')
        for cnameval in result:
            print('Cname for '+name+" is -: "+ str(cnameval.target))
    except Exception:
        print("Does not have Cname for this")
    

quit="wrong"
while True:
        name=input("Enter the name for which you want to check the Cannonical Name-:")
        look_dns(name)
        while True:
            quit=input("Do you want to quit ? (Y or N) ").lower()
            if quit not in ["n","y"]:
                print("PLease give the valid input")
            else:
                break


        if quit=="y":
            print("--------")
            print("Thank you for visiting us!")
            break

                
