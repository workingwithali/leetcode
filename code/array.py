# Input lines
line1 = ""
line2 = ""

# Convert the lines into lists
line1_array = line1.split()
line2_array = line2.split()

# Switch the values between the two arrays
swapped_array = [line2_array[i] for i in range(len(line2_array))]

# Print the swapped array
print("Original Arrays:")
print("Line 1:", line1_array)
print("Line 2:", line2_array)

print("\nSwapped Array:")
print(swapped_array)
