# Reverse-DNS
This tool can be used to identify the Fully Qualified Domain Name (FQDN) of IP addresses within a subnet. 

Required python3 packages
- dnspython
- ipaddress

Note: Threading has not yet been implemented in this tool. Be aware that enumerating IP addresses on anything greater than 
a /16 subnet (i.e. the quantity of IP addresses is greater than the total IP addresses in a /16 subnet) will take a considerable amount of time to complete.
