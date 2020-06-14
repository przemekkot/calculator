import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(operation, number1, number2):
  result = ''
  if int(operation) == 1:
    result = float(number1) + float(number2)
  elif int(operation) == 2:
    result = float(number1) - float(number2)
  elif int(operation) == 3:
    result = float(number1) * float(number2)
  elif int(operation) == 4:
    result = float(number1) / float(number2)
  return result


if __name__ == "__main__":
  operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
  if int(operation) not in [1, 2, 3, 4]:
    logging.debug("Niepoprawny kod działania")
    exit(1)
  number1 = input("Podaj pierwszą wartość liczbową działania: ")
  number2 = input("Podaj drugą wartość liczbową działania: ")
  if int(operation) == 1:
    logging.debug("Dodaję %s i %s" % (number1, number2))
  elif int(operation) == 2:
    logging.debug("Odejmuję %s i %s" % (number1, number2))
  elif int(operation) == 3:
    logging.debug("Mnożę %s i %s" % (number1, number2))
  elif int(operation) == 4:
    logging.debug("Dzielę %s i %s" % (number1, number2))
  result = calculator(operation, number1, number2)
  logging.debug("Wynik to %.2f" % result)
calculator(operation, number1, number2)
