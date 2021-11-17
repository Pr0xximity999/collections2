num1 = int(input("geef getal 1 >>"))
num2 = int(input("geef getal 2 >>"))

if num1 > num2:
    print(f"{num1} is groter")
else:
    print(f"{num2} is groter")

num1 = int(input("geef getal 1 >>"))
num2 = int(input("geef getal 2 >>"))

for i in range(num1, num2 + 1):
    print(i)


num1 = int(input("geef getal 1 >>"))
num2 = int(input("geef getal 2 >>"))

i = num1
while i < num2 - 1:
    print(i)
    i += 1

num1 = int(input("geef getal 1 >>"))
num2 = int(input("geef getal 2 >>"))

for i in range(num2, num1, -1):
    print(i)


num1 = int(input("geef getal 1 >>"))
num2 = int(input("geef getal 2 >>"))

i = num2
while i > num1 - 1:
    print(i)
    i -= 1