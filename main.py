import tkinter as tk
from tkinter import messagebox
import math
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate area
def calculate_area():
    def calculate():
        shape = shape_var.get()
        try:
            if shape == "Square":
                side = float(side_entry.get())
                result.set(f"Area of Square: {side ** 2}")
            elif shape == "Rectangle":
                length = float(length_entry.get())
                width = float(width_entry.get())
                result.set(f"Area of Rectangle: {length * width}")
            elif shape == "Circle":
                radius = float(radius_entry.get())
                result.set(f"Area of Circle: {math.pi * radius ** 2}")
            elif shape == "Triangle":
                base = float(base_entry.get())
                height = float(height_entry.get())
                result.set(f"Area of Triangle: {0.5 * base * height}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    # Create a new window for area calculation
    area_window = tk.Toplevel()
    area_window.title("Area Calculation")

    # Dropdown for shape selection
    shape_var = tk.StringVar()
    shape_var.set("Square")
    shape_options = ["Square", "Rectangle", "Circle", "Triangle"]
    shape_menu = tk.OptionMenu(area_window, shape_var, *shape_options)
    shape_menu.pack()

    # Input fields for each shape
    side_label = tk.Label(area_window, text="Enter side length (Square):")
    side_label.pack()
    side_entry = tk.Entry(area_window)
    side_entry.pack()

    length_label = tk.Label(area_window, text="Enter length (Rectangle):")
    length_label.pack()
    length_entry = tk.Entry(area_window)
    length_entry.pack()

    width_label = tk.Label(area_window, text="Enter width (Rectangle):")
    width_label.pack()
    width_entry = tk.Entry(area_window)
    width_entry.pack()

    radius_label = tk.Label(area_window, text="Enter radius (Circle):")
    radius_label.pack()
    radius_entry = tk.Entry(area_window)
    radius_entry.pack()

    base_label = tk.Label(area_window, text="Enter base (Triangle):")
    base_label.pack()
    base_entry = tk.Entry(area_window)
    base_entry.pack()

    height_label = tk.Label(area_window, text="Enter height (Triangle):")
    height_label.pack()
    height_entry = tk.Entry(area_window)
    height_entry.pack()

    result = tk.StringVar()
    result_label = tk.Label(area_window, textvariable=result)
    result_label.pack()

    calculate_button = tk.Button(area_window, text="Calculate", command=calculate)
    calculate_button.pack()

# Function to calculate volume
def calculate_volume():
    def calculate():
        shape = shape_var.get()
        try:
            if shape == "Cube":
                side = float(side_entry.get())
                result.set(f"Volume of Cube: {side ** 3}")
            elif shape == "Rectangular Prism":
                length = float(length_entry.get())
                width = float(width_entry.get())
                height = float(height_entry.get())
                result.set(f"Volume of Rectangular Prism: {length * width * height}")
            elif shape == "Sphere":
                radius = float(radius_entry.get())
                result.set(f"Volume of Sphere: {(4/3) * math.pi * radius ** 3}")
            elif shape == "Cylinder":
                radius = float(radius_entry.get())
                height = float(height_entry.get())
                result.set(f"Volume of Cylinder: {math.pi * radius ** 2 * height}")
            elif shape == "Cone":
                radius = float(radius_entry.get())
                height = float(height_entry.get())
                result.set(f"Volume of Cone: {(1/3) * math.pi * radius ** 2 * height}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    # Create a new window for volume calculation
    volume_window = tk.Toplevel()
    volume_window.title("Volume Calculation")

    # Dropdown for shape selection
    shape_var = tk.StringVar()
    shape_var.set("Cube")
    shape_options = ["Cube", "Rectangular Prism", "Sphere", "Cylinder", "Cone"]
    shape_menu = tk.OptionMenu(volume_window, shape_var, *shape_options)
    shape_menu.pack()

    # Input fields for each shape
    side_label = tk.Label(volume_window, text="Enter side length (Cube):")
    side_label.pack()
    side_entry = tk.Entry(volume_window)
    side_entry.pack()

    length_label = tk.Label(volume_window, text="Enter length (Rectangular Prism):")
    length_label.pack()
    length_entry = tk.Entry(volume_window)
    length_entry.pack()

    width_label = tk.Label(volume_window, text="Enter width (Rectangular Prism):")
    width_label.pack()
    width_entry = tk.Entry(volume_window)
    width_entry.pack()

    radius_label = tk.Label(volume_window, text="Enter radius (Sphere/Cylinder/Cone):")
    radius_label.pack()
    radius_entry = tk.Entry(volume_window)
    radius_entry.pack()

    height_label = tk.Label(volume_window, text="Enter height (Cylinder/Cone):")
    height_label.pack()
    height_entry = tk.Entry(volume_window)
    height_entry.pack()

    result = tk.StringVar()
    result_label = tk.Label(volume_window, textvariable=result)
    result_label.pack()

    calculate_button = tk.Button(volume_window, text="Calculate", command=calculate)
    calculate_button.pack()

# Function to calculate surface area
def calculate_surface_area():
    def calculate():
        shape = shape_var.get()
        try:
            if shape == "Cube":
                side = float(side_entry.get())
                result.set(f"Surface area of Cube: {6 * side ** 2}")
            elif shape == "Rectangular Prism":
                length = float(length_entry.get())
                width = float(width_entry.get())
                height = float(height_entry.get())
                result.set(f"Surface area of Rectangular Prism: {2 * (length * width + width * height + height * length)}")
            elif shape == "Sphere":
                radius = float(radius_entry.get())
                result.set(f"Surface area of Sphere: {4 * math.pi * radius ** 2}")
            elif shape == "Cylinder":
                radius = float(radius_entry.get())
                height = float(height_entry.get())
                result.set(f"Surface area of Cylinder: {2 * math.pi * radius * (radius + height)}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    # Create a new window for surface area calculation
    surface_area_window = tk.Toplevel()
    surface_area_window.title("Surface Area Calculation")

    # Dropdown for shape selection
    shape_var = tk.StringVar()
    shape_var.set("Cube")
    shape_options = ["Cube", "Rectangular Prism", "Sphere", "Cylinder"]
    shape_menu = tk.OptionMenu(surface_area_window, shape_var, *shape_options)
    shape_menu.pack()

    # Input fields for each shape
    side_label = tk.Label(surface_area_window, text="Enter side length (Cube):")
    side_label.pack()
    side_entry = tk.Entry(surface_area_window)
    side_entry.pack()

    length_label = tk.Label(surface_area_window, text="Enter length (Rectangular Prism):")
    length_label.pack()
    length_entry = tk.Entry(surface_area_window)
    length_entry.pack()

    width_label = tk.Label(surface_area_window, text="Enter width (Rectangular Prism):")
    width_label.pack()
    width_entry = tk.Entry(surface_area_window)
    width_entry.pack()

    radius_label = tk.Label(surface_area_window, text="Enter radius (Sphere/Cylinder):")
    radius_label.pack()
    radius_entry = tk.Entry(surface_area_window)
    radius_entry.pack()

    height_label = tk.Label(surface_area_window, text="Enter height (Cylinder):")
    height_label.pack()
    height_entry = tk.Entry(surface_area_window)
    height_entry.pack()

    result = tk.StringVar()
    result_label = tk.Label(surface_area_window, textvariable=result)
    result_label.pack()

    calculate_button = tk.Button(surface_area_window, text="Calculate", command=calculate)
    calculate_button.pack()

# Function to calculate angles
def calculate_angles():
    def calculate():
        angle = float(angle_entry.get())
        radians = math.radians(angle)
        choice = choice_var.get()
        try:
            if choice == "Sine":
                result.set(f"Sine({angle}): {math.sin(radians)}")
            elif choice == "Cosine":
                result.set(f"Cosine({angle}): {math.cos(radians)}")
            elif choice == "Tangent":
                result.set(f"Tangent({angle}): {math.tan(radians)}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid angle")

    # Create a new window for angle calculation
    angle_window = tk.Toplevel()
    angle_window.title("Angle Calculation")

    # Dropdown for trigonometric function selection
    choice_var = tk.StringVar()
    choice_var.set("Sine")
    choices = ["Sine", "Cosine", "Tangent"]
    choice_menu = tk.OptionMenu(angle_window, choice_var, *choices)
    choice_menu.pack()

    # Input field for angle
    angle_label = tk.Label(angle_window, text="Enter angle in degrees:")
    angle_label.pack()
    angle_entry = tk.Entry(angle_window)
    angle_entry.pack()

    result = tk.StringVar()
    result_label = tk.Label(angle_window, textvariable=result)
    result_label.pack()

    calculate_button = tk.Button(angle_window, text="Calculate", command=calculate)
    calculate_button.pack()

# Function to calculate the hypotenuse
def calculate_hypotenuse():
    def calculate():
        try:
            side_a = float(side_a_entry.get())
            side_b = float(side_b_entry.get())
            hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
            result.set(f"Hypotenuse: {hypotenuse}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    # Create a new window for hypotenuse calculation
    hypotenuse_window = tk.Toplevel()
    hypotenuse_window.title("Hypotenuse Calculator")

    # Input fields for sides of the triangle
    side_a_label = tk.Label(hypotenuse_window, text="Enter side A:")
    side_a_label.pack()
    side_a_entry = tk.Entry(hypotenuse_window)
    side_a_entry.pack()

    side_b_label = tk.Label(hypotenuse_window, text="Enter side B:")
    side_b_label.pack()
    side_b_entry = tk.Entry(hypotenuse_window)
    side_b_entry.pack()

    result = tk.StringVar()
    result_label = tk.Label(hypotenuse_window, textvariable=result)
    result_label.pack()

    calculate_button = tk.Button(hypotenuse_window, text="Calculate", command=calculate)
    calculate_button.pack()

# Function to check for prime numbers
def prime_check():
    def check():
        try:
            num = int(num_entry.get())
            if num <= 1:
                result.set(f"{num} is not a prime number.")
            else:
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        result.set(f"{num} is not a prime number.")
                        break
                else:
                    result.set(f"{num} is a prime number.")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")

    # Create a new window for prime number check
    prime_window = tk.Toplevel()
    prime_window.title("Prime Number Check")

    # Input field for number
    num_label = tk.Label(prime_window, text="Enter a number:")
    num_label.pack()
    num_entry = tk.Entry(prime_window)
    num_entry.pack()

    result = tk.StringVar()
    result_label = tk.Label(prime_window, textvariable=result)
    result_label.pack()

    check_button = tk.Button(prime_window, text="Check", command=check)
    check_button.pack()

# Function to solve quadratic equations
def quadratic_solver():
    def solve():
        try:
            a = float(a_entry.get())
            b = float(b_entry.get())
            c = float(c_entry.get())
            discriminant = b ** 2 - 4 * a * c
            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                result.set(f"Roots: {root1}, {root2}")
            elif discriminant == 0:
                root = -b / (2 * a)
                result.set(f"One real root: {root}")
            else:
                result.set("No real roots")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")

    # Create a new window for quadratic solver
    quadratic_window = tk.Toplevel()
    quadratic_window.title("Quadratic Solver")

    # Input fields for coefficients
    a_label = tk.Label(quadratic_window, text="Enter coefficient a:")
    a_label.pack()
    a_entry = tk.Entry(quadratic_window)
    a_entry.pack()

    b_label = tk.Label(quadratic_window, text="Enter coefficient b:")
    b_label.pack()
    b_entry = tk.Entry(quadratic_window)
    b_entry.pack()

    c_label = tk.Label(quadratic_window, text="Enter coefficient c:")
    c_label.pack()
    c_entry = tk.Entry(quadratic_window)
    c_entry.pack()

    result = tk.StringVar()
    result_label = tk.Label(quadratic_window, textvariable=result)
    result_label.pack()

    solve_button = tk.Button(quadratic_window, text="Solve", command=solve)
    solve_button.pack()

# Main window
root = tk.Tk()
root.title("Math Tool App")

# Create buttons for different tools
area_button = tk.Button(root, text="Calculate Area", command=calculate_area)
area_button.pack(pady=10)

volume_button = tk.Button(root, text="Calculate Volume", command=calculate_volume)
volume_button.pack(pady=10)

surface_area_button = tk.Button(root, text="Calculate Surface Area", command=calculate_surface_area)
surface_area_button.pack(pady=10)

angles_button = tk.Button(root, text="Calculate Angles", command=calculate_angles)
angles_button.pack(pady=10)

hypotenuse_button = tk.Button(root, text="Calculate Hypotenuse", command=calculate_hypotenuse)
hypotenuse_button.pack(pady=10)

prime_button = tk.Button(root, text="Prime Number Check", command=prime_check)
prime_button.pack(pady=10)

quadratic_button = tk.Button(root, text="Quadratic Equation Solver", command=quadratic_solver)
quadratic_button.pack(pady=10)

# Run the application
root.mainloop()
