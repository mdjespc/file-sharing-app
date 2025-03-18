from view.main_view import MainView
from model.main_model import MainModel


class MainController():
    def __init__(self, model : MainModel, view : MainView):
        self.model = model
        self.view = view

        #test
        self.devices = ["0.0.0.0", "192.10.0.2"]
        self.local_ip  = self.model.local_ip
        if self.local_ip:
            self.view.update_alias_label(self.local_ip)

        #Add callbacks through controller
        self.view.add_callbacks("refresh", self.refresh)
        self.view.add_callbacks("upload", self.upload)

        #Bind the registered callback methods to their respective MainView widgets
        self.view.bind_commands()

    def refresh(self):
        self.view.update_device_list(self.devices)

    def upload(self):
        selected_file = self.view.request_file()
