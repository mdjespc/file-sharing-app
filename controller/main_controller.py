from view.main_view import MainView


class MainController():
    def __init__(self, view : MainView):
        self.view = view

        #test
        devices = ["0.0.0.0", "192.10.0.2"]
        self.view.update_device_list(devices)