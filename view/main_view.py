import os
import tkinter as tk
from tkinter import filedialog, Label, Button, Listbox
from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk


class MainView():
    ROOTWIDTH, ROOTHEIGHT = 300, 500
    BGCOLOR = "#d5d9ce"
    HEADERCOLOR = "#000000"
    PRIMARYFONT = ("Bookman Old Style", 12, "bold") 
    HEADERFONT = ("Bookman Old Style", 28, "bold")
    PRIMARYSTYLE = {
        "font": PRIMARYFONT,
        "bg":"#137fad",
        "fg":"#ffffff",
        "highlightcolor":"#063d80",
        "relief":tk.FLAT
    }

    def __init__(self, root : tk.Tk):
        self.root = root
        self.callbacks = dict()

        self.root.geometry(f"{self.ROOTWIDTH}x{self.ROOTHEIGHT}")
        self.root.title("File Sharing App")
        favicon_path = os.path.abspath(os.path.join("resources", "favicon.ico"))
        self.root.iconbitmap(default = favicon_path)

        canvas = tk.Canvas(self.root, width=self.ROOTWIDTH, height=self.ROOTHEIGHT, bg=self.BGCOLOR, bd=0)
        canvas.grid(row=0,
                    rowspan=6,
                    column=0,
                    columnspan=4,
                    padx=0,
                    pady=0,
                    sticky="nsew"
        )

        self.header_label = Label(self.root,
                                  font=self.HEADERFONT,
                                  bg=self.BGCOLOR,
                                  fg=self.HEADERCOLOR,
                                  text="FILE SHARING"
                                )
        self.header_label.grid(row=0,
                               column=0,
                               padx=0,
                               pady=0
        )

        logo_image_path = os.path.abspath(os.path.join("resources", "logo.png"))
        self.main_logo = ImageTk.PhotoImage(Image.open(logo_image_path).resize((128, 128)))
        self.main_logo_label = Label(self.root, image=self.main_logo, bg=self.BGCOLOR)
        self.main_logo_label.grid(row=1,
                                column=0,
                                padx=0,
                                pady=0
        )
        
        
        self.alias_label = Label(self.root,
                                 text=f"UNKNOWN",
                                 cnf=self.PRIMARYSTYLE
        )
        self.alias_label.grid(row=2,
                              column=0,
                              padx=5,
                              pady=5)

        self.device_listbox = Listbox(self.root,
                                         width=10,
                                         height=5,
                                         bd=7,
                                         highlightthickness=0,
                                         font=self.PRIMARYFONT,
                                         bg=self.PRIMARYSTYLE["bg"],
                                         fg=self.PRIMARYSTYLE["fg"],
                                         selectbackground=self.PRIMARYSTYLE["highlightcolor"],
                                         relief=self.PRIMARYSTYLE["relief"]
                                         )
        self.device_listbox.grid(row=3,
                                rowspan=1,
                                column=0,
                                columnspan=2,
                                padx=5,
                                pady=0
                                )
        
        self.refresh_button = Button(self.root,
                                     cnf=self.PRIMARYSTYLE,
                                     text="REFRESH",
                                     width=10,
                                     height=2)
        self.refresh_button.grid(row=4,
                                column=0,
                                padx=5,
                                pady=5
        )

        self.upload_button = Button(self.root,
                                     cnf=self.PRIMARYSTYLE,
                                     text="UPLOAD",
                                     width=10,
                                     height=2)
        self.upload_button.grid(row=5,
                                column=0,
                                padx=5,
                                pady=5
        )

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


    def update_alias_label(self, alias):
        self.alias_label.config(text=f"Others will see you as {alias}")

    '''
    Callback methods

    These are strictly binded to the corresponding Tkinter widgets that trigger them on interaction.
    All callback method binding is handled through the controller.
    '''
    def update_device_list(self, devices):
        #Updates the listbox with detected devices
        self.device_listbox.delete(0, tk.END)
        for device in devices:
            self.device_listbox.insert(tk.END, device)

    def request_file(self):
        return filedialog.askopenfilename()


    '''
    In order to bind commands, the associated callback method is added
    through the controller.

    Once the controller has verified that all relevant methods have been
    added to the callback dictionary, it will then call `bind_commands`
    to individually configure each button or widget with the corresponding
    callback method as its command bind.
    '''
    def add_callbacks(self, key, method):
        self.callbacks[key] = method

    def bind_commands(self):
        self.refresh_button.config(command=self.callbacks["refresh"])
        self.upload_button.config(command=self.callbacks["upload"])