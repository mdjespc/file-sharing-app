from view.main_view import MainView


class MainController():
    def __init__(self, view : MainView):
        self.view = view

        #test
        self.devices = ["0.0.0.0", "192.10.0.2"]

        #Step 1 of button command bind: Add callback through controller
        self.view.add_callbacks("refresh", self.refresh)
        self.view.add_callbacks("upload", self.upload)

        #Step 2: Bind commands
        self.view.bind_commands()

    def refresh(self):
        self.view.update_device_list(self.devices)

    def upload(self):
        self.view.request_file()
