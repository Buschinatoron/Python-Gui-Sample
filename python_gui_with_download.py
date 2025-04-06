from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import requests

class SimpleGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # set title, scale
        self.title("Simple_Gui")
        self.geometry("400x200")

        # icon
        try:
            icon = Image.open("#url/path")
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

        self.button = ttk.Button(self.container, text="Download File", command=self.download_file)
        self.button.pack()

    def download_file(self):
        url = "url"
        file_name = "downloaded_file.txt"

        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(file_name, "wb") as file:
                file.write(response.content)
            self.label.config(text="Download finished")
        except Exception as e:
            self.label.config(text=f"error: {e}")

if __name__ == "__main__":
    app = SimpleGUI()
    app.mainloop()
