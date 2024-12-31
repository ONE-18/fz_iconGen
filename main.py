import tkinter as tk
from PIL import Image, ImageDraw

# Configuración inicial
CELLS = 10
CELL_SIZE = 50
GRID_SIZE = CELLS * CELL_SIZE

class PixelGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Matriz 10x10")
        self.canvas = tk.Canvas(root, width=GRID_SIZE, height=GRID_SIZE, bg="white")
        self.canvas.pack()
        
        # Crear celdas iniciales
        self.grid = [[0 for _ in range(CELLS)] for _ in range(CELLS)]
        self.rectangles = [[None for _ in range(CELLS)] for _ in range(CELLS)]
        self.create_grid()
        
        # Configurar el clic
        self.canvas.bind("<Button-1>", self.toggle_cell)
        
        # Botón para guardar como PNG
        self.save_button = tk.Button(root, text="Guardar como PNG", command=self.save_as_png)
        self.save_button.pack(pady=10)

    def create_grid(self):
        for i in range(CELLS):
            for j in range(CELLS):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                self.rectangles[i][j] = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="white", outline="black"
                )
    
    def toggle_cell(self, event):
        x, y = event.x, event.y
        row, col = y // CELL_SIZE, x // CELL_SIZE
        if 0 <= row < CELLS and 0 <= col < CELLS:
            # Alternar color
            self.grid[row][col] = 1 - self.grid[row][col]
            color = "black" if self.grid[row][col] else "white"
            self.canvas.itemconfig(self.rectangles[row][col], fill=color)
    
    def save_as_png(self):
        # Crear una imagen de 10x10
        image = Image.new("RGB", (CELLS, CELLS), "white")
        draw = ImageDraw.Draw(image)
        
        for i in range(CELLS):
            for j in range(CELLS):
                color = (0, 0, 0) if self.grid[i][j] else (255, 255, 255)
                draw.point((j, i), fill=color)
        
        # Guardar como PNG
        image.save("matriz_10x10.png")
        print("Imagen guardada como matriz_10x10.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = PixelGridApp(root)
    root.mainloop()
