# Version 1.0

def splitNumbers(numbers):
    numbers = numbers.replace("   ", "\n").replace("  ", "\n")
    return numbers.splitlines()

def scientificToStandardNotation(numbers, digits):
    if digits < 2 or digits > 20:
        return print("'digits' must be between 2 and 20")
    for number in numbers:
        numbers[numbers.index(number)] = round(float(number[:digits+1]) * 10 ** int(number[-2:]))
    return numbers

numbers = input("Paste your string of numbers: ")
digits = int(input("How many significant digits have those numbers: "))
print("")
list = scientificToStandardNotation(splitNumbers(numbers), digits)
list.sort()
for value in list:
    print(value)