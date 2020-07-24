import dns 
import dns.resolver
# domain names to IP address
def look_dns(name):
    #ip address for the domain using the dns.resolver.resolve
    #mapping between IP address and domain name is also known as 'A' record
    try:

        result = dns.resolver.resolve(name+".com", 'A')
        for ipval in result:
            print('IP for '+name+" is -: "+ ipval.to_text())
    except Exception:
        print("Does mot have IP address for this ")


quit="wrong"
while True:
        name=input("Enter the name for which you want to check the DNS lookup-:")
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

                
