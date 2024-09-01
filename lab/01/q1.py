def trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height

def parallelogram(base, height):
    return base * height

def sa_cylinder(radius, height):
    return (2 * 3.14 * radius * height) + (2 * 3.14 * (radius ** 2))

def sv_cylinder(radius, height):
    return 3.14 * (radius ** 2) * height

# Variables
a = 3  # base1 of the trapezoid, base of the parallelogram
b = 5  # base2 of the trapezoid
h = 6  # height for trapezoid, parallelogram, and cylinder
r = 7  # radius of the cylinder

# Calculate and print the areas and volumes
print("Trapezoid Area:", trapezoid(a, b, h))
print("Parallelogram Area:", parallelogram(a, h))
print("Surface Area of Cylinder:", sa_cylinder(r, h))
print("Volume of Cylinder:", sv_cylinder(r, h))

