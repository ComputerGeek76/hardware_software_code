def while_loop():
    lang_list = ["Python" , "JavaScript" , "PHP" , "Rust" , "Solidity" , "Assembly"]
    counter = 0
    while (counter < len(lang_list)):
        print(lang_list[counter])
        counter += 1

def for_loop():
    lang_list = ["Python" , "JavaScript" , "PHP" , "Rust" , "Solidity" , "Assembly"]
    for lang in lang_list:
        print(lang, end=" ")

def main():
    my_msg("for")
    for_loop()
    my_msg("while")
    while_loop()
