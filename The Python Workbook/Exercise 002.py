name = input("""What is your name? 
""")
print(f"Hello, {name}, what's up?")
mood = input("How are you feeling? ")
if mood == "good" or mood == "great":
  print(f"So you feel {mood}, that's great!")
elif mood =="bad":
  print(f"Aww. You feel {mood}. That sucks.")
else:
  print(f"So you feel {mood}. Alright")
