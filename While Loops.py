# 1
my_str = "hello"
i = 0

while i < len(my_str):
  char = my_str[i]
  print(char)
  i += 1


print()

# 2
numbers = [7, 7, 2, 7, 11]
a = 0

while a < len(numbers):
  num = numbers[a]
  print(num)
  a += 1


print()

# 3
marks = [84, 89, 90, 45, 67]
b = 0

while b < len(marks):
  grade = marks[b]
  print(grade)
  b += 1


print()

# 4

c = 0
while c in range(10):
  print(c)
  c += 1


print()

# 5
d = 5
while d in range(5, 100):
  print(d)
  d += 5


print()

# 6
e = 100
while e in range(100, -1, -5):
  print(e)
  e += -5