'''
file_transfer_app/
│── model/
│   ├── device_discovery.py  #Handles network scanning and device detection
│   ├── file_transfer.py     #Manages file sending and receiving
│   ├── config.py            #Stores application settings (e.g., port numbers)
│── view/
│   ├── main_view.py         #Tkinter GUI, displaying detected devices and controls
│── controller/
│   ├── main_controller.py   #Manages interaction between view and model
│── run.py                   #Entry point to launch the application
'''

import tkinter as tk
from view.main_view import MainView
from controller.main_controller import MainController

if __name__ == "__main__":
    root = tk.Tk()
    controller = MainController(MainView(root))
    root.mainloop()