import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(operation, number1, number2):
  result = ''
  if operation == 1:
    result = number1 + number2
  elif operation == 2:
    result = number1 - number2
  elif operation == 3:
    result = number1 * number2
  elif operation == 4:
    result = number1 / number2
  else:
    print("Niepoprawny kod działania")
    exit(1)
  return result


if __name__ == "__main__":
  operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
  number1 = input("Podaj pierwszą wartość liczbową działania: ")
  number2 = input("Podaj drugą wartość liczbową działania: ")
  logging.debug("Dodaję %s i %s" % (number1, number2))
  result = calculator(operation, number1, number2)
  logging.debug("Wynik to %s" % result)
  calculator(operation, number1, number2)
