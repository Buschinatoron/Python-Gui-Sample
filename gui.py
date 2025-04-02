from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

class SimpleGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # set title,scale
        self.title("Simple_Gui")
        self.geometry("400x200")

        # icon
        try:
            icon = Image.open("ur_image.png")
            photo = ImageTk.PhotoImage(icon)
            self.iconphoto(True, photo)
        except Exception as e:
            print(f"photo loading error {e}")

        # set background color
        self.container = tk.Frame(self, bg="lightpink")
        self.container.pack(fill="both", expand=True)

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Beenden", command=self.quit)
        menubar.add_cascade(label="Sample", menu=file_menu)

        self.config(menu=menubar)

    def create_widgets(self):
        # set style
        style = ttk.Style()
        style.configure("TLabel", background="#05b1f5", foreground="Black")

        self.label = ttk.Label(self.container, text="Text1", style="TLabel")
        self.label.pack(pady=20)


        self.button = ttk.Button(self.container, text="Button1", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Text2")
        self.button.config(text="Button_end", command=self.quit)

if __name__ == "__main__":
    app = SimpleGUI()
    app.mainloop()
