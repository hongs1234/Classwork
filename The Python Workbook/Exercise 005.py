print("Enter the number of each bottle type you have to calculate refund:")
num_small_bottles = int(input("Number of small bottles: "))
num_large_bottles = int(input("Number of large bottles: "))
refund = (num_small_bottles * 0.10) + (num_large_bottles *0.25)

print(f"You get ${refund} back")