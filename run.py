import tkinter as tk
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController

if __name__ == "__main__":
    root = tk.Tk()
    controller = MainController(MainModel(), MainView(root))
    root.mainloop()