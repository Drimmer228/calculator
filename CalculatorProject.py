from colorama import init
init()
from colorama import Fore, Style


def exception(codeExept):
    match (codeExept):
        case "wrong_number":
            print(Fore.RED + "Введено неверное число")
        case "bad_number":
            print(Fore.RED + "\tНельзя делить на ноль!")
    print(Style.RESET_ALL)

operations = 0
while operations <= 0:
    try:
        print("Введите количество операций:")
        operations = int(input())
    except:
        exception("wrong_number")

result = 0
while result <= 0:
    try:
        print("Введите первое число:")
        result = int(input())
    except:
        exception("wrong_number")

for i in range(operations):
    action = 0
    while action <= 0 or action >= 6:
        try:
            print("Введите операцию, где:")
            print("1: сложение")
            print("2: вычитание")
            print("3: умножение")
            print("4: деление")
            print("5: возведение в степень")

            action = int(input())
        except:
            exception("wrong_number")

    secondNumber = 0
    while secondNumber <= 0:
        try:
            print("Введите второе число:")
            secondNumber = int(input())
        except:
            exception("wrong_number")

    match(action):
        case 1:
            result += secondNumber
            print(Fore.GREEN + "\tСумма цифр =", result)
        case 2:
            result -= secondNumber
            print(Fore.GREEN + "\tРазность цифр =", result)
        case 3:
            result *= secondNumber
            print(Fore.GREEN + "\tПроизведение цифр =", result)
        case 4:
            if secondNumber!=0:
                result /= secondNumber
                print(Fore.GREEN + "\tЧастное цифр =", result)
            else:
                exception("bad_number")
        case 5:
            temp = result
            result **= secondNumber
            print(Fore.GREEN + "\tСтепень числа", temp, "=", result)
    print(Style.RESET_ALL)