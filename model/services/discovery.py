'''
Uses UDP broadcasts to announce presence and listens for discovery messages.
UDP protocol does not establish a connection before data transmission.


More on low-level networking:
https://docs.python.org/3/library/socket.html

More on thread-based parallelism:
https://docs.python.org/3/library/threading.html
'''

import socket
import threading


class DeviceDiscoveryService():
    DISCOVERY_PORT = 5000 #Windows network device interoperability port
    DISCOVERY_MSG = "FILE_TRANSFER_DISCOVERY"

    def __init__(self):
        self.discovered_devices = []
        self.local_ip = self.get_local_ip()

    def get_local_ip(self):
        """
        Retrieves the local machine's IP address by connecting to an external address.
        This helps identify the correct network interface to use.
        """

        #Connect to Google's DNS server and find local IP address
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()

        return local_ip
    
    def broadcast_discovery(self):
        """
        Sends a UDP broadcast message to the network to announce presence.
        Other devices listening on `DISCOVERY_PORT` can detect this message.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #Enable broadcasting
        '''
        The IP address 255.255.255.255 is a limited broadcast address, 
        meaning it's used to send data to all devices on the same local network segment, 
        but not across routers. 

        When a device sends a packet to this address, it's intended for all devices on the
        same network segment (also known as the same broadcast domain). 
        '''
        sock.sendto(self.DISCOVERY_MSG.encode(), ('255.255.255.255', self.DISCOVERY_PORT))
        sock.close()

    def listen(self):
        """
        Continuously listens for discovery messages from other devices.
        If a new device is detected, its IP is added to `discovered_devices`.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', self.DISCOVERY_PORT))

        while True:
            data, addr = sock.recvfrom(1024) #Attempt message reception through bound port
            if data.decode() == self.DISCOVERY_MSG and addr[0] != self.local_ip:
                if addr[0] not in self.discovered_devices:
                    self.discovered_devices.append(addr[0]) #Store discovered address
                    print(f"Discovered device {addr[0]} with message {data}")

    def listen_async(self):
        """
        Starts the discovery listener in a separate background thread without 
        blocking execution of the calling thread, while still being able to retrieve 
        their results when needed.

        This allows the application to run while continuously detecting devices.

        A thread can be flagged as a "daemon thread". 
        The significance of this flag is that the entire Python program exits when
        only daemon threads are left. 
        
        The initial value is inherited from the creating thread.
        """
        threading.Thread(target=self.listen, daemon=True).start()