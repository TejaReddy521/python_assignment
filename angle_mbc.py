import math

# Get input from user
AB = float(input("Enter the length of side AB: "))
BC = float(input("Enter the length of side BC: "))

# Calculate length of hypotenuse AC
AC = math.sqrt(AB*2 + BC*2)

# Calculate angle MBC using the tangent function
MBC = math.degrees(math.atan(AB/BC))

# Print the result
print("Angle MBC is:", MBC, "degrees")