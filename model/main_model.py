from model.services.discovery import DeviceDiscoveryService
from model.services.transfer import FileTransferService

class MainModel():
    '''
    Provides an encapsulation of application services
    '''
    def __init__(self):
        self.discovery_service = DeviceDiscoveryService()
        self.transfer_service = FileTransferService()

        #Get own IP address and listen to broadcast messages on daemonic thread
        self.local_ip = self.discovery_service.get_local_ip()
        self.discovery_service.listen_async()
        print("Device Discovery Service initialized and running.")

    def get_discovered_devices(self):
        #Send broadcast message and update list of received signals
        self.discovery_service.broadcast_discovery()
        return self.discovery_service.discovered_devices