def calculate_water_mass(radius, height):
    density_water = 1000.0
    volume = 3.14159 * radius**2 * height
    mass = volume * density_water / 1000.0  
    return round(mass, 2)

radius_cylinder = 2.0
height_cylinder = 5.0
water_mass = calculate_water_mass(radius_cylinder, height_cylinder)
print("Масса воды в цилиндре:", water_mass, "кг")