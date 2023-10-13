def main():
    #get the inputs
    x = int(input("First Number: "))
    y = int(input("Second Number: "))

    #choose the operation
    op = input("Choose the operation: ").capitalize()

    #apply the selected operation
    if op == 'A':
        add(x, y)
    elif op == 'M':
        multi(x, y)
    elif op == 'S':
        sub(x, y)
    elif op == 'D':
        div(x, y)
    else:
        print("Invalid")

#define operation for multiplication
def multi(x, y):
    print(x * y)

#define operation for addition
def add(x, y):
    print(x + y)

#define operation for subtraction
def sub(x, y):
    print(x - y)

#define operation for division
def div(x, y):
    print(x / y)
    
#call main
main()