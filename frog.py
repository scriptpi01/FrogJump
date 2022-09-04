
import math

number = list()
x = input().split()
number.append(x)
num1 = int(number[0][0])
num2 = int(number[0][1])
if num1 > num2 :
    print(2)
elif num2 % num1 ==0 :
    print(f'{num2//num1}')
else:
    print(math.ceil(num2/num1))
