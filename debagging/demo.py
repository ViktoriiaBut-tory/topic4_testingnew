def devide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Invalid input"
    except:
        return "Invalid case"


print(devide(10, 2))
print(devide(10, 0))
print(devide("10", "b"))
