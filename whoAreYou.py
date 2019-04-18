# -*- encoding: utf-8 -*-
import time
import ipaddress
import os
from dns import resolver, reversename

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
def getAddressList():
    x = input("Enter address range (ex. 192.168.0.0/24): \n> ")
    f = open("iplist.txt", "w+")

    for ip in ipaddress.IPv4Network(x):
        f.write(str(ip) + "\n")

    f.close()
    print("\nEnumerating IP addresses to resolve...")
    time.sleep(2)
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
def getFQDN():
    d = open("alive.txt", "w+")
    d.write("IP Address\t\tDomain Name\n")
    d.write("_ _ _ _ _ _     _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

    e = open("sleep.txt", "w+")
    e.write("IP Address\t\tDomain Name\n")
    e.write("_ _ _ _ _ _     _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
    list = []
    for line in open('iplist.txt', 'r'):
        list.append(line.strip())

    print("\nResolving IP addresses...")
    x = 0
    for ip in list:
        try:
            addr = reversename.from_address(list[x])
            result=str(resolver.query(addr,"PTR")[0])
            d.write(list[x] + "\t" + result + "\n")
            # print(list[x] + "\t" + result)
            x += 1
        except:
            e.write(list[x] + "\t\t" + "Not Found" + "\n")
    		# print(list[x] + "\t" + "Not Found")
            x += 1

    d.close()
    e.close()
    storage = os.getcwd()
    print("\nTask Complete! Results are stored in the following path:\n" + storage + "\n")
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
def main():
    getAddressList()
    getFQDN()
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
main()
