# Felix Paulino Project: Conversion Calculator
# Program Name: Number Converter
# Purpose: This program converts numbers between the main 2 number systems we went over in class - binary and decimal and vice versa between both of them
# What the Code does: The code gives a list that give the user the ablity to choose the conversion type, then prompts for the input number and performs the conversion.

def decimal_to_binary(decimal_num):
    """Converts a decimal number to binary."""
    binary_num = ""
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
    return binary_num

def binary_to_decimal(binary_num):
    """Converts a binary number to decimal."""
    decimal_num = 0
    power = len(binary_num) - 1
    for digit in binary_num:
        decimal_num += int(digit) * (2 ** power)
        power -= 1
    return decimal_num

def main():
    print("Hello, Welcome to Felix Paulino's Conversion Calculator!")

    while True:
        print("\nList:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Leave Program")

        choice = input("Enter your choice: ")

        if choice == '1':
            binary_num = input("Enter a binary number: ")
            # Validate binary input
            if not all(bit in '01' for bit in binary_num):
                print("Invalid binary number!")
                continue
            print("Decimal version equals:", binary_to_decimal(binary_num))

        elif choice == '2':
            decimal_num = int(input("Enter a decimal number: "))
            print("Binary version equals:", decimal_to_binary(decimal_num))

        elif choice == '3':
            print("Thank you for using My Conversion Calculator!")
            break

        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    main()

# Comments-if not all bit in 01 for bit in binary_num basically means that if the binary number
#does not have a 0 or a 1 it is going to print invalid binary number
# Also power = len(binary_num) - 1 basically means that it will subtract 1 since binary number has a base of 2 and so
# therfore will always subtract 1 since binary is base 2
# https://github.com/ComputerGeek76/hardware_software_code
