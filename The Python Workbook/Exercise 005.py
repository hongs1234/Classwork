print("Enter the number of each bottle type you have to calculate refund:")
one_litre_or_less = int(input("Number of one_litre_or_less bottles: "))
more = int(input("Number of more than one litre bottles: "))
refund = (one_litre_or_less * 0.10) + (more *0.25)

print(f"You get ${refund} back")