def dec_to_binary(numbers):
    dec_list = {"0" , "1", "2", "3" , "4", "5", "6", "7" , "8" , "9" , "10"}
    for number in numbers:
        if number.upper() not in dec_list: # check if the number is not in dec_list
            print("Not a decimal number")
            return(False)
    return(True)


def main():
    good_selection = False
    while not good_selection:
        selection = input("Provide a decimal number:")
        good_selection = dec_to_binary(selection)
    print("Correct" , selection, "is a decimal number!!!")


if __name__ == "__main__":
    main()
