result = 5 + 10 # сложения
result2 = 10 - 2 # вычитание
result3 = 5 * 5 # усножен
result4 = 5 / 2 # деление , вернет float
print(result4, type(result4))
result5 = 5 // 2  # вернет целое int
print(result5, type(result5))
result6 = 5 % 2    # вернет остаток int
print(result6, type(result6))

result7 = 5 ** 2 # возводим в степень int
print(result7, type(result7))

num1 = -123
abs_num1 = abs(num1) # модуль числа int
print(abs_num1, type(abs_num1))

num2 = 233

num2 = "hello"
print(num2, type(num2))

# str - str() float - float() int - int()
num2 = 25
num2 = str(num2)

print(num2, type(num2))
num3 = float(num2)
print(num3, type(num3))