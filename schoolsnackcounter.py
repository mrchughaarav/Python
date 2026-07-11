from array import array

# Step 1: Create Snack Boxes as Sets
snack_box1 = {"chips", "cookies", "apple", "chips"}
snack_box2 = {"cookies", "banana", "juice", "cookies"}

print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)

# Step 2: Add a New Snack to a Set
snack_box1.add("banana")
print("\nUpdated Snack Box 1:", snack_box1)

# Step 3: Find Common Snacks
common_snacks = snack_box1.intersection(snack_box2)
print("Common Snacks:", common_snacks)

# Step 4: Create an Array of Snack Counts
snack_counts = array('i', [5, 3, 2, 3])

# Step 5: Add Items to the Array
snack_counts.insert(0, 10)
snack_counts.append(7)

# Step 6: Count and Reverse the Array
count_of_3 = snack_counts.count(3)
snack_counts.reverse()

# Step 7: Print the Final Summary
print("\nFinal Summary")
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
print("Shared Snacks:", common_snacks)
print("Snack Counts:", snack_counts)
print("Number 3 appears", count_of_3, "times.")

# Step 8: Run and Explore
print("\nTry changing the snack names or count values to see different results!")