import re

handler = open("regex_sum_678843.txt")
total = 0 

numbers = re.findall("[0-9]+", handler.read())
print(numbers)

for number in numbers:
    total = total + int(number)

print("Total:", total)

# Existe otra forma de hacerlo en una linea de código
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )