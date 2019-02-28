year_of_birth = int(input("Enter the year of birth: "))
divided = year_of_birth % 12

if divided == 8:
    print("You are a Dragon")
elif divided == 9:
    print("You are a Snake")
elif divided == 10:
    print("You are a Horse")
elif divided == 11:
    print("You are a Sheep")
elif divided == 0:
    print("You are a Monkey")
elif divided == 1:
    print("Your are a Rooster")
elif divided == 2:
    print("You are a Dog")
elif divided == 3:
    print("You are a Pig")
elif divided == 4:
    print("You are a Rat")
elif divided == 5:
    print("You are a Ox")
elif divided == 6:
    print("You are a Tiger")
else:
    print("You are a Hare")

