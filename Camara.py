import tkinter as tk

class TriangleButton(tk.Canvas):
    def __init__(self, parent, text, size, color, command=None, *args, **kwargs):
        super().__init__(parent, width=size, height=size, *args, **kwargs)
        self.parent = parent
        self.size = size
        self.color = color
        self.command = command
        
        self.create_polygon(0, size, size/2, 0, size, size, outline=color, fill=color)
        self.create_text(size/2, size/2, text=text, fill="white")
        self.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        if self.command:
            self.command()

def on_button_click():
    print("Botón de triángulo presionado")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Botón de Triángulo")

    triangle_button = TriangleButton(root, "Presionar", size=100, color="green", command=on_button_click)
    triangle_button.pack(pady=20)

    root.mainloop()


















