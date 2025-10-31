import customtkinter as ctk
from components.settings import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações iniciais do app.
        self.title(app_title)
        self.geometry(f'{app_width}x{app_height}')

if __name__ == '__main__':
    try:
        app = App()
        app.mainloop()
    
    except Exception as e:
        print("Erro: ", e)

