globalVar = 42

def my_address(str, var):
    print("{1} adress: {0}\n{1} value: {2}".format(id(var), str,var))

def ask_me(*num): # Ask the user for number
    if num[0] == 1:
        ans = int(input("Please provide a number:"))
        return ans
    elif num[0] == 2:
        print("What do you think you will get.")
        print("When you add globalVar + numl?")
        input("globalVar = {} and num = {} ".format(num[1], num[-1]))
    else:
        print("globalVar = {} and num = {} ".format(num[1], num[-1]))

def add(numl):
    globalVar = numl
    my_address('add globalVar', globalVar)
    globalVar = globalVar + numl
    print('In add function globalVar + numl = {}'.format(globalVar))

def global_add(numl):
    global globalVar
    my_address('globalVar adress', globalVar)
    globalVar = globalVar + numl
    print('In global_add globalVar + numl = {}'.format(globalVar))

def main():
    my_address('main globalVar', globalVar)
    numl = ask_me(1)
    my_address('main numl', numl)
    ask_me(2,globalVar, numl)
    sum = add(numl)
    ask_me(3,globalVar, sum)
    input("Why is that?")
    print("Now let's look at global_add")
    sum = global_add(num1)
    ask_me(3,globalVar, sum)

if __name__ == "__main__":
   main()
