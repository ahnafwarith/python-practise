# 6. Write a python program that takes a number N as input and prints the series 1 + 11 + 111 + 1111 + ... and then prints the sum

inputValue = int(input("Please enter the number you want your series: "))
container = ""
summation = 0
for i in range(0, inputValue):
    container += '1'*i + "+"
    summation += i
print(container, summation)
