def calculate_total_distance(left_list, right_list):
    # Step 1: Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Step 2: Calculate the sum of absolute differences
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance

# Example input
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]





# Calculate the total distance
total_distance = calculate_total_distance(left_list, right_list)
print("Total Distance:", total_distance)
