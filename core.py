import tkinter as tk

class App:
    def __init__(self, width=800, height=600, title="Blinkable App"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        self.labels = []
        self.buttons = []

    # Visual Components

    def add_text(self, text, font=("Arial", 20)):
        label = tk.Label(self.root, text=text, font=font)
        label.pack(pady=20)
        self.labels.append(label)
        return label

    def add_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command)
        button.pack(pady=10)
        self.buttons.append(button)
        return button

    # Logic Components

    def render(self):
        self.root.mainloop()
