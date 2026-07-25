import tkinter as tk
import math
import tkinter.messagebox as messagebox

#class for polygon
class Polygon:
    def __init__(self, numberOfSides, name):
        self.numberOfSides = numberOfSides
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass
        
#class for rectangle
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4, "Rectangle")
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

#class for triangle
class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        super().__init__(3, "Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

#rectangle button
def rectangle():
    try:
        length = float(entry1.get())
        width = float(entry2.get())

        if length <= 0 or width <= 0:
            raise ValueError

        rect = Rectangle(length, width)

        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Shape: {rect.name}\n")
        output.insert(tk.END, f"Number of Sides: {rect.numberOfSides}\n")
        output.insert(tk.END, f"Area: {rect.area():.2f}\n")
        output.insert(tk.END, f"Perimeter: {rect.perimeter():.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid positive numbers.")

#triangle
def triangle():
    try:
        side1 = float(entry1.get())
        side2 = float(entry2.get())
        side3 = float(entry3.get())

        if (side1 + side2 <= side3 or
            side1 + side3 <= side2 or
            side2 + side3 <= side1):
            messagebox.showerror("Error", "The given sides do not form a valid triangle.")
            return

        tri = Triangle(side1, side2, side3)

        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Shape: {tri.name}\n")
        output.insert(tk.END, f"Number of Sides: {tri.numberOfSides}\n")
        output.insert(tk.END, f"Area: {tri.area():.2f}\n")
        output.insert(tk.END, f"Perimeter: {tri.perimeter():.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive numbers.")

#popup ui
root = tk.Tk()
root.title("Polygon Shape Calculator")
root.geometry("450x450")

tk.Label(root, text="Value 1 (Length / Side 1)").pack()
entry1 = tk.Entry(root, width=30)
entry1.pack()

tk.Label(root, text="Value 2 (Width / Side 2)").pack()
entry2 = tk.Entry(root, width=30)
entry2.pack()

tk.Label(root, text="Value 3 (Side 3 - Triangle Only)").pack()
entry3 = tk.Entry(root, width=30)
entry3.pack(pady=5)

tk.Button(root, text="Rectangle", width=20, command=rectangle).pack(pady=5)
tk.Button(root, text="Triangle", width=20, command=triangle).pack(pady=5)

output = tk.Text(root, height=10, width=50)
output.pack(pady=10)

root.mainloop()