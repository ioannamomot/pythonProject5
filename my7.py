import random
a = [random.randint (0, 10)
     for i in range(7)]
b = [random.randint (0, 10)
     for i in range(7)]
print(a, b)

same_values = set(a) & set(b)
print (same_values)
