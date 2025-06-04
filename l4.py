# bool - True и False

# num1 = int(input("enter a number: "))
# and - и or - или
# sl1 = num1 > 10 and num1 % 2 == 0

# print(usl1)

# if условия == True:
    #действия
#elif условия == True:
    #действия
#elif условия == True:
    #действия
#else:
    #действия
# if num1 != 0 and num1 > 0:
#     print("Число положительное")
# elif num1 != 0 and num1 < 0:
#     print("Число отрицательное")
# else:
# #     print("0")
# usl1 = True
# print(not(usl1))
a1 = int(input("Введите число A: "))
a2 = int(input("Введите число Б: "))
a3 = input("Выберите действие: ")
if a3 == "+":
    print(a1 + a2)
elif a3 == "-":
    print(a1 - a2)
elif a3 == "*":
    print(a1 * a2)
elif a3 == "/":
    print(a1 / a2)
elif a3 == "**":
    print(a1 ** a2)
else:
    print("Возможно вы что-то сделали не так")