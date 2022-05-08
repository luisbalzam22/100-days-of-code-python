HEIGHTS = [1.75, 1.55, 1.83, 1.80, 1.66, 1.78, 1.69]

total_count = 0
largest_height = 0
total_sum = 0


for height in HEIGHTS:
    total_count +=1
    total_sum += height
    if height > largest_height:
        largest_height = height
    
print(f"The average height of summing-up {HEIGHTS} is: {round(total_sum/ total_count)}\n And the largest height is: {largest_height}")