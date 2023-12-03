import socket

def reverse_lookup(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        print(hostnames)
        domain_name = hostnames[0]
        return domain_name
    except socket.herror:
        return None

# 示例使用
ip_address = '39.99.128.227'
# ip_address = '122.114.161.117'
domain_name = reverse_lookup(ip_address)
if domain_name:
    print(f"The domain name associated with the IP address {ip_address} is: {domain_name}")
else:
    print(f"No domain name found for the IP address {ip_address}")