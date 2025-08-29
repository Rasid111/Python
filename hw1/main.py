def task1():
    name = input("Имя: ")
    age = input("Возраст: ")
    print(f"Привет, {name}! Через год тебе будет {int(age) + 1} лет.")


def task2():
    number = input("Число: ")
    print("Четное" if int(number) % 2 == 0 else "Нечетное")


def task3():
    for i in range(0, 11):
        for j in range(i, 11):
            print(f"{i} * {j} = {i*j}")


def task4():
    number = input("Число: ")
    output = 1
    for i in range(1, int(number) + 1):
        output *= i
    print(output)


def task5():
    for i in range(1, 21):
        print(f"{i}^2 = {i*i}")


def task6(word):
    for i in range(0, int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


def task7(text):
    result = {}
    splittetText = text.split()
    for word in splittetText:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def task8(text):
    result = text.split()
    result.sort(key=len)
    return result


def task9(length):
    import random
    import string
    letters = string.ascii_letters + string.digits + string.punctuation
    result = ""
    for i in range(0, int(length)):
        result += random.choice(letters)
    return result


def task10(arr1, arr2):
    result = list(dict.fromkeys(arr1 + arr2))
    return result


def task11(path):
    fstream = open(path)
    ftext = fstream.read()
    ccount = len(ftext)
    rcount = 0
    wcount = 0
    if ccount > 0:
        rcount = 1
        wcount = 1
        for c in ftext:
            if c == "\n":
                rcount += 1
                wcount += 1
            if c == " ":
                wcount += 1
    return {
        "rcount": rcount,
        "wcount": wcount,
        "ccount": ccount
    }


def task12(arr):
    if len(arr) == 0:
        return None
    else:
        max = arr[0]
        for value in arr:
            if value > max:
                max = value
    return max


def task13():
    numerator = input("Числитель: ")
    denominator = input("Знаменатель: ")
    try:
        presult = int(numerator) / int(denominator)
        print(presult)
    except ZeroDivisionError:
        print("Деление на ноль")
    except ValueError:
        print("Не число")


def task14():
    result = []
    for i in range(101):
        if i % 3 == 0 and i % 5 != 0:
            result.append(i)
    print(result)


def task15():
    import calendar
    year = int(input("Год: "))
    month = int(input("Месяц: "))
    result = calendar.month(year, month)
    print(result)
