from model.services.discovery import DeviceDiscoveryService
from model.services.transfer import FileTransferService

class MainModel():
    '''
    Provides an encapsulation of application services
    '''
    def __init__(self):
        self.discovery_service = DeviceDiscoveryService()
        self.transfer_service = FileTransferService()

        self.local_ip = self.discovery_service.get_local_ip()

    def get_discovered_devices(self):
        self.discovery_service.broadcast_discovery()
        return self.discovery_service.discovered_devices