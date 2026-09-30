import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="logeg.log",
    filemode="a",
)


def devide(a, b):
    try:
        result = a / b
        logging.info(f" {a} devide by {b} is {result}")
        return result
    except ZeroDivisionError:
        logging.info(f"Devide by zero error")
        return "Divide by zero error"
    except:
        logging.info(f"Exeption occur")
        return "Exeption occur"


print(devide(10, 20))
print(devide("4", "b"))
