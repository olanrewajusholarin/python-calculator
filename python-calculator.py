# made by cyber-turtle
# we leave the default values blank by using empty quotes so we can store data in them later
input1 = ""
input2 = ""
selector = ""
print("Choose from the list of operations below:")
print("* for multiplication")
print("/ for division")
print("- for subtraction")
print("+ for addition")
# we make use of the while loop so as to keep the program running till the user enters 'quit'
while selector != 'quit':
    selector = input("> ")
# if the value of selector is '*'
    if selector == '*':
        print('you have selected multiplication!')
        input1 = int(input("enter first number: "))
        input2 = int(input("enter second number: "))
        print(f'Answer:{input1 * input2}')
# if the value of selector is '/'
    elif selector == '/':
        print('you have selected division!')
        input1 = int(input("enter first number: "))
        input2 = int(input("enter second number: "))
        gym_vs_jim = float(input1 / input2)
        if input2 == '0':
            print('undefined bro')
        print(f'Answer:{gym_vs_jim}')
# if the value of selector is '-'
    elif selector == '-':
        print('you have selected subtraction!')
        input1 = int(input("enter first number: "))
        input2 = int(input("enter second number: "))
        print(f'Answer:{input1 - input2}')
# if the value of selector is '+'
    elif selector == '+':
        print('you have selected addition!')
        input1 = int(input("enter first number: "))
        input2 = int(input("enter second number: "))
        print(f'Answer:{input1 + input2}')
# if quit is entered,the program is terminated
    elif selector == 'quit':
        print("goodbye")
        break
    elif selector == 'help':
        print("Choose from the list of operations below:")
        print("* for multiplication")
        print("/ for division")
        print("- for subtraction")
        print("+ for addition")
# if none of our conditions are met we tell the program to print out
    else:
        print("you have inserted a character i do not understand, type 'help' "
              "to bring out a list of operations i can perform and 'quit' to "
              "escape the environment")
