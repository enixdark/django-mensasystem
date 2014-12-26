from netifaces import interfaces, ifaddresses, AF_INET

def get_ip():
    ips = []
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET,[{'addr':''}] )]
	ips += addresses
    return filter(lambda  x : x not in ['127.0.0.1',''],ips)
